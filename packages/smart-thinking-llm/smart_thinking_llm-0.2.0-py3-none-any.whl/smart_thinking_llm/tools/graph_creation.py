import ast
import json
import logging
import os
import re
import time
import requests
from collections import defaultdict

import openai
import networkx as nx
from dotenv import load_dotenv
from pathlib import Path
from typing import List, Literal

from smart_thinking_llm.datasets.wikidata_dataset import WikiDataset
from smart_thinking_llm.datasets.data_classes import (
    Entity,
    EntityID,
    Object,
    Relation,
    RelationID,
)
from smart_thinking_llm.utils import init_basic_logger, make_openai_request

load_dotenv()


class Graph:
    def __init__(self, entity_to_entity_struct: dict[Entity, dict[Relation, Entity]]):
        self.entity_to_entity_struct = entity_to_entity_struct
        self.graph = nx.DiGraph()
        for entity_1, relations in entity_to_entity_struct.items():
            self.graph.add_node(entity_1, label=entity_1.id._id)
            for relation, entity_2 in relations.items():
                if entity_2 not in self.graph:
                    self.graph.add_node(entity_2, label=entity_2.id._id)
                self.graph.add_edge(entity_1, entity_2, label=relation.id._id)

    @staticmethod
    def node_match(n1, n2):
        return n1["label"] == n2["label"]

    @staticmethod
    def edge_match(e1, e2):
        return e1["label"] == e2["label"]

    def compare_to(
        self,
        other: "Graph",
        node_del_cost: float = 1.0,
        node_ins_cost: float = 1.0,
        edge_del_cost: float = 1.0,
        edge_ins_cost: float = 1.0,
    ) -> float:
        # TODO: add edge_subst_cost and node_subst_cost
        node_del = lambda _: node_del_cost
        node_ins = lambda _: node_ins_cost
        edge_del = lambda _: edge_del_cost
        edge_ins = lambda _: edge_ins_cost
        return nx.graph_edit_distance(
            self.graph,
            other.graph,
            node_match=self.node_match,
            edge_match=self.edge_match,
            node_del_cost=node_del,
            node_ins_cost=node_ins,
            edge_del_cost=edge_del,
            edge_ins_cost=edge_ins,
        )

    def __str__(self) -> str:
        if not self.entity_to_entity_struct:
            return "Graph is empty."

        def get_repr(item: object) -> str:
            """Helper to get a readable representation of an Entity, Relation, or Object."""
            aliases = getattr(item, "aliases", [])
            item_id = getattr(item, "id", "")
            name = aliases[0] if aliases else "N/A"
            return f"{name} ({item_id})"

        output_lines = []
        all_subjects = set(self.entity_to_entity_struct.keys())
        all_objects = {
            obj
            for relations_dict in self.entity_to_entity_struct.values()
            for obj in relations_dict.values()
        }

        # Start traversal from root nodes (those that are not objects of any relation)
        root_nodes = sorted(
            [s for s in all_subjects if s not in all_objects],
            key=lambda x: str(x.id),
        )

        # Also include other nodes to handle cycles or disconnected components
        other_nodes = sorted(
            [s for s in all_subjects if s in all_objects],
            key=lambda x: str(x.id),
        )

        processed_nodes = set()

        def build_tree(node: Entity, prefix: str = "", is_root: bool = True):
            if node in processed_nodes and not is_root:
                output_lines.append(f"{prefix}└─> (Cycle detected to {get_repr(node)})")
                return

            if is_root:
                output_lines.append(f"[{get_repr(node)}]")

            processed_nodes.add(node)

            if node in self.entity_to_entity_struct:
                relations = self.entity_to_entity_struct[node]
                children = sorted(list(relations.items()), key=lambda x: str(x[0].id))

                for i, (relation, obj) in enumerate(children):
                    is_last = i == len(children) - 1
                    connector = "└──" if is_last else "├──"
                    output_lines.append(
                        f"{prefix}{connector} {get_repr(relation)}: [{get_repr(obj)}]"
                    )

                    new_prefix = prefix + ("    " if is_last else "│   ")
                    if isinstance(obj, Entity):
                        build_tree(obj, new_prefix, is_root=False)

        # Process all components of the graph
        for node in root_nodes + other_nodes:
            if node not in processed_nodes:
                build_tree(node, is_root=True)
                output_lines.append("")  # Add a newline for separation

        return "\n".join(output_lines)


class GraphCreator:
    def __init__(
        self,
        entity_aliases_filepath: Path,
        relation_aliases_filepath: Path,
        dataset_filepath: Path,
        triplets_prompt_filepath: Path,
        openai_client: openai.OpenAI,
        triplets_model: Literal[
            "gpt-4.1-2025-04-14",
            "gpt-4.1-mini-2025-04-14",
            "gpt-4.1-nano-2025-04-14",
        ] = "gpt-4.1-nano-2025-04-14",
        norm_lev_threshold: float = 0.3,
        parse_graph_strategy: Literal[
            "no_info", # без знаний о сущностях внутри одной тройки или каких-либо еще
            "entities_info" # в коде используется информация о предсказанных подряд entity
        ] = "entities_info"
    ):
        self.entity_aliases_filepath = entity_aliases_filepath
        self.relation_aliases_filepath = relation_aliases_filepath
        self.dataset_filepath = dataset_filepath
        self.triplets_prompt_filepath = triplets_prompt_filepath
        self.triplets_model = triplets_model
        self.openai_client = openai_client
        self.logger = init_basic_logger("GraphCreator", logging.INFO)
        self.norm_lev_threshold = norm_lev_threshold
        self.parse_graph_strategy = parse_graph_strategy
        self.wikidata_dataset = WikiDataset(
            self.dataset_filepath,
            self.entity_aliases_filepath,
            self.relation_aliases_filepath,
        )

        with open(self.triplets_prompt_filepath, mode="r", encoding="utf-8") as f:
            self.triplets_prompt = f.read()

    def parse_triplets(self, triplets: str) -> dict[str, dict[str, str]]:
        triplets = triplets.strip().replace("\n", "")
        triplets_list = ast.literal_eval(triplets)
        triplets_dict = defaultdict(dict)
        for triplet in triplets_list:
            subject, question, answer = triplet
            triplets_dict[subject][question] = answer
        return triplets_dict

    def make_entity_request(
        self, object_name: str, action: str = "wbsearchentities"
    ) -> str:
        url = "https://www.wikidata.org/w/api.php"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        params = {
            "action": action,
            "language": "en",
            "format": "json",
            "search": object_name,
        }
        response = requests.get(url, params=params, headers=headers)
        try:
            response_json = response.json()
        except json.JSONDecodeError as e:
            self.logger.warning(f"Entity {object_name} not found in wikisearch")
            return ""
        if "search" not in response_json or not response_json["search"]:
            self.logger.warning(f"Entity {object_name} not found")
            return ""
        found_entity_id = response_json["search"][0]["id"]
        return found_entity_id

    @staticmethod
    def levenshtein_distance(s1: str, s2: str) -> int:
        if len(s1) < len(s2):
            return GraphCreator.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    def _find_relation_by_name_no_info(
        self, relation_name: str, entity_root: Entity
    ) -> Relation:
        min_distance = float("inf")
        min_relation = None
        for relation, _ in self.wikidata_dataset.get_all_children_of_entity(
            entity_root
        ):
            for alias in relation.aliases:
                distance = self.levenshtein_distance(alias, relation_name)
                normalized_distance = distance / len(relation_name)
                if normalized_distance < min_distance:
                    min_distance = normalized_distance
                    min_relation = relation
        if min_relation is None or min_distance > self.norm_lev_threshold:
            raise ValueError(f"Relation {relation_name} not found")
        return min_relation

    def _parse_graph_structure_no_info(self, triplets_dict: dict[str, dict[str, str]]) -> dict[Entity, dict[Relation, Entity]]:
        graph_structure = defaultdict(dict)
        for subject, relations in triplets_dict.items():
            # Add sleep to avoid rate limit
            entity_id = self.make_entity_request(subject)
            if not entity_id:
                self.logger.warning(
                    f"Skip triplet ({subject}, {relations}) because subject is not found in wikisearch"
                )
                continue
            try:
                entity = self.wikidata_dataset.get_object_by_str_id(entity_id)
            except KeyError as e:
                self.logger.warning(f"Entity {entity_id} is not an Entity. {e}")
                continue
            if not isinstance(entity, Entity):
                self.logger.warning(f"Entity {entity_id} is not an Entity")
                continue
            for relation, answer in relations.items():
                relation = self._find_relation_by_name_no_info(relation, entity)
                if relation is None:
                    self.logger.warning(
                        f"Skip triplet ({subject}, {relations}) because relation is not found"
                    )
                    continue
                # Add sleep to avoid rate limit
                answer_id = self.make_entity_request(answer)
                if not answer_id:
                    self.logger.warning(
                        f"Skip triplet ({subject}, {relations}) because answer is not found in wikisearch"
                    )
                    continue
                try:
                    answer = self.wikidata_dataset.get_object_by_str_id(answer_id)
                except KeyError as e:
                    self.logger.warning(f"Answer {answer_id} is not an Entity. {e}")
                    continue
                graph_structure[entity][relation] = answer
        return graph_structure
    
    def _find_relation_by_name_entities_info(self, relation_name: str, entity_start: Entity, entity_end: Entity) -> Relation:
        min_distance = float("inf")
        min_relation = None
        for relation, entity_end_current in self.wikidata_dataset.get_all_children_of_entity(entity_start):
            if entity_end_current == entity_end:
                continue
            for alias in relation.aliases:
                distance = self.levenshtein_distance(alias, relation_name)
                normalized_distance = distance / len(relation_name)
                if normalized_distance < min_distance:
                    min_distance = normalized_distance
                    min_relation = relation
        if min_relation is None or min_distance > self.norm_lev_threshold:
            self.logger.warning(f"Relation {relation_name} not found")
        return min_relation

    def _parse_graph_structure_entities_info(self, triplets_dict: dict[str, dict[str, str]]) -> dict[Entity, dict[Relation, Entity]]:
        graph_structure = defaultdict(dict)
        for subject, relations in triplets_dict.items():
            entity_id = self.make_entity_request(subject)
            if not entity_id:
                self.logger.warning(f"Skip triplet ({subject}, {relations}) because subject is not found in wikisearch")
                continue
            entity = self.wikidata_dataset.get_object_by_str_id(entity_id)
            if not isinstance(entity, Entity):
                self.logger.warning(f"Entity {entity_id} is not an Entity")
                continue
            for relation, answer in relations.items():
                answer_id = self.make_entity_request(answer)
                if not answer_id:
                    self.logger.warning(f"Skip triplet ({subject}, {relations}, {answer}) because answer is not found in wikisearch")
                    continue
                answer = self.wikidata_dataset.get_object_by_str_id(answer_id)
                if not isinstance(answer, Entity):
                    self.logger.warning(f"Answer {answer_id} is not an Entity")
                    continue
                relation = self._find_relation_by_name_entities_info(relation, entity, answer)
                if relation is None:
                    self.logger.warning(f"Skip triplet ({subject}, {relations}, {answer}) because relation is not found")
                    continue
                graph_structure[entity][relation] = answer
        return graph_structure

    def parse_graph_structure(
        self, triplets_dict: dict[str, dict[str, str]]
    ) -> dict[Entity, dict[Relation, Entity]]:
        if self.parse_graph_strategy == "no_info":
            return self._parse_graph_structure_no_info(triplets_dict)
        elif self.parse_graph_strategy == "entities_info":
            return self._parse_graph_structure_entities_info(triplets_dict)
        else:
            raise ValueError(f"Invalid parse graph strategy: {self.parse_graph_strategy}")

    def get_graph_from_path(self, path: str) -> Graph:
        graph_structure = defaultdict(dict)
        triple_pattern = re.compile(r'(?=(Q\d+)-(P\d+)-(Q\d+))')
        
        for match in triple_pattern.finditer(path):
            subject, predicate, obj = match.groups()
            subject = self.wikidata_dataset.get_object_by_str_id(subject)
            predicate = self.wikidata_dataset.get_object_by_str_id(predicate)
            obj = self.wikidata_dataset.get_object_by_str_id(obj)
            graph_structure[subject][predicate] = obj
        
        return Graph(graph_structure)

    def __call__(self, model_answer: str) -> Graph:
        prompt = self.triplets_prompt % model_answer
        triplets = make_openai_request(
            self.openai_client, self.triplets_model, prompt, self.logger
        ) # [("Donatus Djagom", "religious affiliation", "Catholicism"), ("Catholicism", "headquarters located", "Vatican City")]
        triplets_dict = self.parse_triplets(triplets) # {"Donatus Djagom": {"religious affiliation": "Catholicism"}, "Catholicism": {"headquarters located": "Vatican City"}}
        graph_structure = self.parse_graph_structure(triplets_dict)

        return Graph(graph_structure)


### !! USE EXAMPLES TO TEST THE GRAPH CREATION !!
def main():
    openai.api_key = os.environ.get("OPENAI_APIKEY")
    openai_client = openai.OpenAI()

    graph_creator = GraphCreator(
        entity_aliases_filepath=Path(
            "data/raw_data/wikidata5m_alias/wikidata5m_entity.txt"
        ),
        relation_aliases_filepath=Path(
            "data/raw_data/wikidata5m_alias/wikidata5m_relation.txt"
        ),
        dataset_filepath=Path(
            "data/raw_data/wikidata5m_transductive/wikidata5m_transductive_train.txt"
        ),
        triplets_prompt_filepath=Path(
            "smart_thinking_llm/prompts/generate_triplets_prompt.txt"
        ),
        openai_client=openai_client,
        parse_graph_strategy="entities_info"
    )

    # 2hop graph
    model_answer = """Feyenoord Rotterdam is based in the Netherlands.  
The head of government of the Netherlands is the Prime Minister.  
The Prime Minister of the Netherlands is Mark Rutte."""

    graph = graph_creator(model_answer)

    ground_truth_graph = Graph(
        {
            Entity(EntityID("Q134241"), aliases=["Feyenoord Rotterdam"]): {
                Relation(RelationID("P17"), aliases=["based in"]): Entity(
                    EntityID("Q55"), aliases=["the Netherlands"]
                ),
            },
            Entity(EntityID("Q55"), aliases=["the Netherlands"]): {
                Relation(RelationID("P6"), aliases=["head of government"]): Entity(
                    EntityID("Q57792"),
                    aliases=["Marc Rutte", "mark rutt", "rutte, mark", "Mark Rutte"],
                ),
            },
        }
    )
    print("=" * 50, "2hop graph", "=" * 50)
    print("*" * 10, "Generated graph", "*" * 10)
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 10))
    nx.draw(graph.graph, with_labels=True)
    plt.savefig("generated_graph_2hop.png")
    plt.close()
    print("*" * 10, "Ground truth graph", "*" * 10)
    print(ground_truth_graph)
    print(f"Graph edit distance: {graph.compare_to(ground_truth_graph)}")
    print("=" * 100)

    # 3hop graph
    model_answer = """Miyankuh-e Gharbi is located in Iran. Iran shares a border with Pakistan. The highest peak in Pakistan is K2, which rises to 8,611 metres above sea level."""

    graph = graph_creator(model_answer)

    ground_truth_graph = Graph(
        {
            Entity(EntityID("Q6884371"), aliases=["Miyankuh-e Gharbi"]): {
                Relation(RelationID("P17"), aliases=["country"]): Entity(
                    EntityID("Q794"), aliases=["Persian State of Iran"]
                ),
            },
            Entity(EntityID("Q794"), aliases=["Persian State of Iran"]): {
                Relation(RelationID("P47"), aliases=["shares border with"]): Entity(
                    EntityID("Q227"), aliases=["azerbajani"]
                ),
            },
            Entity(EntityID("Q227"), aliases=["Pakistan"]): {
                Relation(RelationID("P610"), aliases=["highest peak"]): Entity(
                    EntityID("Q725591"), aliases=["bazardüzü"]
                ),
            },
        }
    )
    print("=" * 50, "3hop graph", "=" * 50)
    print("*" * 10, "Generated graph", "*" * 10)
    plt.figure(figsize=(10, 10))
    nx.draw(graph.graph, with_labels=True)
    plt.savefig("generated_graph_3hop.png")
    plt.close()
    print("*" * 10, "Ground truth graph", "*" * 10)
    print(ground_truth_graph)
    print(f"Graph edit distance: {graph.compare_to(ground_truth_graph)}")
    print("=" * 100)


if __name__ == "__main__":
    main()

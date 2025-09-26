import networkx as nx
import yaml
from typing import Literal
from cwl_utils.parser import (
    Workflow,
    load_document,
    cwl_version,
    WorkflowInputParameter,
    WorkflowOutputParameter,
    WorkflowStep,
    WorkflowStepInput,
    WorkflowStepOutput,
)
from cwl_utils.parser.cwl_v1_0 import LoadingOptions as LoadingOptionsV10
from cwl_utils.parser.cwl_v1_1 import LoadingOptions as LoadingOptionsV11
from cwl_utils.parser.cwl_v1_2 import LoadingOptions as LoadingOptionsV12
from cwl_utils.parser.cwl_v1_0 import WorkflowStepOutput as WorkflowStepOutputV10
from cwl_utils.parser.cwl_v1_1 import WorkflowStepOutput as WorkflowStepOutputV11
from cwl_utils.parser.cwl_v1_2 import WorkflowStepOutput as WorkflowStepOutputV12

from cwl2nx.term_viz import dag_to_str

NodeType = (
    WorkflowStep
    | WorkflowStepInput
    | WorkflowStepOutput
    | WorkflowInputParameter
    | WorkflowOutputParameter
)
NodeTypeStr = Literal[
    "WorkflowStep",
    "WorkflowStepInput",
    "WorkflowStepOutput",
    "WorkflowInputParameter",
    "WorkflowOutputParameter",
]

# DEFAULT_DISPLAY_PARAMS: dict[NodeTypeStr, dict[str, str | float | int]] = {
#     "WorkflowStep": {"color": "blue", "shape": "o", "size": 500},
#     "WorkflowStepInput": {"color": "blue", "shape": "o", "size": 500},
#     "WorkflowStepOutput": {"color": "blue", "shape": "o", "size": 500},
#     "WorkflowInputParameter": {"color": "blue", "shape": "o", "size": 500},
#     "WorkflowOutputParameter": {"color": "blue", "shape": "o", "size": 500},
# }
DEFAULT_DISPLAY_PARAMS: dict[NodeTypeStr, dict[str, str | float | int]] = {
    "WorkflowStep": {"color": "blue"},
    "WorkflowStepInput": {"color": "blue"},
    "WorkflowStepOutput": {"color": "blue"},
    "WorkflowInputParameter": {"color": "blue"},
    "WorkflowOutputParameter": {"color": "blue"},
}


class CWLToNetworkxConnector:
    def __init__(
        self,
        cwl_path: str,
        display_params: dict[
            NodeTypeStr, dict[str, str | float | int]
        ] = DEFAULT_DISPLAY_PARAMS,
    ):
        r"""
        Initialize the connector.
        Parse and validate the cwl file, with cwl_utils library.

        Parameters :
        ---

        - cwl_path: path to the cwl file
        - display_params : display parameters for nodes of graph (can be any dictionnary)

            example value for display_params :

                ```
                {
                    "WorkflowStep": {"color": "blue", "shape": "o", "size": 500},
                    "WorkflowStepInput": {"color": "blue", "shape": "o", "size": 500},
                    "WorkflowStepOutput": {"color": "blue", "shape": "o", "size": 500},
                    "WorkflowInputParameter": {"color": "blue", "shape": "o", "size": 500},
                    "WorkflowOutputParameter": {"color": "blue", "shape": "o", "size": 500},
                }
                ```
            see : https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.display.html

        """
        self.cwl_path = cwl_path
        self.verbose_node_names = True
        self.display_params = display_params

        self.cwl_utils_graph: Workflow = self.parse_and_validate_cwl()
        self.nx_graph: nx.DiGraph = nx.DiGraph()

    def parse_and_validate_cwl(self) -> Workflow:
        r"""
        Parse the cwl in an Workflow object from cwl_utils
        parser submodule.

        Returns :
        ---
        The Workflow object from cwl_utils library, validated.
        """
        try:
            with open(self.cwl_path, "rt") as f:
                raw_yaml = yaml.safe_load(f)
            self.cwl_version = cwl_version(raw_yaml)

            loading_options = None
            match self.cwl_version:
                case "v1.0":
                    loading_options = LoadingOptionsV10(no_link_check=True)
                case "v1.1":
                    loading_options = LoadingOptionsV11(no_link_check=True)
                case "v1.2":
                    loading_options = LoadingOptionsV12(no_link_check=True)
                case _:
                    raise ValueError(
                        f"Unexcpected cwl_version in cwl file : {self.cwl_version}"
                    )

            parsed_cwl = load_document(raw_yaml, loadingOptions=loading_options)
            # add a proper label for each step
            for each_step in parsed_cwl.steps:
                if self.verbose_node_names:
                    each_step.label = each_step.id
                else:
                    each_step.label = each_step.id.split("/")[-1]

        except Exception:
            raise Exception(f"Could not parse and validate the cwl file.")
        else:
            return parsed_cwl

    def create_nx_node_from_cwl(
        self, node_id: str, cwl_utils_object: NodeType, node_type_str: NodeTypeStr
    ):
        if node_id in self.nx_graph.nodes:
            return
        self.nx_graph.add_node(node_id)
        self.nx_graph.nodes[node_id]["cwl_utils_object"] = cwl_utils_object
        display_params_input = self.display_params[node_type_str]

        # adding display params in the node
        for each_key, each_value in display_params_input.items():
            self.nx_graph.nodes[node_id][each_key] = each_value
        self.nx_graph.nodes[node_id]["node_type"] = node_type_str

    def convert_to_networkx(self) -> nx.DiGraph:
        r"""
        Convert the cwl_utils.parser.Workflow in a networkx graph. The graph contains
        five types of nodes (following cwl_utils structure):

        - WorkflowStep
        - WorkflowStepInput
        - WorkflowStepOutput
        - WorkflowInputParameter
        - WorkflowOutputParameter

        The above cwl_utils objects are accessible trough parameter 'cwl' of the networkx node :

        Example :

        ```python
        g.nodes[node_name]["cwl_utils_object"]
        >  <class 'cwl_utils.parser.cwl_v1_0.WorkflowStep'>
        ```

        Returns :
        ---
        The networkx DiGraph associated with the cwl, with cwl_utils objects accessible in nodes:
            - WorkflowStep
            - WorkflowStepInput
            - WorkflowStepOutput
            - WorkflowInputParameter
            - WorkflowOutputParameter
        """
        primary_node_type: dict[NodeTypeStr, list] = {
            "WorkflowStep": self.cwl_utils_graph.steps,
            "WorkflowInputParameter": self.cwl_utils_graph.inputs,
            "WorkflowOutputParameter": self.cwl_utils_graph.outputs,
        }

        # creating WorkflowStep, WorkflowInputParameter and WorkflowOutputParameter nodes
        for (
            each_primary_node_type,
            each_cwl_utils_object_list,
        ) in primary_node_type.items():
            for each_cwl_utils_object in each_cwl_utils_object_list:
                self.create_nx_node_from_cwl(
                    node_id=each_cwl_utils_object.id,
                    cwl_utils_object=each_cwl_utils_object,
                    node_type_str=each_primary_node_type,
                )

        # creating inputs and linking them to steps
        for each_step in self.cwl_utils_graph.steps:
            for each_input in each_step.in_:
                if each_input.source in self.nx_graph.nodes:
                    self.nx_graph.add_edge(each_input.source, each_step.id)
                    continue
                self.create_nx_node_from_cwl(
                    node_id=each_input.source,
                    cwl_utils_object=each_input,
                    node_type_str="WorkflowStepInput",
                )
                self.nx_graph.add_edge(each_input.source, each_step.id)

        # linking step to their outputs (who are existing inputs or WorkflowOutputParameter)
        for each_step in self.cwl_utils_graph.steps:
            for each_output in each_step.out:
                if each_output in self.nx_graph.nodes:
                    self.nx_graph.add_edge(each_step.id, each_output)
                    continue

                # case where output of step is also a WorkflowOutput
                for each_wf_output in self.cwl_utils_graph.outputs:
                    if each_wf_output.outputSource == each_output:
                        self.nx_graph.add_edge(each_step.id, each_wf_output.id)
                        break
                else:  # if output is neither a node nor a WorkflowOutput
                    # then its a WorkflowStepOutput not linked to any WorkflowStepInput
                    match self.cwl_version:
                        case "v1.0":
                            constructor = WorkflowStepOutputV10
                        case "v1.1":
                            constructor = WorkflowStepOutputV11
                        case "v1.2":
                            constructor = WorkflowStepOutputV12
                        case _:
                            raise ValueError(
                                f"Unexpected value for cwl_version : {self.cwl_version}"
                            )
                    self.create_nx_node_from_cwl(
                        node_id=each_output,
                        cwl_utils_object=constructor(each_output),
                        node_type_str="WorkflowStepOutput",
                    )
                    self.nx_graph.add_edge(each_step.id, each_output)
        if not nx.is_directed_acyclic_graph(self.nx_graph):
            raise Exception(f"The parsed graph is not a DAG (Directed Acyclic Graph).")

        return self.nx_graph

    def remove_dataset_nodes(self):
        drop_nodes = []
        for each_node_name in self.nx_graph.nodes:
            this_node = self.nx_graph.nodes[each_node_name]
            if this_node["cwl"]["node_type"] in ["input", "output"]:
                # add an edge between steps
                drop_nodes.append(each_node_name)
                for each_predecessor in self.nx_graph.predecessors(each_node_name):
                    for each_successor in self.nx_graph.successors(each_node_name):
                        self.nx_graph.add_edge(
                            each_predecessor, each_successor, label=this_node["label"]
                        )

        self.nx_graph.remove_nodes_from(drop_nodes)  # drop the input and output nodes


def cwl_to_str(dir: str, verbose=False) -> str:
    """
    Convert cwl to networkx, and then convert the nx.DiGraph
    in a easy-to-read string.

    Parameters :
    ---
    - dir: directory of the cwl file
    - verbose: whether to show full id's of cwl objects, or just
        the end (their path from the current working directory)

    Returns :
    ---
    A str that displays as a DAG
    """
    g = CWLToNetworkxConnector(dir).convert_to_networkx()
    if not verbose:
        import os

        to_drop = f"file://{os.getcwd()}/#"
        mapping = {each_node: each_node.replace(to_drop, "") for each_node in g.nodes}
        g = nx.relabel_nodes(g, mapping=mapping)
    return dag_to_str(g, round_angle=True)


if __name__ == "__main__":
    # from cwl2nx import CWLToNetworkxConnector, cwl_to_str

    dir = "workflow_example.cwl.yaml"
    print(cwl_to_str(dir))

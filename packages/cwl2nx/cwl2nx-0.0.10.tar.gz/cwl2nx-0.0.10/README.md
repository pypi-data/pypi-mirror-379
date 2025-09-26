# CWL2Nx

Lightweight python module to load, validate and visualize CWL (Common Workflow Language) files through networkx graphs.
It uses [cwl_utils](https://github.com/common-workflow-language/cwl-utils) for parsing and validation.

## Installation

```
pip install cwl2nx
```

## Example Usage

> You will find an example of workflow in the GitHub repository : [workflow_example.cwl.yaml](https://raw.githubusercontent.com/mariusgarenaux/cwl2nx/refs/heads/main/workflow_example.cwl.yaml). Other examples can be found here : https://workflowhub.org

### Straightforward conversion

```python
from cwl2nx import CWLToNetworkxConnector

dir = "workflow_example.cwl.yaml"
dag = CWLToNetworkxConnector(dir).convert_to_networkx() # dag is networkx.DiGraph
print(dag.nodes, dag.edges)
```

### Using dagviz

> You'll need to install [`dagviz`](https://wimyedema.github.io/dagviz/index.html#installing) before

> /!\ you need to run the code below in a jupyter notebook

```python
from cwl2nx import CWLToNetworkxConnector
import networkx as nx
import dagviz

dir = "workflow_example.cwl.yaml"
connector = CWLToNetworkxConnector(dir)
dag = connector.convert_to_networkx()


dagviz.Dagre(dag)

dagviz.Metro(dag) # github tree dag style
```

![Dagre](https://github.com/mariusgarenaux/cwl2nx/blob/main/doc/dagviz_Dagre.png?raw=true)

![Metro](https://github.com/mariusgarenaux/cwl2nx/blob/main/doc/dagviz_Metro.png?raw=true)

### Visualization in the terminal

To get a string representing the graph (code from: https://github.com/ctongfei/py-dagviz):

```python
from cwl2nx import cwl_to_str

dir = "workflow_example.cwl.yaml"
print(cwl_to_str(dir))
```

output : 

```text
• input_file_1.json
│ • parameter.py
│ │ • config.yaml
╰─│─┴─• init_task
  │   ╰─• init_task/initialized_dataset.json
  ╰─────┼─• inter_task_1
        ╰─│─• inter_task_2
          ╰─│─• inter_task_1/output_inter_1
            ╰─│─• inter_task_2/output_inter_2
              ╰─┴─• end_task
                  ╰─• wf_output
```

## Link with cwl-utils

Each node of the parsed networkx graph object has an attribute `cwl_utils_object` containing the cwl_utils object, among the following :

- WorkflowStep
- WorkflowStepInput
- WorkflowStepOutput
- WorkflowInputParameter
- WorkflowOutputParameter

The type of the node (one of the above in string) is accessible through the parameter `node_type` of each node.

## License

[Apache 2.0](LICENSE-2.0.txt)
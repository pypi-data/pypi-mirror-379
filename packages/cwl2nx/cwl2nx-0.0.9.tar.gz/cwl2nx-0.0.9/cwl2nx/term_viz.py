# Code adapted from : https://github.com/ctongfei/py-dagviz

# MIT License

# Copyright (c) 2022 Tongfei Chen

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Hashable, Dict, List
import array
import networkx as nx


def dag_to_str(g: nx.DiGraph, round_angle: bool = False) -> str:
    """
    Function highly inspired from https://github.com/ctongfei/py-dagviz/blob/main/dagviz.py

    Creates a text rendering of a directed acyclic graph (DAG) for visualization purposes in a terminal.

    :param g: A directed acyclic graph, of type `nx.DiGraph`
    :param round_angle: Whether to use a round-angled box drawing character or not
    :return: A multi-line string representation of the directed acyclic graph, each line corresponding to a node
    """
    assert nx.is_directed_acyclic_graph(g), "Graph contains cycles"

    rows: List[Hashable] = []
    node_to_row: Dict[Hashable, int] = {}
    indents: List[int] = []

    def _process_dag(g: nx.DiGraph, indent: int):
        for sg in nx.weakly_connected_components(g):
            _process_component(g.subgraph(sg), indent=indent)

    def _process_component(g: nx.DiGraph, indent: int):
        sources = [v for v in g.nodes if g.in_degree(v) == 0]
        for i in range(len(sources)):
            node_to_row[sources[i]] = len(rows)
            rows.append(sources[i])
            indents.append(indent + i)
        _process_dag(
            g.subgraph(set(g.nodes).difference(sources)), indent=indent + len(sources)
        )

    _process_dag(g, indent=0)
    a = [array.array("u", [" "] * indents[i] * 2) for i in range(len(rows))]
    for i, u in enumerate(rows):
        successors = sorted(g.successors(u), key=lambda v: node_to_row[v])
        if len(successors) == 0:
            continue
        l = node_to_row[successors[-1]]
        for j in range(i + 1, l):
            a[j][indents[i] * 2] = "│"
        for v in successors[:-1]:
            j = node_to_row[v]
            a[j][indents[i] * 2] = (
                "┼" if indents[i] > 0 and a[j][indents[i] * 2 - 1] == "─" else "├"
            )
            for k in range(indents[i] * 2 + 1, indents[j] * 2):
                a[j][k] = "─"
        a[l][indents[i] * 2] = (
            "┴"
            if indents[i] > 0 and a[l][indents[i] * 2 - 1] == "─"
            else ("╰" if round_angle else "└")
        )
        for k in range(indents[i] * 2 + 1, indents[l] * 2):
            a[l][k] = "─"

    lines: List[str] = [
        l.tounicode() + "• " + str(i).replace("\n", " ") for l, i in zip(a, rows)
    ]
    return "\n".join(lines)

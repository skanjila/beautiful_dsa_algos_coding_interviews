from beautiful_dsa_algos_coding_interviews.search.dfs.clone_graph import (
    GraphNode,
    clone_graph,
)


def test_clone_graph_cycle():
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node1.neighbors = [node2]
    node2.neighbors = [node1]

    cloned = clone_graph(node1)

    assert cloned is not node1
    assert cloned.val == 1
    assert cloned.neighbors[0] is not node2
    assert cloned.neighbors[0].val == 2
    assert cloned.neighbors[0].neighbors[0] is cloned

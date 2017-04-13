
import sys
from graph import Graph

def calc_min_deletions(n, edges):
    graph = Graph()
    for i in range(1, n + 1):
        graph.add_vertex(i)

    for edge in edges:
        graph.add_edge(edge)

    min_deletions = sys.maxint
    for root in range(1, n + 1):
        min_deletions = min(min_deletions, N - max_subtree_nodes(root, 0, graph))
    return min_deletions

def max_subtree_nodes(current_node, parent, graph):
    max_two = []

    for x in neighbors of current_node:
        if x == parent:
            continue
        max_two
        update max_two with max_subtree_nodes(x, current_node)
    if len(max_two) == 2:
        return 1 + sum(max_two)
    return 1

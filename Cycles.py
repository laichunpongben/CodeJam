# Google Code Jam
# Practice Contests
# Practice Contest
# Problem C. Cycles

# Solved for small dataset

from graph import Graph

class TestCase:
    def __init__(self, n, not_adj_edges):
        self.vertex_count = n
        self.forbidden_edges = not_adj_edges
        
    def count_hamiltonian_path(self):
        graph = Graph(create_graph_dict_by_forbidden_edges(self.vertex_count, self.forbidden_edges))
        paths = graph.find_all_hamiltonian_paths()
        path_count = round(len(paths) / len(graph.vertices()) / 2)
        return path_count

def initialize_test_cases():
    global test_cases
    test_cases[0] = TestCase(4, [[1, 2]])
    test_cases[1] = TestCase(8, [[1, 2], [2, 3], [4, 5], [5, 6]])
    test_cases[2] = TestCase(10, [[5, 4], [8, 9], [1, 6], [3, 2], [7, 10]])
    test_cases[3] = TestCase(10, [[3, 6], [4, 3], [5, 9], [10, 2], [4, 1], [1, 2], [7, 8], [6, 5], [9, 8], [7, 10]])
    test_cases[4] = TestCase(8, [[2, 3], [4, 2], [2, 6], [2, 5]])
    test_cases[5] = TestCase(6, [[5, 6], [4, 2], [3, 4], [3, 1], [3, 6], [5, 3], [3, 2], [5, 1], [1, 4], [6, 4], [4, 5], [5, 2], [1, 6], [2, 1], [2, 6]])
    test_cases[6] = TestCase(10, [[1, 7], [10, 4], [6, 5], [2, 3], [8, 4], [1, 3], [6, 9], [2, 4], [1, 5], [8, 5]])
    test_cases[7] = TestCase(10, [[2, 5], [4, 5], [9, 5], [7, 1], [9, 8], [2, 10], [7, 8], [9, 6], [9, 10], [2, 6]])
    test_cases[8] = TestCase(10, [[9, 5], [3, 2], [4, 10], [1, 10], [1, 6], [7, 10], [9, 4], [7, 6], [10, 6], [2, 9], [4, 1], [5, 1], [8, 5], [4, 7], [8, 2]])
    test_cases[9] = TestCase(10, [[2, 8], [9, 6], [10, 1], [3, 9], [2, 3], [1, 6], [8, 4], [6, 3], [7, 4], [6, 8], [4, 10], [3, 8], [3, 7], [1, 7], [9, 5]])

def neighbour(vertex_count, forbidden_edges, x):
    return [y+1 for y in range(vertex_count) if (x != y) and ([x + 1, y + 1] not in forbidden_edges) and ([y + 1, x + 1] not in forbidden_edges)]
        
def create_graph_dict_by_forbidden_edges(vertex_count, forbidden_edges):
    return {x+1: neighbour(vertex_count, forbidden_edges, x) for x in range(vertex_count)}
    
def print_all_results():
    for x in range(len(test_cases)):
        print("Case #" + str(x + 1) + ": " + str(test_cases[x].count_hamiltonian_path() % 9901))

test_cases = [0 for x in range(10)]
initialize_test_cases()
print_all_results()

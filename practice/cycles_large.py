# Google Code Jam
# Practice Contests
# Practice Contest
# Problem C. Cycles

# Unsolved for large dataset

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
    test_cases[2] = TestCase(30, [[5, 29], [12, 16], [25, 17], [18, 30], [27, 10], [4, 23], [20, 3], [1, 24], [26, 19], [14, 9], [6, 22], [8, 13], [15, 21], [28, 7], [11, 2]])
    test_cases[3] = TestCase(15, [[6, 13], [7, 4], [6, 10], [1, 4], [11, 13], [11, 7], [12, 3], [15, 8], [9, 14], [5, 10], [3, 2], [2, 8], [14, 12], [1, 15], [5, 9]])
    test_cases[4] = TestCase(300, [[246, 171], [36, 246], [238, 36], [191, 238], [171, 233], [36, 233], [191, 233], [246, 191], [171, 238]])
    test_cases[5] = TestCase(6, [[1, 2], [1, 3], [2, 6], [3, 5], [5, 6], [1, 6], [6, 3], [1, 5], [6, 4], [3, 2], [4, 1], [4, 5], [2, 4], [2, 5], [4, 3]])
    test_cases[6] = TestCase(100, [[50, 68], [50, 29], [37, 31], [54, 21], [87, 68], [54, 29], [37, 68], [54, 24], [77, 24], [85, 43], [50, 26], [54, 43], [85, 76], [85, 21], [87, 24]])
    test_cases[7] = TestCase(100, [[61, 77], [51, 37], [1, 16], [88, 77], [51, 16], [1, 76], [66, 77], [61, 69], [59, 69], [88, 16], [17, 76], [51, 77], [66, 76], [59, 30], [51, 76]])
    test_cases[8] = TestCase(300, [[94, 231], [227, 75], [187, 194], [144, 154], [15, 175], [180, 214], [163, 78], [189, 276], [111, 220], [295, 33], [147, 18], [38, 36], [254, 292], [74, 144], [226, 129]])
    test_cases[9] = TestCase(300, [[291, 170], [258, 197], [144, 166], [139, 194], [166, 82], [144, 291], [170, 82], [86, 197], [291, 82], [139, 258], [82, 194], [144, 82], [139, 291], [258, 86], [197, 166]])

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

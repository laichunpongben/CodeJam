# Google Code Jam
# Practice Contests
# Practice Contest
# Problem C. Cycles

from Graph import Graph

inputTestCases = [0 for x in range(10)]

class TestCase:
    def __init__(self, n, notAdjEdges):
        self.vertexCount = n
        self.forbiddenEdges = notAdjEdges

def InitializeTestCases():
    global inputTestCases
    
    inputTestCases[0] = TestCase(4, [[1, 2]])
    inputTestCases[1] = TestCase(8, [[1, 2], [2, 3], [4, 5], [5, 6]])
    inputTestCases[2] = TestCase(30, [[5, 29], [12, 16], [25, 17], [18, 30], [27, 10], [4, 23], [20, 3], [1, 24], [26, 19], [14, 9], [6, 22], [8, 13], [15, 21], [28, 7], [11, 2]])
    inputTestCases[3] = TestCase(15, [[6, 13], [7, 4], [6, 10], [1, 4], [11, 13], [11, 7], [12, 3], [15, 8], [9, 14], [5, 10], [3, 2], [2, 8], [14, 12], [1, 15], [5, 9]])
    inputTestCases[4] = TestCase(300, [[246, 171], [36, 246], [238, 36], [191, 238], [171, 233], [36, 233], [191, 233], [246, 191], [171, 238]])
    inputTestCases[5] = TestCase(6, [[1, 2], [1, 3], [2, 6], [3, 5], [5, 6], [1, 6], [6, 3], [1, 5], [6, 4], [3, 2], [4, 1], [4, 5], [2, 4], [2, 5], [4, 3]])
    inputTestCases[6] = TestCase(100, [[50, 68], [50, 29], [37, 31], [54, 21], [87, 68], [54, 29], [37, 68], [54, 24], [77, 24], [85, 43], [50, 26], [54, 43], [85, 76], [85, 21], [87, 24]])
    inputTestCases[7] = TestCase(100, [[61, 77], [51, 37], [1, 16], [88, 77], [51, 16], [1, 76], [66, 77], [61, 69], [59, 69], [88, 16], [17, 76], [51, 77], [66, 76], [59, 30], [51, 76]])
    inputTestCases[8] = TestCase(300, [[94, 231], [227, 75], [187, 194], [144, 154], [15, 175], [180, 214], [163, 78], [189, 276], [111, 220], [295, 33], [147, 18], [38, 36], [254, 292], [74, 144], [226, 129]])
    inputTestCases[9] = TestCase(300, [[291, 170], [258, 197], [144, 166], [139, 194], [166, 82], [144, 291], [170, 82], [86, 197], [291, 82], [139, 258], [82, 194], [144, 82], [139, 291], [258, 86], [197, 166]])
        
def Neighbour(vertexCount, forbiddenEdges, x):
    return [y+1 for y in range(vertexCount) if (x != y) and ([x + 1, y + 1] not in forbiddenEdges) and ([y + 1, x + 1] not in forbiddenEdges)]
        
def CreateGraphDictByForbiddenEdges(vertexCount, forbiddenEdges):
    return {x+1: Neighbour(vertexCount, forbiddenEdges, x) for x in range(vertexCount)}
    
def ComputeHamiltonianPathCount(testCase):
    graph = Graph(CreateGraphDictByForbiddenEdges(testCase.vertexCount, testCase.forbiddenEdges))
    paths = graph.find_all_hamiltonian_paths()
    pathsCount = round(len(paths) / len(graph.vertices()) / 2)
    return pathsCount
    
def PrintAllResults():
    InitializeTestCases()
    for x in range(len(inputTestCases)):
        print("Case #" + str(x + 1) + ": " + str(ComputeHamiltonianPathCount(inputTestCases[x]) % 9901))
    
PrintAllResults()
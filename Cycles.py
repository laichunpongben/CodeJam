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
    inputTestCases[2] = TestCase(10, [[5, 4], [8, 9], [1, 6], [3, 2], [7, 10]])
    inputTestCases[3] = TestCase(10, [[3, 6], [4, 3], [5, 9], [10, 2], [4, 1], [1, 2], [7, 8], [6, 5], [9, 8], [7, 10]])
    inputTestCases[4] = TestCase(8, [[2, 3], [4, 2], [2, 6], [2, 5]])
    inputTestCases[5] = TestCase(6, [[5, 6], [4, 2], [3, 4], [3, 1], [3, 6], [5, 3], [3, 2], [5, 1], [1, 4], [6, 4], [4, 5], [5, 2], [1, 6], [2, 1], [2, 6]])
    inputTestCases[6] = TestCase(10, [[1, 7], [10, 4], [6, 5], [2, 3], [8, 4], [1, 3], [6, 9], [2, 4], [1, 5], [8, 5]])
    inputTestCases[7] = TestCase(10, [[2, 5], [4, 5], [9, 5], [7, 1], [9, 8], [2, 10], [7, 8], [9, 6], [9, 10], [2, 6]])
    inputTestCases[8] = TestCase(10, [[9, 5], [3, 2], [4, 10], [1, 10], [1, 6], [7, 10], [9, 4], [7, 6], [10, 6], [2, 9], [4, 1], [5, 1], [8, 5], [4, 7], [8, 2]])
    inputTestCases[9] = TestCase(10, [[2, 8], [9, 6], [10, 1], [3, 9], [2, 3], [1, 6], [8, 4], [6, 3], [7, 4], [6, 8], [4, 10], [3, 8], [3, 7], [1, 7], [9, 5]])
        
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

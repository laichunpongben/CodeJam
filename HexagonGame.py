# Google Code Jam
# Practice Contests
# Code Jam Beta 2008
# Problem D. Hexagon Game

from Graph import Graph

class HexagonGraph:
    def __init__(self, s):
        self.size = s
        self.vertexCount = round((3 * s ** 2 + 1) / 4)
        self.sideLength = round((s + 1) / 2)
        self.vertex = [[] for x in range(s)]
        self.edges = {}
        
        self.InitializeVertices()
        self.InitializeEdges()
        
        
    def InitializeVertices(self):
        x = 0
        y = 0
        maxY = self.sideLength
        for v in range(self.vertexCount):
            self.vertex[x].append(v + 1)
            y += 1
            if (y == maxY): 
                x += 1
                y = 0
                if (x < self.sideLength): maxY += 1
                else: maxY += -1
                
    def InitializeEdges(self):
        for x in range(len(self.vertex)): 
            for y in range(len(self.vertex[x])):
                #print(str(x) + ',' + str(y) + ',' + str(self.vertex[x][y]))
                self.edges[self.vertex[x][y]] = []
                if (y > 0): self.edges[self.vertex[x][y]] += [self.vertex[x][y - 1]]
                if (y < len(self.vertex[x]) - 1): self.edges[self.vertex[x][y]] += [self.vertex[x][y + 1]]
                if (x > 0): 
                    if (x < self.sideLength and y > 0): self.edges[self.vertex[x][y]] += [self.vertex[x - 1][y - 1]]
                    elif (x >= self.sideLength): self.edges[self.vertex[x][y]] += [self.vertex[x - 1][y]]
                    
                    if (x < self.sideLength and y < len(self.vertex[x]) - 1): self.edges[self.vertex[x][y]] += [self.vertex[x - 1][y]]
                    elif (x >= self.sideLength): self.edges[self.vertex[x][y]] += [self.vertex[x - 1][y + 1]]
                if (x < len(self.vertex) - 1):
                    if (x >= self.sideLength - 1 and y > 0): self.edges[self.vertex[x][y]] += [self.vertex[x + 1][y - 1]]
                    elif (x < self.sideLength - 1): self.edges[self.vertex[x][y]] += [self.vertex[x + 1][y]]
                    
                    if (x >= self.sideLength - 1 and y < len(self.vertex[x]) - 1): self.edges[self.vertex[x][y]] += [self.vertex[x + 1][y]]
                    elif (x < self.sideLength - 1): self.edges[self.vertex[x][y]] += [self.vertex[x + 1][y + 1]]
        
h = HexagonGraph(7)
g = Graph(h.edges)
path = g.find_all_paths(1, 18)
print(path)
#g.find_all_paths(1, 3)

#for x in range(a.vertexCount):
#    print(a.edges[x + 1])

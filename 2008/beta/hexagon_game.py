# Google Code Jam
# Practice Contests
# Code Jam Beta 2008
# Problem D. Hexagon Game

# Unsolved

from graph import Graph

class HexagonGraph:
    def __init__(self, s):
        self.size = s
        self.vertex_count = round((3 * s ** 2 + 1) / 4)
        self.side_length = round((s + 1) / 2)
        self.vertex = [[] for x in range(s)]
        self.edges = {}
        
        self.initialize_vertices()
        self.initialize_edges()
        
    def initialize_vertices(self):
        x = 0
        y = 0
        max_y = self.side_length
        for v in range(self.vertex_count):
            self.vertex[x].append(v + 1)
            y += 1
            if (y == max_y): 
                x += 1
                y = 0
                if (x < self.side_length): max_y += 1
                else: max_y += -1
                
    def initialize_edges(self):
        for x in range(len(self.vertex)): 
            for y in range(len(self.vertex[x])):
                self.edges[self.vertex[x][y]] = []
                if (y > 0): self.edges[self.vertex[x][y]] += [self.vertex[x][y - 1]]
                if (y < len(self.vertex[x]) - 1): self.edges[self.vertex[x][y]] += [self.vertex[x][y + 1]]
                if (x > 0): 
                    if (x < self.side_length and y > 0): self.edges[self.vertex[x][y]] += [self.vertex[x - 1][y - 1]]
                    elif (x >= self.side_length): self.edges[self.vertex[x][y]] += [self.vertex[x - 1][y]]
                    
                    if (x < self.side_length and y < len(self.vertex[x]) - 1): self.edges[self.vertex[x][y]] += [self.vertex[x - 1][y]]
                    elif (x >= self.side_length): self.edges[self.vertex[x][y]] += [self.vertex[x - 1][y + 1]]
                if (x < len(self.vertex) - 1):
                    if (x >= self.side_length - 1 and y > 0): self.edges[self.vertex[x][y]] += [self.vertex[x + 1][y - 1]]
                    elif (x < self.side_length - 1): self.edges[self.vertex[x][y]] += [self.vertex[x + 1][y]]
                    
                    if (x >= self.side_length - 1 and y < len(self.vertex[x]) - 1): self.edges[self.vertex[x][y]] += [self.vertex[x + 1][y]]
                    elif (x < self.side_length - 1): self.edges[self.vertex[x][y]] += [self.vertex[x + 1][y + 1]]
        
h = HexagonGraph(7)
g = Graph(h.edges)
path = g.find_all_paths(1, 18)
print(path)

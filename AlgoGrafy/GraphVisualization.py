import networkx as nx
import matplotlib.pyplot as plt
from random import randint
from pomocne import *

def GraphGenerator(n, m, directed=False):
    G = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        while x == y or G[x][y] == 1:
            x = randint(0, n - 1)
            y = randint(0, n - 1)
        G[x][y] = 1
        if not directed:
            G[y][x] = 1
    return G


class GraphVisualization:
    # dataType = 0: adjacency matrix
    # dataType = 1: adjacency list
    def __init__(self, graph=[], dataType=0):
        self.G = nx.Graph()
        n = len(graph)
        for i in range(n):
            if dataType == 0:
                count_edges = 0
                for j in range(n):
                    if graph[i][j] == 1:
                        self.G.add_edge(i, j)
                        count_edges += 1
                if count_edges == 0:
                    self.G.add_node(i)
            elif dataType == 1:
                m = len(graph[i])
                if m == 0:
                    self.G.add_node(i)
                else:
                    for j in range(m):
                        self.G.add_edge(i, graph[i][j])

    def visualize(self):
        nx.draw_networkx(self.G)
        plt.show()


# Test code
if __name__ == "__main__":
    G = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [
            4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]
    G = conv_to_im(G)
    # G = GraphGenerator(7, 4)
    GV = GraphVisualization(G, 0)
    GV.visualize()

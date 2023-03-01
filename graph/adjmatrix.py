from graph import Graph, Node
import numpy as np

class GraphAdjMatrix(Graph):
    def __init__(self, vertex_amount, type="undirected"):
        super().__init__(vertex_amount)
        self.matrix = np.zeros((vertex_amount, vertex_amount))
        self.type = type

    def add_vertex(self, vertex):
        if vertex not in self.vertex:
            self.vertex[vertex-1] = vertex
        else:
            print("!!! Vertex ", vertex," already part of the graph !!!")
    
    def add_edge(self, vertex_1, vertex_2, weight=1):
        if self.matrix[vertex_1-1][vertex_2-1] != weight:
            self.matrix[vertex_1-1][vertex_2-1] = weight
        
        if self.type == "undirected":
            self.matrix[vertex_2-1][vertex_1-1] = weight

    def print_graph(self):
        for i in range(self.vertex_am):
            print(i+1,"\t|", end="\t")
            for j in range(self.vertex_am):
                print(self.matrix[i][j], end="\t")
            print()

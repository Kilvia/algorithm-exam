import numpy as np

class Node:
    def __init__(self, value=None):
        self.next = None
        self.vertex = value

class Graph:
    def __init__(self, vertex_amount):
        self.vertex_am = vertex_amount
        self.vertex = [None] * vertex_amount

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

class GraphAdjList(Graph):
    def __init__(self, vertex_amount):
        super().__init__(vertex_amount)
        self.list = [None] * vertex_amount
    
    def add_vertex(self, vertex):
        if vertex not in self.list:
            self.list[vertex-1] = Node(vertex)
        else:
            print("!!! Vertex ", vertex," already part of the graph !!!")
    
    def add_edge(self, vertex_1, vertex_2, value=1):
        i = 0

        if self.list[vertex_1-1].next == None:
            self.list[vertex_1-1].next = Node(vertex_2)
        else: 
            aux = self.list[vertex_1-1].next
            
            while aux.vertex != vertex_2 and aux.next != None and i < self.vertex_am:
                aux = aux.next
            
            if aux.next == None:
                aux.next = Node(vertex_2)
            else:
                print("!!! Edge ", vertex_1, " ", vertex_2, " already exist !!!")

    def print_graph(self):
        for i in range(self.vertex_am):
            print(self.list[i].vertex, end="")
            aux = self.list[i].next
            while aux != None:
                print("\t->\t", aux.vertex, end="")
                aux = aux.next
            print()

if __name__ == "__main__":
    print("======================================")
    print("Graph Represented by Adjacent Matrix")
    print("--------------------------------------")
    print("Undirected Graph")
    adjm = GraphAdjMatrix(5)
    adjm.add_vertex(1)
    adjm.add_vertex(2)
    adjm.add_vertex(3)
    adjm.add_vertex(4)
    adjm.add_vertex(5)
    adjm.add_edge(1, 2)
    adjm.add_edge(1, 5)
    adjm.add_edge(2, 3)
    adjm.add_edge(2, 4)
    adjm.add_edge(2, 5)
    adjm.add_edge(3, 4)
    adjm.add_edge(4, 5)
    adjm.print_graph()
    print("--------------------------------------")
    print("Directed Graph")
    adjm_d = GraphAdjMatrix(6, "directed")
    adjm_d.add_vertex(1)
    adjm_d.add_vertex(2)
    adjm_d.add_vertex(3)
    adjm_d.add_vertex(4)
    adjm_d.add_vertex(5)
    adjm_d.add_edge(1, 2)
    adjm_d.add_edge(1, 4)
    adjm_d.add_edge(2, 5)
    adjm_d.add_edge(3, 5)
    adjm_d.add_edge(3, 6)
    adjm_d.add_edge(4, 2)
    adjm_d.add_edge(5, 4)
    adjm_d.add_edge(6, 6)
    adjm_d.print_graph()
    print("**************************************")
    print("Graph Represented by Adjacent List")
    print("--------------------------------------")
    print("Undirected Graph")
    adjl = GraphAdjList(5)
    adjl.add_vertex(1)
    adjl.add_vertex(2)
    adjl.add_vertex(3)
    adjl.add_vertex(4)
    adjl.add_vertex(5)
    adjl.add_edge(1, 2)
    adjl.add_edge(1, 5)
    adjl.add_edge(2, 1)
    adjl.add_edge(2, 3)
    adjl.add_edge(2, 4)
    adjl.add_edge(2, 5)
    adjl.add_edge(3, 2)
    adjl.add_edge(3, 4)
    adjl.add_edge(4, 2)
    adjl.add_edge(4, 3)
    adjl.add_edge(4, 5)
    adjl.add_edge(5, 1)
    adjl.add_edge(5, 2)
    adjl.add_edge(5, 4)
    adjl.print_graph()
    print("--------------------------------------")
    print("Directed Graph")
    adjl_d = GraphAdjList(6)
    adjl_d.add_vertex(1)
    adjl_d.add_vertex(2)
    adjl_d.add_vertex(3)
    adjl_d.add_vertex(4)
    adjl_d.add_vertex(5)
    adjl_d.add_vertex(6)
    adjl_d.add_edge(1, 2)
    adjl_d.add_edge(1, 4)
    adjl_d.add_edge(2, 5)
    adjl_d.add_edge(3, 5)
    adjl_d.add_edge(3, 6)
    adjl_d.add_edge(4, 2)
    adjl_d.add_edge(5, 4)
    adjl_d.add_edge(6, 6)
    adjl_d.print_graph()
    print("**************************************")


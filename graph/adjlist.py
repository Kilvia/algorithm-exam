from graph import Graph, Node

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

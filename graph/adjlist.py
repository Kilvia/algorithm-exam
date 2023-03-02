from graph import Graph, Node
from queue import Queue
import math

time = 0

class Vertex(Node):
    def __init__(self, value=None):
        super().__init__(value)
        self.color = None
        self.distance = None
        self.f = None
        self.pred = None

class GraphAdjList(Graph):
    def __init__(self, vertex_am):
        super().__init__(vertex_am)
        self.list = [None] * vertex_am

    def add_vertex(self, vertex):
        if vertex not in self.list:
            self.list[vertex-1] = Vertex(vertex)
        else:
            print("!!! Vertex ", vertex," already part of the graph !!!")
    
    def add_edge(self, vertex_1, vertex_2, value=1):
        i = 0

        if self.list[vertex_1-1].next == None:
            self.list[vertex_1-1].next = Vertex(vertex_2)
        else: 
            aux = self.list[vertex_1-1].next
            
            while aux.vertex != vertex_2 and aux.next != None and i < self.vertex_am:
                aux = aux.next
            
            if aux.next == None:
                aux.next = Vertex(vertex_2)
            else:
                print("!!! Edge ", vertex_1, " ", vertex_2, " already exist !!!")
    
    def bfs(self, node):
        
        print("Distance from vertex ", node.vertex)
        for i in range(self.vertex_am):
            self.list[i].color = "white"
            self.list[i].distance = math.inf
            self.list[i].pred = None
        
        node.color = "gray"
        node.distance = 0 
        node.pred = None

        q = Queue(maxsize=self.vertex_am)
        q.put(node)

        while not(q.empty()):
            
            u = q.get()
            print("Vertex", u.vertex, ":", self.list[u.vertex-1].distance)
            v = u.next
            
            while v != None:
                if self.list[v.vertex-1].color == "white":
            
                    self.list[v.vertex-1].color = "gray"
                    self.list[v.vertex-1].distance = self.list[u.vertex-1].distance + 1
                    self.list[v.vertex-1].pred = u
                    q.put(self.list[v.vertex-1])
                v = v.next

            u.color = "black"

    def dfs_visit(self, node):
        
        global time
        time += 1
        self.list[node.vertex - 1].distance = time
        self.list[node.vertex - 1].color = "gray"
        temp = self.list[node.vertex - 1].next
        print(node.vertex, end=" ")

        while temp != None:
            if self.list[temp.vertex - 1].color == "white":
                self.list[temp.vertex - 1].pred = node
                self.dfs_visit(temp)
            temp = temp.next

        node.color = "black"
        time += 1
        self.list[node.vertex - 1].f = time

    def dfs(self):
        global time
        for i in range(self.vertex_am):
            self.list[i].color = "white"
            self.list[i].pred = None
        
        time = 0

        for i in range(self.vertex_am):
            if self.list[i].color == "white":
                self.dfs_visit(self.list[i])
        print()

    def print_graph(self):
        for i in range(self.vertex_am):
            print(self.list[i].vertex, end="")
            aux = self.list[i].next
            while aux != None:
                print("\t->\t", aux.vertex, end="")
                aux = aux.next
            print()

    def print_path(self, node_s, node_end):
            if node_s == node_end:
                print(node_s.vertex, end=" ")
            elif node_end.pred == None:
                print("No path from vertex", node_s, "to", node_end)
            else:
                self.print_path(node_s, node_end.pred)
                print("->", node_end.vertex, end=" ")
from adjlist import GraphAdjList, Vertex

aux = []

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, node):

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

def dfs_visit(graph, node):
        
    global time
    global aux 

    time += 1
    graph.list[node.vertex - 1].distance = time
    graph.list[node.vertex - 1].color = "gray"
    temp = graph.list[node.vertex - 1].next

    while temp != None:
        if graph.list[temp.vertex - 1].color == "white":
            graph.list[temp.vertex - 1].pred = node
            dfs_visit(graph, temp)
        temp = temp.next

    node.color = "black"
    time += 1
    graph.list[node.vertex - 1].f = time

    print("Vertex to be add ", graph.list[node.vertex - 1].vertex, " start time ", graph.list[node.vertex - 1].distance, " end time ", graph.list[node.vertex - 1].f)
        
    aux.insert(0, graph.list[node.vertex - 1])
    
# Print the nodes time in decreasing order
def dfs(graph):
    
    global time
    global aux
    
    for i in range(graph.vertex_am):
        graph.list[i].color = "white"
        graph.list[i].pred = None
    
    time = 0

    for i in range(graph.vertex_am):
        if graph.list[i].color == "white":
            dfs_visit(graph, graph.list[i])
    return aux

def top_sort(graph):
    
    top = dfs(graph)
        
    return top
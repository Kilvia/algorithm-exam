from adjlist import GraphAdjList, Vertex
from topsort import dfs
from copy import deepcopy


def transpose(graph):
    transp = GraphAdjList(graph.vertex_am)

    for i in range(graph.vertex_am):
        transp.list[i] = deepcopy(graph.list[i])
        transp.list[graph.list[i].vertex-1].next = None
    
    original_list = deepcopy(transp.list)

    for i in range(graph.vertex_am):
        temp = deepcopy(graph.list[i].next)
        while temp: 
            if transp.list[temp.vertex-1].next == None:
                transp.list[temp.vertex-1].next = original_list[i]
            else:
                aux = deepcopy(original_list[i])
                aux.next = transp.list[temp.vertex-1].next
                transp.list[temp.vertex-1].next = aux
            
            temp = temp.next

    return transp

def conn(graph):
    print("DFS: ", end=" ")
    graph.dfs()
    print()
    transp = transpose(graph)
    transp.print_graph()
       
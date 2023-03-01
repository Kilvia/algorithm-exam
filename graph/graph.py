class Node:
    def __init__(self, value=None):
        self.next = None
        self.vertex = value

class Graph:
    def __init__(self, vertex_amount):
        self.vertex_am = vertex_amount
        self.vertex = [None] * vertex_amount

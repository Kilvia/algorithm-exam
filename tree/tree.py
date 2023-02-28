class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key

def print_node(node, level=0):
    if node != None:
        print_node(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.key))
        print_node(node.right, level + 1)


class Tree():
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            aux = self.root
            node_aux = None
            while aux != None:
                node_aux = aux
                if key < aux.key:
                    aux = self.root.right
                else: aux = self.root.left
            
            if key < node_aux.key:
                node_aux.right = Node(key)
                node_aux.right.parent = node_aux
            else: 
                node_aux.left = Node(key)
                node_aux.left.parent = node_aux

    def print_tree(self):
        print_node(self.root)
            

if __name__ == "__main__":
    tree = Tree()  
    tree.insert(12)
    tree.insert(18)
    tree.insert(5)
    tree.print_tree()
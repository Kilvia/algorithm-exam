class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key

def print_node(node, level=0):
    if node != None:
        print_node(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.key))
        print_node(node.left, level + 1)


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
                    aux = aux.left
                else: aux = aux.right
            
            if key < node_aux.key:
                node_aux.left = Node(key)
                node_aux.left.parent = node_aux
            else: 
                node_aux.right = Node(key)
                node_aux.right.parent = node_aux

    def search_rec(self, node, key):
        if node == None or node.key == key:
            return node
        
        if key < node.key:
            return self.search_rec(node.left, key)
        else:
            return self.search_rec(node.right, key)
    
    def search_ite(self, key):
        node = self.root
        while node != None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
                
        return node
    
    def minimum(self):
        aux = self.root
        
        while aux.left != None:
            aux = aux.left
        
        return aux
    
    def maximum(self):
        aux = self.root

        while aux.right != None:
            aux = aux.right

        return aux
    
    def successor(self, node):
        if node.right != None:
            return self.minimum(node.right)
        
        y = node.parent
        while y != None and node == y.right:
            node = y
            y = y.parent
        return y

    def predecessor(self, node):
        if node.left != None:
            return self.maximum(node.left)
        
        y = node.parent
        while y != None and node == y.left:
            node = y
            y = y.parent
        return y


    def print_tree(self):
        print_node(self.root)
            

if __name__ == "__main__":
    tree = Tree()  
    tree.insert(15)
    tree.insert(6)
    tree.insert(18)
    tree.insert(3)
    tree.insert(7)
    tree.insert(17)
    tree.insert(20)
    tree.insert(2)
    tree.insert(4)
    tree.insert(13)
    tree.insert(9)
    tree.print_tree()
    print("---------------------------------")
    min = tree.minimum()
    max = tree.maximum()
    print("Minimum element: ", min.key)
    print("Maximum element: ", max.key)
    print("---------------------------------")
    search_node_i = tree.search_ite(9)
    search_node_r = tree.search_rec(tree.root, 9)
    print("Element found through iterative function: ", search_node_i)
    print("Element found through recurrent function: ", search_node_r)
    print("---------------------------------")
    pred = tree.search_ite(7)
    succ = tree.search_ite(13)
    pred_asw = tree.predecessor(pred)
    succ_asw = tree.successor(succ)
    print("Predecessor of number ", pred.key,": ", pred_asw.key)
    print("Successor of number ", succ.key,": ", succ_asw.key)

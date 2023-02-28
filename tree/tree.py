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

    def transplant(self, node_sub, node):
        if node.parent == None:
            self.root = node_sub
        elif node == node.parent.left:
            node.parent.left = node_sub
        else: node.parent.right = node_sub

        if node_sub != None:
            node_sub.parent = node.parent

    def delete(self, node):
        if node.left == None:
            self.transplant(node.right, node)
        elif node.right == None:
            self.transplant(node.left, node)
        else:
            y = self.minimum(node.right)
            if y.parent != node:
                self.transplant(y.right, y)
                y.right = node.right
                y.right.parent = y
            self.transplant(y, node)
            y.left = node.left
            y.left.p = y      

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
    
    def minimum(self, node):
        while node.left != None:
            node = node.left
        
        return node
    
    def maximum(self, node):
        while node.right != None:
            node = node.right

        return node
    
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
    
def print_inoder(root):
    if root:
        print_inoder(root.left)
        print(root.key, end=" ")
        print_inoder(root.right)

def print_preoder(root):
    if root:
        print(root.key, end=" ")
        print_preoder(root.left)
        print_preoder(root.right)

def print_postoder(root):
    if root:
        print_postoder(root.left)
        print_postoder(root.right)
        print(root.key, end=" ")

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
    min = tree.minimum(tree.root)
    max = tree.maximum(tree.root)
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
    print("---------------------------------")
    tree_1 = Tree()  
    tree_1.insert(25)
    tree_1.insert(15)
    tree_1.insert(50)
    tree_1.insert(10)
    tree_1.insert(22)
    tree_1.insert(35)
    tree_1.insert(70)
    tree_1.insert(4)
    tree_1.insert(12)
    tree_1.insert(18)
    tree_1.insert(24)
    tree_1.insert(31)
    tree_1.insert(44)
    tree_1.insert(66)
    tree_1.insert(90)
    tree_1.print_tree()
    print("---------------------------------")
    print("Print the tree in inoder: ", end=" ")
    print_inoder(tree_1.root)
    print("\nPrint the tree in preoder: ", end=" ")
    print_preoder(tree_1.root)
    print("\nPrint the tree in postoder: ", end=" ")
    print_postoder(tree_1.root)
    print("---------------------------------")
    dele = tree.search_ite(15)
    tree.delete(dele)
    tree.print_tree()


from copy import deepcopy
import math

class DirectAddresTable:
    def __init__(self, size):
        self.table = [None] * size
    
    def direct_add_search(self, key):
        return self.table[key]

    def direct_add_insert(self, key, value):
        self.table[key] = value
    
    def direct_add_delete(self, key):
        self.table[key] = None
    
    def find_max(self):
        # return the maximum element
        aux = 0
        for i in range(len(self.table)):
            if self.table[i] != None and aux < self.table[i]:
                aux = self.table[i]
        return aux
    
    def find_min(self):
        # return the minimum element
        aux = math.inf
        for i in range(len(self.table)):
            if self.table[i] != None and aux > self.table[i]:
                aux = self.table[i]
        return aux  

# Basic hash without treating collisions 
class Hash():
    def __init__(self, size):
        self.table = [None] * size
        self.size = size

    def division(self, key):
        return (key % self.size)
    
    # Insert through open addressing
    def insert(self, key):
        h = self.division(key)
        self.table[h] = key
        
        return h
    
    def delete(self, key):
        h = self.division(key)

        if self.table[h] == key:
            self.table[h] = "Deleted"


    def search(self, key):
        h = self.division(key)

        if self.table[h] == key:
            return h

        return None
    
    def print_hash(self):
        for i in range(self.size):
            print(i, "\t|\t", self.table[i])

# Hash treating collisions with open addressing
class HashOpenAddressing(Hash):
    def __init__(self, size, probe_type):
        super().__init__(size)
        self.probe = probe_type

    def linear(self, h, i):
        return ((h + i) % self.size)
    
    def quadratic(self, h, c_1, c_2, i):
        return ((h + (c_1 * i) + (pow(i,2) * c_2)) % self.size)
    
    def double(self, h, h_2, i):
        return((h + (i * h_2)) % self.size)
    
    # Insert through open addressing
    def insert(self, key):
        h = self.division(key)
        i = 1
        h_aux = h

        while self.table[h_aux] != None and self.table[h_aux] != "Deleted" and i <= self.size:
            # Check for an empty position
            if self.probe == "linear":
                h_aux = self.linear(h, i)
            elif self.probe == "quadratic":
                c_1 = 1
                c_2 = 3
                h_aux = self.quadratic(h, c_1, c_2, i)
            else:
                h_2 = 1 + (key % (self.size - 1))
                h_aux = self.double(h, h_2, i)
            
            i += 1
        
        h = h_aux
        
        # Check the position and add the key
        if h != None:
            self.table[h] = key
            return h
        else:
            print("Cant insert element. Hash table full")
    
    def delete(self, key):
        h = self.division(key)
        h_aux = h
        i = 1

        while self.table[h_aux] != key and i <= self.size:
            if self.probe == "linear":
                h_aux = self.linear(h, i)
            elif self.probe == "quadratic":
                c_1 = 1
                c_2 = 3
                h_aux = self.quadratic(h, c_1, c_2, i)
            else:
                h_2 = 1 + (key % (self.size - 1))
                h_aux = self.double(h, h_2, i)
            i += 1

        if self.table[h_aux] == key:
            self.table[h_aux] = "Deleted"


    def search(self, key):
        h = self.division(key)

        if self.table[h] == key:
            return h
        elif self.table[h] == None:
            return None
        else:
            h_aux = h
            i = 1
            while self.table[h_aux] != None and i <= self.size:
                if self.probe == "linear":
                    h_aux = self.linear(h, i)
                elif self.probe == "quadratic":
                    c_1 = 1
                    c_2 = 3
                    h_aux = self.quadratic(h, c_1, c_2, i)
                else:
                    h_2 = 1 + (key % (self.size - 1))
                    h_aux = self.double(h, h_2, i)

                if self.table[h_aux] == key: 
                    return h_aux
                
                i += 1

        return None
                
class Node:
    def __init__(self, key=None):
        self.prev = None
        self.next = None
        self.key = key

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, key):
        node = Node(key)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def delete(self, key):
        
        if self.head == None:
            print("Key doesnt exist")
            return 0
            
        temp = self.head
        
        if temp.key == key:
            self.head = temp.next
        else:
            while temp.key != key and temp.next != None:
                temp = temp.next
            
            if temp.key != key:
                print("Key doesnt exist")
            else:
                temp.prev.next = temp.next
                if temp.next != None:
                    temp.next.prev = temp.prev

    def search(self, key):
        if self.head == None:
            return None
        else:
            temp = self.head
            
            while temp.key != key and temp.next != None:
                temp = temp.next
            
            if temp.key == key:
                return key
        return None
            

    def traverse(self, i):
        temp = self.head
        s = str(i) + "\t| "
        if temp == None:
            s += str(None)
        while temp:
            s += str(temp.key) + "\t"
            temp = temp.next

        print(s)

class HashChaining(Hash):
    def __init__(self, size):
       super().__init__(size)
       for i in range(size):
           self.table[i] = LinkedList()
    
    def insert(self, key):
        h = self.division(key)
        self.table[h].insert(key)
    
    def delete(self, key):
        h = self.division(key)
        self.table[h].delete(key)

    def search(self, key):
        h = self.division(key)
        aux = self.table[h].search(key)
        if aux != None:
            return h 
        else: return None

    def print_hash(self):
        for i in range(self.size):
            self.table[i].traverse(i)

if __name__ == '__main__':
    #### Direct Address ####
    # dat = DirectAddresTable(6)
    # dat.direct_add_insert(0, 4)
    # dat.direct_add_insert(1, 6)
    # dat.direct_add_insert(2, 3)
    # dat.direct_add_insert(3, 8)
    # dat.direct_add_delete(2)
    # print(dat.find_min())

    #### Basical Hash ####
    print("\n\tHash")
    print("\nIndex\t|\tKey")
    hash = Hash(11)
    hash.insert(10)
    hash.insert(22)
    hash.insert(31)
    hash.insert(4)
    hash.insert(15)
    hash.insert(28)
    hash.insert(17)
    hash.insert(88)
    hash.insert(59)
    hash.delete(88)
    hash.print_hash()
    print("------------------------------------------")

    #### Hash Open Addressing ####
    print("\n\tLinear")
    print("\nIndex\t|\tKey")
    hash_l = HashOpenAddressing(11, "linear")
    hash_l.insert(10)
    hash_l.insert(22)
    hash_l.insert(31)
    hash_l.insert(4)
    hash_l.insert(15)
    hash_l.insert(28)
    hash_l.insert(17)
    hash_l.insert(88)
    hash_l.insert(59)
    hash_l.delete(4)
    hash_l.print_hash()
    print("------------------------------------------")

    print("\n\tQuadratic")
    print("\nIndex\t|\tKey")
    hash_q = HashOpenAddressing(11, "quadratic")
    hash_q.insert(10)
    hash_q.insert(22)
    hash_q.insert(31)
    hash_q.insert(4)
    hash_q.insert(15)
    hash_q.insert(28)
    hash_q.insert(17)
    hash_q.insert(88)
    hash_q.insert(59)
    hash_q.print_hash()
    print("------------------------------------------")

    print("\n\tDouble")
    print("\nIndex\t|\tKey")
    hash_d = HashOpenAddressing(11,"double")
    hash_d.insert(10)
    hash_d.insert(22)
    hash_d.insert(31)
    hash_d.insert(4)
    hash_d.insert(15)
    hash_d.insert(28)
    hash_d.insert(17)
    hash_d.insert(88)
    hash_d.insert(59)
    hash_d.print_hash()
    print("------------------------------------------")

    #### Hash Chaining ####
    print("\n\tHash Chaining")
    print("\nIndex\t|\tKeys")
    hash_c = HashChaining(11)
    # hash_c.print_hash()
    hash_c.insert(10)
    hash_c.insert(22)
    hash_c.insert(31)
    hash_c.insert(4)
    hash_c.insert(15)
    hash_c.insert(28)
    hash_c.insert(17)
    hash_c.insert(88)
    hash_c.insert(59)
    hash_c.delete(15)
    hash_c.print_hash()
    print("------------------------------------------")

    print("\nSearch index\n")
    search = 59

    ind = hash.search(search)
    print("Key ", search, ": ", ind)

    ind = hash_l.search(search)
    print("Key ", search, ": ", ind)

    ind = hash_q.search(search)
    print("Key ", search, ": ", ind)

    ind = hash_d.search(search)
    print("Key ", search, ": ", ind)

    ind = hash_c.search(search)
    print("Key ", search, ": ", ind)
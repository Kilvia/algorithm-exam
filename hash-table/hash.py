
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

class Hash:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size
    
    def division(self, key):
        return (key % self.size)

    def linear(self, h):
        i = 1
        h_1 = (h + i) % self.size

        while self.table[h_1] != None:
            i += 1
            h_1 = (h + i) % self.size
        
        return h_1
    
    def quadratic(self, h, c_1, c_2):
        i = 1
        h_1 = (h + (c_1 * i) + (pow(i,2) * c_2)) % self.size

        while self.table[h_1] != None:
            i += 1
            h_1 = (h + (c_1 * i) + (pow(i,2) * c_2)) % self.size
        
        return h_1

    def double(self, h, h_2):
        i = 1
        h_1 = (h + (i * h_2)) % self.size
        
        while self.table[h_1] != None:
            i += 1
            h_1 = (h + (i * h_2)) % self.size
        
        return h_1
    
    def insert(self, key, probe_type):
        h = self.division(key)

        if self.table[h] == None:
            self.table[h] = key
        else:
            if probe_type == "linear":
                h = self.linear(h)
            elif probe_type == "quadratic":
                c_1 = 1
                c_2 = 3
                h = self.quadratic(h, c_1, c_2)
            else:
                h_2 = 1 + (key % (self.size - 1))
                h = self.double(h, h_2)
            
            self.table[h] = key
    
    def print_hash(self):
        for i in range(self.size):
            print(self.table[i])
                



if __name__ == '__main__':
    # dat = DirectAddresTable(6)
    # dat.direct_add_insert(0, 4)
    # dat.direct_add_insert(1, 6)
    # dat.direct_add_insert(2, 3)
    # dat.direct_add_insert(3, 8)
    # dat.direct_add_delete(2)
    # print(dat.find_min())

    print("\nLinear")
    hash = Hash(11)
    hash.insert(10, "linear")
    hash.insert(22, "linear")
    hash.insert(31, "linear")
    hash.insert(4, "linear")
    hash.insert(15, "linear")
    hash.insert(28, "linear")
    hash.insert(17, "linear")
    hash.insert(88, "linear")
    hash.insert(59, "linear")
    hash.print_hash()
    print("------------------------------------------")

    print("\nQuadratic")
    hash_q = Hash(11)
    hash_q.insert(10, "quadratic")
    hash_q.insert(22, "quadratic")
    hash_q.insert(31, "quadratic")
    hash_q.insert(4, "quadratic")
    hash_q.insert(15, "quadratic")
    hash_q.insert(28, "quadratic")
    hash_q.insert(17, "quadratic")
    hash_q.insert(88, "quadratic")
    hash_q.insert(59, "quadratic")
    hash_q.print_hash()
    print("------------------------------------------")

    print("\nDouble")
    hash_d = Hash(11)
    hash_d.insert(10, "double")
    hash_d.insert(22, "double")
    hash_d.insert(31, "double")
    hash_d.insert(4, "double")
    hash_d.insert(15, "double")
    hash_d.insert(28, "double")
    hash_d.insert(17, "double")
    hash_d.insert(88, "double")
    hash_d.insert(59, "double")
    hash_d.print_hash()
    print("------------------------------------------")
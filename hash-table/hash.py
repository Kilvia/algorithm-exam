
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
    def __init__(self, size, probe_type):
        self.table = [None] * size
        self.size = size
        self.probe = probe_type
    
    def division(self, key):
        return (key % self.size)

    def linear(self, h, i):
        return ((h + i) % self.size)
    
    def quadratic(self, h, c_1, c_2, i):
        return ((h + (c_1 * i) + (pow(i,2) * c_2)) % self.size)
    
    def double(self, h, h_2, i):
        return((h + (i * h_2)) % self.size)
    
    def insert(self, key):
        h = self.division(key)
        i = 1
        h_aux = h

        while self.table[h_aux] != None and i <= self.size:
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
        else:
            print("Cant insert element. Hash table full")

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
    
    def print_hash(self):
        for i in range(self.size):
            print(i, "\t|\t", self.table[i])
                



if __name__ == '__main__':
    # dat = DirectAddresTable(6)
    # dat.direct_add_insert(0, 4)
    # dat.direct_add_insert(1, 6)
    # dat.direct_add_insert(2, 3)
    # dat.direct_add_insert(3, 8)
    # dat.direct_add_delete(2)
    # print(dat.find_min())

    print("\n\tLinear")
    print("\nIndex\t|\tKey")
    hash = Hash(11, "linear")
    hash.insert(10)
    hash.insert(22)
    hash.insert(31)
    hash.insert(4)
    hash.insert(15)
    hash.insert(28)
    hash.insert(17)
    hash.insert(88)
    hash.insert(59)
    hash.print_hash()
    print("------------------------------------------")

    print("\n\tQuadratic")
    print("\nIndex\t|\tKey")
    hash_q = Hash(11, "quadratic")
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
    hash_d = Hash(11,"double")
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

    print("\nSearch index\n")
    search = 59

    ind = hash.search(search)
    print("Key ", search, ": ", ind)

    ind = hash_q.search(search)
    print("Key ", search, ": ", ind)

    ind = hash_d.search(search)
    print("Key ", search, ": ", ind)
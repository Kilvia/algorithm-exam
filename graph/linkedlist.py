class Element():
    def __init__(self, key):
        self.key = key
        self.head = None
        self.tail = None
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, key):
        x = Element(key)
        self.size += 1

        if self.head == None:
            self.head = x
            self.tail = x
        else:
            x.head = self.head
            self.tail.next, self.tail = x, x

    def search(self, elem):
        temp = self.head
        
        while temp:
            if temp.key == elem:
                return temp
            
            temp = temp.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.key, end=" ")
            temp = temp.next
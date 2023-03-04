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
    
    def add(self, key):
        x = Element(key)

        if self.head == None:
            self.head = x
            self.tail = x
        else:
            x.head = self.head
            self.tail.next, self.tail = x, x

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.key)
            temp = temp.next
        

x = LinkedList()
x.add("f")  
x.add("g")      
x.add("d")  
x.print_list()
from linkedlist import LinkedList, Element

# For this linked list each elements points to the 
# head and the last one points to the tail too
def find_set_linked_list(element):
    return element.head

def find_set_forest(x):
    if x != x.p:
        x.p = find_set_forest(x.p)
    return x.p

def make_set_linked_list(element):
    set = LinkedList()
    set.add(element)
    return set

def make_set_forest(x):
    x.p = x
    x.rank = 0

def union_linked_list(elem_1, elem_2):
    union = LinkedList()
    temp = None

    union.size = elem_1.size + elem_2.size

    if elem_1.size >= elem_2.size:
        union.head = elem_1.head
        elem_1.tail.next = elem_2.head
        temp = elem_2.head
        elem_1.tail = elem_2.tail
        union.tail = elem_2.tail
    else:
        union.head = elem_2.head
        elem_2.tail.next = elem_1.head
        temp = elem_1.head
        elem_2.tail = elem_1.tail
        union.tail = elem_1.tail

    while temp:
        temp.head = union.head
        temp = temp.next

    elem_1.tail = elem_2.tail
    union.tail = elem_2.tail

    return union

def link_forest(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank = y.rank + 1

def union_forest(x, y):
    link_forest(find_set_forest(x), find_set_forest(y))
    
x = LinkedList()
x.add("f")  
x.add("g")      
x.add("d")  
x.print_list()
print()
elem = x.search("g")
elem_1 = x.search("f")
elem_2 = x.search("d")
res = find_set_linked_list(elem)
set_1 = make_set_linked_list(elem.key)
set_2 = make_set_linked_list(elem_1.key)
set_3 = make_set_linked_list(elem_2.key)
union = union_linked_list(set_1, set_2)
union = union_linked_list(union, set_3)
union.print_list()

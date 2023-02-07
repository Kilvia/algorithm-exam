def max_heapify(A, i):
    
    l = (2*i)+1
    r = (2*i)+2
    
    largest = l if l < len(A) and A[l] > A[i] else i
    if r < len(A) and A[r] > A[largest]: largest = r 
    if largest != i: 
        aux = A[largest]
        A[largest] = A[i]
        A[i] = aux
        max_heapify(A, largest)

def min_heapify(A, i):
    
    l = (2*i)+1
    r = (2*i)+2

    smalest = l if l < len(A) and A[l] < A[i] else i
    if r < len(A) and A[r] < A[smalest]: smalest = r
    if smalest != i:
        aux = A[smalest]
        A[smalest] = A[i]
        A[i] = aux
        min_heapify(A, smalest)

def build_max_heap(A):
    
    j = (int)(len(A)/2 -1)

    for i in range(j, -1, -1):
        max_heapify(A, i)

def build_min_heap(A):
    
    j = (int)((len(A)/2)-1)

    for i in range(j, -1, -1):
        min_heapify(A, i)

def max_heapsort(A):
    
    build_max_heap(A)
    heap = [0]*(len(A))
    
    for i in range(len(A)-1,0,-1):
        heap[i] = A[0]
        A[0] = A[i]
        A.pop(i)
        max_heapify(A, 0)
    
    heap[0] = A[0]
    
    return heap

def min_heapsort(A):

    build_min_heap(A)
    heap = [0]*(len(A))
    for i in range(len(A)-1,0,-1):
        heap[i] = A[0]
        A[0] = A[i]
        A.pop(i)
        min_heapify(A, 0)
    
    heap[0] = A[0]
    
    return heap

def heap_maximum(A):
    return A[0]

def heap_minimum(A):
    return A[0]

def heap_extract_max(A):

    if len(A) < 0:
        IndexError 
    
    max = A[0]
    A[0] = A[len(A)-1]
    A.pop(len(A)-1)
    
    max_heapify(A,0)
    
    return max

def heap_extract_min(A):
    
    if len(A) < 0:
        IndexError 

    min = A[0]
    A[0] = A[len(A)-1]
    A.pop(len(A)-1)

    min_heapify(A,0)
    
    return min

def increase_key(A, i, key):
    
    if key < A[i-1]:
        ValueError
    
    A[i-1] = key
    # parent index
    ind = int((i/2)-1)

    while i > 0 and A[ind] < A[i-1]:
        
        aux = A[i-1]
        A[i-1] = A[ind]
        A[ind] = aux
        
        i = ind + 1
        ind = (int)((i/2)-1)

def decrease_key(A, i, key):
    
    if key > A[i-1]:
        ValueError
    
    A[i-1] = key
    # parent index
    ind = int((i/2)-1)

    while i > 0 and A[ind] > A[i-1]:
        
        aux = A[i-1]
        A[i-1] = A[ind]
        A[ind] = aux
        
        i = ind + 1
        ind = (int)((i/2)-1)

def max_insert(A, key):
    A.append(float('-inf'))
    increase_key(A, len(A), key)

def min_insert(A, key):
    A.append(float('inf'))
    decrease_key(A, len(A), key)

if __name__ == "__main__":
    # A = [16, 14, 10, 8, 7, 9, 3]
    A = [9, 8, 7, 6, 5, 4, 3]
    A_min = [16, 14, 10, 8, 7, 9, 3]
  
    # build_min_heap(A_min)
    # build_max_heap(A)
    # print(A, A_min)
    
    # minimum = heap_minimum(A_min)
    # maximum = heap_maximum(A)
    # print(maximum, minimum)

    # max_key = heap_extract_max(A)
    # min_key = heap_extract_min(A_min)
    # print(max_key, A, min_key, A_min)
    
    # increase_key(A, 5, 50)
    # decrease_key(A_min, 5, 2)
    # print(A, A_min)

    # max_insert(A, 10)
    # min_insert(A_min,1)
    # print(A, A_min)

    # heap_max = max_heapsort(A)
    # heap_min = min_heapsort(A_min)
    # print(heap_max, heap_min)
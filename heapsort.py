
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

def heapsort():
    return 0

if __name__ == "__main__":
    A = [16, 4, 10, 8, 7, 9, 3, 16, 1]
    # max_heapify(A, 1)
    # min_heapify(A, 2)
    print(A)
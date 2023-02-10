import random


def partition(A, p, r):
    i = p - 2
    key = A[r-1] 

    for j in range(p-1, r-1):
        if A[j] <= key:
            A[i+1], A[j] = A[j], A[i+1]
            i += 1
    A[r-1], A[i+1] = A[i+1], A[r-1]

    return i+2

# Modify the partition for when all the elements have the same size
def partition_mod(A, p, r):
    i = p - 2
    key = A[r-1]
    repition = 0 

    for j in range(p-1, r-1):
        
        if A[j] <= key:
            if A[j] == key:
                repition += 1

            A[i+1], A[j] = A[j], A[i+1]
            i += 1
    
    A[r-1], A[i+1] = A[i+1], A[r-1]
    
    if repition == r-p:
        return (int)((p+r)/2)
    else:
        return (i+2)

def random_partition(A, p, r):
    i = random.randint(p-1, r-1) 
    A[r-1], A[i] = A[i], A[r-1]   

    return partition(A, p, r)   

def quicksort(A, p, r):
    if p < r:
        # # q = partition(A, p, r)
        # q = partition_mod(A, p, r)
        q = random_partition(A, p, r)

        # since A[q] is already in the right position call quick sort again for it left and right side elements
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

if __name__ == '__main__':
    # A = [2,8,7,1,3,5,6,4]
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    # A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    quicksort(A, 1, 12)
    print(A)
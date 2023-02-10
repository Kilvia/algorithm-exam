import math

def merge(a, p, q, r):
    l_array = [0] * (q - p + 2)
    r_array = [0] * (r - q + 1)
    infinity = math.inf

    index = 0
    for i in range(p-1, q):
        l_array[index] = a[i]
        index += 1

    l_array[index] = infinity
    
    index = 0
    for i in range(q, r):
        r_array[index] = a[i]
        index += 1
    
    r_array[index] = infinity

    i = 0
    j = 0

    for k in range(p-1, r):
        if l_array[i] < r_array[j]:
            a[k] = l_array[i]
            i += 1
        else: 
            a[k] = r_array[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)


if __name__ == "__main__":
    a = [2, 4, 5, 7, 1, 2, 3, 6]
    # Index from 1 - 8
    merge_sort(a, 1, 8)
    print(a)
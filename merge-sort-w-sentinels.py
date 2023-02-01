import math

def merge(a, p, q, r):
    l_array = [0] * (q - p + 1)
    r_array = [0] * (r - q)
    infinity = math.inf ### Sentinel

    index = 0
    for i in range(p-1, q):
        l_array[index] = a[i]
        index += 1
    
    index = 0
    for i in range(q, r):
        r_array[index] = a[i]
        index += 1

    i = 0
    j = 0
    n_i = q - p + 1
    n_j = r - q

    for k in range(p-1, r):
        if i >= n_i:
            a[k] = r_array[j]
            j += 1
        
        elif j >= n_j:
            a[k] = l_array[i]
            i += 1

        elif l_array[i] < r_array[j]:
            a[k] = l_array[i]
            i += 1

        else: 
            a[k] = r_array[j]
            j += 1


if __name__ == "__main__":
    a = [2, 4, 5, 7, 8, 1, 3, 8, 9, 10]
    # Index from 1 - 8
    merge(a, 1, 5, 10)
    print(a)
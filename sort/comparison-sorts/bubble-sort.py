def bubble_sort(A):
    for i in range(1, len(A)):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

if __name__ == '__main__':
    A = [2, 8, 5, 3, 9, 4, 1]
    bubble_sort(A)
    print(A)
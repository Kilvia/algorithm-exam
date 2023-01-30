# Input: a sequence of n numbers and a value v
# Output: an index i such that v = A[i] or the special value NIL if v does not appear in A

# Needs to be O(n)

def search(a, v):
    i = 0
    index = None

    for i in range(len(a)):
        if a[i] == v:
            return i

    return index


if __name__ == '__main__':
    a = [1, 2, 6, 8, 12, 9, 10]
    print(search(a, 8))
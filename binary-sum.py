# Input: two n-bit binaryintegers, stored in to n-elements array
# Output: the sum of the two binaries stored in an array of n+1-elements

def binSum(a, b):
    j = len(a)
    carry = 0
    c = [0] * (j+1)

    for i in range(len(a)-1, -1, -1):
        c[j] = (a[i] + b[i] + int(carry)) % 2
        carry = (a[i] + b[i] + int(carry)) / 2
        j -= 1

    c[j] = int(carry)

    return c

if __name__ == '__main__':
    
    a = [1, 1]
    b = [1, 1]

    c = binSum(a, b)
    print(c)
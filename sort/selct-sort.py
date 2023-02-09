# Sort the array selecting the smalest values

# For the worst and best case the time complexity is the same n^2

def sort(a):
    for i in range(len(a)-2):
        index = i
        for j in range(i+1, len(a)):
            if a[index] > a[j]:
                index = j

        a[index], a[i] = a[i], a[index]

if __name__ == "__main__":
    a = [5, 10, 1, 6, 8, 2]
    sort(a)
    print(a)
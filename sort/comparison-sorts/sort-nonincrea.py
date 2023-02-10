# Input: a sequence of n numbers
# Output: a reordering of the input sequences in a non increasing order

def sort(seq):
    for i in range(1, len(seq), 1):
        key = seq[i]
        j = i - 1
        while j >= 0 and seq[j] < key:
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = key
            


if __name__ == '__main__':
    cards = [10, 6, 1, 8, 2, 4]
    sort(cards)
    print(cards)
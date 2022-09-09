import sys

wordList = []
'''
for line in sys.stdin:
    wordList.append(line.replace("\n", "").lower())
'''
def partition(low, high, arr):
    pivot, part = ord(arr[high[0]]), low
    for j in range(low, high):
        if ord(arr[j[0]]) <= pivot:
            arr[j], arr[part] = arr[part], arr[j]
            part += 1
    arr[part], arr[high] = arr[high], arr[part]
    return part

def quicksort(low, high, arr):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(low, high, arr)
        quicksort(low, pi - 1, arr)
        quicksort(pi + 1, high, arr)
    return arr

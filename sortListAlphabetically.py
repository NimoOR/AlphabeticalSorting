#!/usr/bin/env python3

import sys
sys.setrecursionlimit(1500)

words = sys.stdin.read()
wordsList = words.split("\n")
wordsList.pop()

def partition(low, high, arr):
    pivot, part = arr[high].lower(), low - 1
    for j in range(low, high):
        if arr[j].lower() < pivot:
            part += 1
            arr[j], arr[part] = arr[part], arr[j]
    arr[part + 1], arr[high] = arr[high], arr[part + 1]
    return part + 1

def quicksort(low, high, arr):
<<<<<<< HEAD
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(low, high, arr)
        quicksort(low, pi - 1, arr)
        quicksort(pi + 1, high, arr)    
    return arr

final = quicksort(0, len(wordsList) - 1, wordsList)
for index in range(len(wordsList) - 1):
    sys.stdout.write(final[index] + "\n")    
=======
>>>>>>> deba7a270af0a5f8354c4ed96d57986099310a0d
    if low < high:
        pi = partition(low, high, arr)
        quicksort(low, pi - 1, arr)
        quicksort(pi + 1, high, arr)
    final = ""
    for index in range(len(arr) - 1):
        final = final + "\n" + arr[index]
    return final

<<<<<<< HEAD
print(quicksort(0, len(wordsList) - 1, wordsList))
=======
sortedWords = quicksort(0, len(wordsList) - 1, wordsList)
>>>>>>> deba7a270af0a5f8354c4ed96d57986099310a0d

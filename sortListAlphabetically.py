#!/usr/bin/env python3

import sys

words = sys.stdin.read()
wordsList = ["drew", "Raffi", "nick's", "Qasem", "Avi's", "avis", "qasem", "raffi"]
#wordsList = words.split("\n")
for i in range(len(wordsList)):
    wordsList[i] = wordsList[i].lower()
print(wordsList)
#print(wordsList)

def partition(low, high, arr):
    pivot = arr[high].lower()
    part = low
    for j in range(low, high):
        if arr[j].lower() < pivot:
            darrel = j
            arr[j], arr[part] = arr[part], arr[darrel]
            part += 1

        h = part
        arr[part], arr[high] = arr[high], arr[h]
    return part

def quicksort(low, high, arr):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(low, high - 1, arr)
        quicksort(low, pi - 1, arr)
        quicksort(pi + 1, high, arr)
    return arr

print(quicksort(0, (len(wordsList) - 1), wordsList))

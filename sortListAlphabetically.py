#!/usr/bin/env python3

import sys
sys.setrecursionlimit(1500)

words = sys.stdin.read()
wordsList = words.split("\n")
#print(wordsList)
wordsList.pop()
def partition(low, high, arr):
    pivot = arr[high].lower()
    part = low - 1
    for j in range(low, high):
        if arr[j].lower() < pivot:
            part += 1
            arr[j], arr[part] = arr[part], arr[j]
    arr[part + 1], arr[high] = arr[high], arr[part + 1]
    return part + 1

def quicksort(low, high, arr):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(low, high, arr)
        quicksort(low, pi - 1, arr)
        quicksort(pi + 1, high, arr)    
    return arr
final = quicksort(0, len(wordsList) - 1, wordsList)
for index in range(len(wordsList) - 1):
    print(final[index])
    

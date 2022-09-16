#!/usr/bin/env python3

import sys

words = sys.stdin.read()
wordsList = []

wordsList = words.split("\n")
'''print(words)'''
print(wordsList)

def partition(low, high, arr):
    pivot, part = ord(arr[high][0].lower()), low
    for j in range(low, high):
        if ord(arr[j][0].lower()) < pivot:
            arr[j], arr[part] = arr[part], arr[j]
            part += 1
        if ord(arr[j][0].lower()) == pivot:
            char = 0
            while ord(arr[j][char].lower()) == ord(arr[high][char]):
                char += 1
            if ord(arr[j][char].lower()) < ord(arr[high][char]):
                arr[j], arr[part] = arr[part], arr[j]
                part += 1
    arr[part], arr[high] = arr[high], arr[part]
    return part

def quicksort(low, high, arr):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(low, high - 1, arr)
        quicksort(low, pi - 1, arr)
        quicksort(pi + 1, high, arr)
    return arr

for index in range(len(wordsList) - 1):
    print(quicksort(0, len(wordsList) - 1, wordsList)[index])

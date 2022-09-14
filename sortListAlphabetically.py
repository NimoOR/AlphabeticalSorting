#!/usr/bin/env python3

import sys

wordsList = []

words = open(r"test.txt","r")

for line in words:
    wordsList.append(line)

wordsList = [x[:-1] for x in wordsList]

print(wordsList) 

def partition(low, high, arr):
    pivot, part = ord(arr[high][0]), low
    for j in range(low, high):
        if ord(arr[j][0]) <= pivot:
            arr[j], arr[part] = arr[part], arr[j]
            part += 1
    arr[part], arr[high] = arr[high], arr[part]
    return part

def quicksort(low, high, arr, index):
    if len(arr) == 1:
        return arr[index]
    if low < high:
        pi = partition(low, high, arr)
        quicksort(low, pi - 1, arr, index)
        quicksort(pi + 1, high, arr, index)
    return arr[index]

for index in range(len(wordsList) - 1):
    print(quicksort(0, len(wordsList) - 1, wordsList, index))

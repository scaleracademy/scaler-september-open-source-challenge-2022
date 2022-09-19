#!/usr/bin/python
# -*- coding: utf-8 -*-


def InsertionSort(arr):

    n = len(arr)

    for i in range(0, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# driver code

arr = [6, 5, 3, 2, 8, 10, 9]
InsertionSort(arr)
print(arr)

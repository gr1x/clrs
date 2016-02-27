#!/bin/env python

def binary_search(vector, value):
    low = 0
    high = len(vector) - 1
    while low < high:
        mid = (high - low) / 2 + low
        if vector[mid] == value :
            return mid
        elif vector[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return None

vector = [1, 2, 3, 4, 5, 6]
print binary_search(vector, 3)
print binary_search(vector, 1)
print binary_search(vector, 5)
print binary_search(vector, 0)


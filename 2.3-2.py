#!/bin/env python
# From book "Python Algorithms 2nd"

def merge_sort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]

    if len(lft) > 1:
        lft = merge_sort(lft)
    if len(rgt) > 1:
        rgt = merge_sort(rgt)

    result = []
    # while lft and rgt:
        # if lft[-1] >= rgt[-1]:
            # result.append(lft.pop())
        # else:
            # result.append(rgt.pop())
    # result += (lft[::-1] or rgt[::-1])
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            result.append(rgt.pop())
        else:
            result.append(lft.pop())
    result += (lft or rgt)

    result.reverse()
    return result

if __name__ == "__main__":
    A = [3, 52, 41, 26, 38, 9, 57, 49, 9]
    print A
    B = merge_sort(A)
    print B




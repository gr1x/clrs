#!/bin/evn python

A = [33,82,892,39,82,29,3]

def linear(vector, target):
    for i in range(len(vector)):
        if vector[i] == target:
            print "%u is at index of %u" % (target, i)
            return
    print "NIL"
    return

if __name__ == "__main__":
    linear(A, 82)
    print "*"*20
    linear(A, 29)
    print "*"*20
    linear(A, 59)

# Loop invariant
# Subarray vector[0...i-1] consists of elements different from target
# 1. Initialization
# An empty subarray, no element, so different from target
# 2. Maintenance
# vector[0...i-1] is different from target, when vector[i]=target, then it's index is printed; if vector[i]!=target, then vector[i]is added to vector[0...i-1], so vector[0...i] consists of elements different from target.
# 3.Termination
# when i > len(Vector), loop terminates, all elements have been checked in vector[], and haven't found target, so print NIL.

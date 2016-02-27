#!/bin/evn python


def add(A, B):
    C = ''
    carry = 0
    for i in range(len(A) - 1, -1, -1):
        c = (int(A[i]) + int(B[i]) + carry) % 2  # remainder
        carry = (int(A[i]) + int(B[i]) + carry) / 2
        C += str(c)
    C += str(carry)
    C = C[::-1]
    return C

if __name__ == "__main__":
    A = "11001010"
    B = "10101101"
    print A + " + " + B  + " =",
    print add(A, B)

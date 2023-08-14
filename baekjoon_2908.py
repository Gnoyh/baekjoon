# https://www.acmicpc.net/problem/2908

A, B = input().split()

for i in range(len(A)):
    if A[len(A) - 1 - i] < B[len(B) - 1 - i]:
        for j in range(len(B)):
            print(B[len(B) - 1 - j], end="")

        break

    elif A[len(A) - 1 - i] > B[len(B) - 1 - i]:
        for j in range(len(A)):
            print(A[len(A) - 1 - j], end="")

        break
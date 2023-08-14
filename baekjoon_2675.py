# https://www.acmicpc.net/problem/2675

T = int(input())

for i in range(T):
    R, S = input().split()

    for i in S:
        check = 0

        while(check < int(R)):
            print(i, end="")

            check += 1

    print()
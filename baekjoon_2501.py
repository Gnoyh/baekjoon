# https://www.acmicpc.net/problem/2501

N, K = map(int, input().split())

check = 1

while True:
    if N % check == 0:
        K -= 1

    if K == 0:
        print(check)

        break

    if N == check:
        break

    check += 1

if K != 0:
    print(0)
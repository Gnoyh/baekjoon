# https://www.acmicpc.net/problem/11653

N = int(input())

check = N

for i in range(2, N + 1):
    while N % i == 0:
        print(i)

        N /= i

    if N == 1:
        break

    if N == check and i > check // 3:
        print(check)

        break
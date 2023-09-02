# https://www.acmicpc.net/problem/5086

a, b = -1, -1

while True:
    a, b = map(int, input().split())

    if a + b == 0:
        break

    if b % a == 0:
        print("factor")

        continue

    if a % b == 0:
        print("multiple")

        continue

    print("neither")
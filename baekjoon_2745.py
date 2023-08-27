# https://www.acmicpc.net/problem/2745

N, B = input().split()

N = N[::-1]

result = 0

for i in range(len(N)):
    if ord(N[i]) >= 65:
        result += (ord(N[i]) - 55) * int(B) ** i
    else:
        result += int(N[i]) * int(B) ** i

print(result)
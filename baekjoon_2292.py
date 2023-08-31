# https://www.acmicpc.net/problem/2292

N = int(input())

N -= 1
result = 1

while True:
    if N < 1:
        break
    else:
        N -= 6 * result
        result += 1

print(result)
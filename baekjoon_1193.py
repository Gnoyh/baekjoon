# https://www.acmicpc.net/problem/1193

X = int(input())

check = 0
i = 0

result_a = 0
result_b = 0

while True:
    i += 1
    check += 1

    if X <= i:
        if i % 2 == 0:
            result_a = X
            result_b = i + 1 - X
        else:
            result_a = i + 1 - X
            result_b = X

        break
    else:
        X -= check

print("%d/%d" % (result_a, result_b))
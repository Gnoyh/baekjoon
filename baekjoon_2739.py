# https://www.acmicpc.net/problem/2739

num = int(input())

for i in range(1, 10):
    print("%d * %d = %d" %(num, i, num * i))

    i += 1
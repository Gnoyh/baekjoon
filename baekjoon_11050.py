# https://www.acmicpc.net/problem/11050

from sys import stdin

N, K = map(int, stdin.readline().split())

K = min(N - K, K)

check_N = 1
check_K = 1

for i in range(K):
    check_N *= N
    check_K *= K

    N -= 1
    K -= 1

print(check_N // check_K)
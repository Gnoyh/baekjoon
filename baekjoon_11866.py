# https://www.acmicpc.net/problem/11866

from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())

def josephus():
    input_queue = deque(str(i) for i in range(1, N + 1))

    result_list = list()

    while input_queue:
        input_queue.rotate(-((K - 1) % len(input_queue)))

        result_list.append(input_queue.popleft())

    return result_list

result_list = josephus()

print("<" + ", ".join(result_list), end=">")
# https://www.acmicpc.net/problem/24511

from sys import stdin
from collections import deque

def queuestack():
    N = int(stdin.readline())

    check_list = list(map(int, stdin.readline().split()))
    input_list = list(map(int, stdin.readline().split()))

    B = int(stdin.readline())

    insert_list = list(map(int, stdin.readline().split()))

    queue_deque = deque(input_list[i] for i in range(N) if check_list[i] == 0)

    for i in range(B):
        queue_deque.appendleft(insert_list[i])
        print(queue_deque.pop(), end=" ")

queuestack()
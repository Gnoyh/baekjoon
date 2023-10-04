# https://www.acmicpc.net/problem/24511

from sys import stdin

def queuestack():
    N = int(stdin.readline())

    queue_list = [j for i, j in zip(stdin.readline().split(), stdin.readline().split()) if i == "0"]

    B = int(stdin.readline())

    insert_list = stdin.readline().split()

    queue_list.reverse()

    queue_list.extend(insert_list)

    print(" ".join(queue_list[: B]))

queuestack()
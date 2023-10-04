# https://www.acmicpc.net/problem/24511

from sys import stdin

def queuestack():
    N = int(stdin.readline())

    check_list = list(map(int, stdin.readline().split()))
    input_list = list(map(int, stdin.readline().split()))

    B = int(stdin.readline())

    insert_list = list(map(int, stdin.readline().split()))

    queue_list = list(input_list[i] for i in range(N) if check_list[i] == 0)
    result_list = list()

    queue_list.reverse()

    for i in range(B):
        queue_list.append(insert_list[i])
        result_list.append(str(queue_list[i]))

    print(" ".join(result_list))

queuestack()
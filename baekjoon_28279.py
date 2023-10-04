# https://www.acmicpc.net/problem/28279

from sys import stdin
from collections import deque

N = int(stdin.readline())

def deq():
    check_deque = deque()
    result_list = list()

    for _ in range(N):
        input_str = stdin.readline().strip().split()

        if input_str[0] == "1":
            check_deque.appendleft(input_str[1])
        elif input_str[0] == "2":
            check_deque.append(input_str[1])
        elif input_str[0] == "3":
            if check_deque:
                result_list.append(check_deque.popleft())
            else:
                result_list.append("-1")
        elif input_str[0] == "4":
            if check_deque:
                result_list.append(check_deque.pop())
            else:
                result_list.append("-1")
        elif input_str[0] == "5":
            result_list.append(str(len(check_deque)))
        elif input_str[0] == "6":
            if check_deque:
                result_list.append("0")
            else:
                result_list.append("1")
        elif input_str[0] == "7":
            if check_deque:
                result_list.append(check_deque[0])
            else:
                result_list.append("-1")
        elif input_str[0] == "8":
            if check_deque:
                result_list.append(check_deque[-1])
            else:
                result_list.append("-1")

    print("\n".join(result_list))

deq()
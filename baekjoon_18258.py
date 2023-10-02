# https://www.acmicpc.net/problem/18258

from sys import stdin

N = int(stdin.readline())

def queue():
    input_list = list()
    result_list = list()

    check = 0

    for _ in range(N):
        input_str = stdin.readline().strip().split()

        if input_str[0] == "push":
            input_list.append(input_str[-1])
        elif input_str[0] == "pop":
            if check < len(input_list):
                result_list.append(input_list[check])

                check += 1
            else:
                result_list.append("-1")
        elif input_str[0] == "size":
            if check < len(input_list):
                result_list.append(str(len(input_list) - check))
            else:
                result_list.append("0")
        elif input_str[0] == "empty":
            if check < len(input_list):
                result_list.append("0")
            else:
                result_list.append("1")
        elif input_str[0] == "front":
            if check < len(input_list):
                result_list.append(input_list[check])
            else:
                result_list.append("-1")
        elif input_str[0] == "back":
            if check < len(input_list):
                result_list.append(input_list[-1])
            else:
                result_list.append("-1")

        if check == len(input_list):
            check = 0
            input_list = list()

    print("\n".join(result_list))

queue()
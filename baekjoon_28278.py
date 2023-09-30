# https://www.acmicpc.net/problem/28278

from sys import stdin

N = int(stdin.readline())

input_list = list()
result_list = list()

def stack(N):
    for i in range(N):
        input_str = stdin.readline().strip().split()

        if input_str[0] == "1":
            input_list.append(input_str[-1])
        elif input_str[0] == "2":
            if input_list:
                result_list.append(input_list.pop())
            else:
                result_list.append("-1")
        elif input_str[0] == "3":
            result_list.append(str(len(input_list)))
        elif input_str[0] == "4":
            if input_list:
                result_list.append("0")
            else:
                result_list.append("1")
        elif input_str[0] == "5":
            if input_list:
                result_list.append(input_list[-1])
            else:
                result_list.append("-1")

stack(N)

print("\n".join(result_list))
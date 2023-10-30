# https://www.acmicpc.net/problem/14888

from sys import stdin

N = int(stdin.readline())

input_list1 = list(map(int, stdin.readline().split()))
input_list2 = list(map(int, stdin.readline().split()))

result_list = []

def operator(list, result, check):
    if check == N:
        result_list.append(result)

        return

    for i in range(4):
        if list[i] != 0:
            check_list = list.copy()

            if i == 0:
                check_list[i] -= 1

                operator(check_list, result + input_list1[check], check + 1)
            elif i == 1:
                check_list[i] -= 1

                operator(check_list, result - input_list1[check], check + 1)
            elif i == 2:
                check_list[i] -= 1

                operator(check_list, result * input_list1[check], check + 1)
            else:
                check_list[i] -= 1

                if result < 0 or input_list1[check] < 0:
                    operator(check_list, -(abs(result) // abs(input_list1[check])), check + 1)
                else:
                    operator(check_list, abs(result) // abs(input_list1[check]), check + 1)

operator(input_list2, input_list1[0], 1)

print(max(result_list))
print(min(result_list))
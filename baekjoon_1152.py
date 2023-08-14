# https://www.acmicpc.net/problem/1152

input_str = input()

result_int = 0
check = 0

for i in input_str:
    if i == " ":
        check = 0
    else:
        if check == 0:
            result_int += 1

            check = 1

print(result_int)
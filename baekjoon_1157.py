# https://www.acmicpc.net/problem/1157

input_str = input().upper()

check_max = 0
result = ""

for i in set(input_str):
    if check_max == input_str.count(i):
        result = "?"
    elif check_max < input_str.count(i):
        check_max = input_str.count(i)
        result = i

print(result)
# https://www.acmicpc.net/problem/2941

input_str = input()

check_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in check_list:
    input_str = input_str.replace(i, "0")

print(len(input_str))
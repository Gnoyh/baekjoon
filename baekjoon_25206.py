# https://www.acmicpc.net/problem/25206

check_dict = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
check_float = 0.0

result_float = 0.0

for i in range(20):
    a, b, c = input().split()

    if c != "P":
        check_float += float(b)

        result_float += float(b) * check_dict[c]

print(result_float / check_float)
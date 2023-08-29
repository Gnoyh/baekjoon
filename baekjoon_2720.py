# https://www.acmicpc.net/problem/2720

T = int(input())

check_list = [25, 10, 5, 1]

for i in range(T):
    C = int(input())

    for j in check_list:
        print(C // j, end=" ")

        C = C % j

    print()
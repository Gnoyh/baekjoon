# https://www.acmicpc.net/problem/9012

from sys import stdin

T = int(stdin.readline())

def ps():
    for i in range(T):
        check_list = list()

        input_str = stdin.readline().strip()

        for j in input_str:
            if j == "(":
                check_list.append(0)
            elif j == ")":
                if check_list:
                    check_list.pop()
                else:
                    print("NO")

                    break
        else:
            if len(check_list) == 0:
                print("YES")
            else:
                print("NO")

ps()
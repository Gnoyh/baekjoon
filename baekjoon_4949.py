# https://www.acmicpc.net/problem/4949

from sys import stdin

def balance():
    while True:
        input_str = stdin.readline().rstrip()

        check_list = list()

        result = "yes"

        if input_str == ".":
            break

        for i in input_str:
            if i == "(":
                check_list.append(1)

            if i == "[":
                check_list.append(2)

            if i == ")":
                if check_list:
                    if check_list[-1] == 1:
                        check_list.pop()
                    else:
                        result = "no"

                        break
                else:
                    result = "no"

                    break

            if i == "]":
                if check_list:
                    if check_list[-1] == 2:
                        check_list.pop()
                    else:
                        result = "no"

                        break
                else:
                    result = "no"

                    break

        if len(check_list) == 0:
            print(result)
        else:
            print("no")

balance()
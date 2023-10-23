# https://www.acmicpc.net/problem/11729

from sys import stdin

K = int(stdin.readline())

result_list = []

def hanoi(k, bar1, bar2, bar3):
    if k == 1:
        result_list.append(str(bar1) + " " + str(bar2))

        return

    hanoi(k - 1, bar1, bar3, bar2)

    result_list.append(str(bar1) + " " + str(bar2))

    hanoi(k - 1, bar3, bar2, bar1)

hanoi(K, 1, 3, 2)

print(len(result_list))
print("\n".join(result_list))
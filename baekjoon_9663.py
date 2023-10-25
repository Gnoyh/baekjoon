# https://www.acmicpc.net/problem/9663

from sys import stdin

N = int(stdin.readline())

result = 0

def nqueen(check):
    global result

    if len(check_set1) == N:
        result += 1

        return

    for i in range(N):
        if i in check_set1:
            continue
        else:
            j = check - i
            k = check + i

            if j in check_set2 or k in check_set3:
                continue
            else:
                check_list[check] = i
                check_set1.add(i)
                check_set2.add(j)
                check_set3.add(k)

                nqueen(check + 1)

                check_set1.discard(i)
                check_set2.discard(j)
                check_set3.discard(k)

check_list = [0] * N
check_set1 = set()
check_set2 = set()
check_set3 = set()

nqueen(0)

print(result)
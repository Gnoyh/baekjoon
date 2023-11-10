# https://www.acmicpc.net/problem/2580

from sys import stdin

input_list = [list(map(int, stdin.readline().split())) for _ in range(9)]
check_list = []

for i in range(9):
    for j in range(9):
        if input_list[i][j] == 0:
            check_list.append((i, j))

def txt(x):
    if x in {0, 1, 2}:
        return [0, 1, 2]
    elif x in {3, 4, 5}:
        return [3, 4, 5]
    else:
        return[6, 7, 8]

def sudoku(count):
    if count == len(check_list):
        for i in range(9):
            print(*input_list[i])

        exit(0)

    for i in range(1, 10):
        check = 1

        for j in input_list[check_list[count][0]]:
            if j == i:
                check = 0

                break

        if check == 0:
            continue

        for j in range(9):
            if input_list[j][check_list[count][1]] == i:
                check = 0

                break

        if check == 0:
            continue

        for j in txt(check_list[count][0]):
            for k in txt(check_list[count][1]):
                if input_list[j][k] == i:
                    check = 0

                    break

        if check == 0:
            continue

        input_list[check_list[count][0]][check_list[count][1]] = i

        sudoku(count + 1)

        input_list[check_list[count][0]][check_list[count][1]] = 0

sudoku(0)
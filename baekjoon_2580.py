# https://www.acmicpc.net/problem/2580

from sys import stdin

input_list = [list(map(int, stdin.readline().split())) for _ in range(9)]
check_list = []

for i in range(9):
    for j in range(9):
        if input_list[i][j] == 0:
            check_list.append((i, j))

def row(i, x):
    for j in input_list[x]:
        if j == i:
            return False

    return True

def column(i, y):
    for j in range(9):
        if input_list[j][y] == i:
            return False

    return True

def square(i, x, y):
    for j in range(3 * (x // 3), 3 * (x // 3) + 3):
        for k in range(3 * (y // 3), 3 * (y // 3) + 3):
            if input_list[j][k] == i:
                return False

    return True

def sudoku(count):
    if count == len(check_list):
        for i in range(9):
            print(*input_list[i])

        exit()

    x = check_list[count][0]
    y = check_list[count][1]

    for i in range(1, 10):
        if row(i, x) and column(i, y) and square(i, x, y):
            input_list[check_list[count][0]][check_list[count][1]] = i

            sudoku(count + 1)

            input_list[check_list[count][0]][check_list[count][1]] = 0

sudoku(0)
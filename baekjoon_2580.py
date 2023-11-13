# https://www.acmicpc.net/problem/2580

from sys import stdin

input_list = [list(map(int, stdin.readline().split())) for _ in range(9)]
check_list = []
row_list = [[True] * 10 for _ in range(9)]
column_list = [[True] * 10 for _ in range(9)]
square_list = [[[], [], []], [[], [], []], [[], [], []]]

for i in range(9):
    for j in range(9):
        if input_list[i][j] == 0:
            check_list.append((j, i))
        else:
            row_list[i][input_list[i][j]] = False
            column_list[j][input_list[i][j]] = False

for i in range(3):
    square_list_1 = [True] * 10
    square_list_2 = [True] * 10
    square_list_3 = [True] * 10

    for j in range(3):
        for k in range(3):
            square_list_1[input_list[i * 3 + j][k]] = False
            square_list_2[input_list[i * 3 + j][k + 3]] = False
            square_list_3[input_list[i * 3 + j][k + 6]] = False

    square_list[i][0] = square_list_1
    square_list[i][1] = square_list_2
    square_list[i][2] = square_list_3

def sudoku(count):
    if count == len(check_list):
        for i in range(9):
            print(*input_list[i])

        exit()

    x = check_list[count][0]
    y = check_list[count][1]

    for i in range(1, 10):
        if row_list[y][i] and column_list[x][i] and square_list[y // 3][x // 3][i]:
            input_list[y][x] = i
            row_list[y][i] = False
            column_list[x][i] = False
            square_list[y // 3][x // 3][i] = False

            sudoku(count + 1)

            input_list[y][x] = 0
            row_list[y][i] = True
            column_list[x][i] = True
            square_list[y // 3][x // 3][i] = True

sudoku(0)
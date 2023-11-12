# https://www.acmicpc.net/problem/2580

from sys import stdin

input_list = [list(map(int, stdin.readline().split())) for _ in range(9)]
check_list = []
row_list = []
column_list = []
square_list = [[], [], []]

for i in range(9):
    column_set = set()

    for j in range(9):
        if input_list[i][j] == 0:
            check_list.append((j, i))

        column_set.add(input_list[j][i])

    row_list.append(set(input_list[i]))
    column_list.append(column_set)

for i in range(3):

    square_set_1 = set()
    square_set_2 = set()
    square_set_3 = set()

    for j in range(3):
        for k in range(3):
            square_set_1.add(input_list[i * 3 + j][k])
            square_set_2.add(input_list[i * 3 + j][k + 3])
            square_set_3.add(input_list[i * 3 + j][k + 6])

    square_list[i].append(square_set_1)
    square_list[i].append(square_set_2)
    square_list[i].append(square_set_3)

def sudoku(count):
    if count == len(check_list):
        for i in range(9):
            print(*input_list[i])

        exit()

    x = check_list[count][0]
    y = check_list[count][1]

    for i in range(1, 10):
        if i not in row_list[y] and i not in column_list[x] and i not in square_list[y // 3][x // 3]:
            input_list[y][x] = i
            row_list[y].add(i)
            column_list[x].add(i)
            square_list[y // 3][x // 3].add(i)

            sudoku(count + 1)

            input_list[y][x] = 0
            row_list[y].discard(i)
            column_list[x].discard(i)
            square_list[y // 3][x // 3].discard(i)

sudoku(0)
#!/usr/bin/env python
import os
import getch

grid = []
col = 0
row = 0

# mazes can be generated from http://www.delorie.com/game-room/mazes/genmaze.cgi
with open('maze.txt', 'r') as f:
    for line in f:
        line = line.rstrip("\n")
        grid.append(list(line))

col_depth = len(grid)
row_depth = len(grid[0])

while True:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

    if grid[row][col] == '$':
        exit()

    old_tile = grid[row][col]
    grid[row][col] = '@'

    for line in grid:
        print(*line)

    grid[row][col] = old_tile
    c = getch.getch()

    if (c == 'h') and (col - 1 >= 0) and (grid[row][col - 1] != "*"):
        col -= 1
    if (c == 'j') and (row + 1 < col_depth) and (grid[row + 1][col] != "*"):
        row += 1
    if c == 'k' and (row - 1 >= 0) and (grid[row - 1][col] != "*"):
        row -= 1
    if c == 'l' and (col + 1 < row_depth) and (grid[row][col + 1] != "*"):
        col += 1

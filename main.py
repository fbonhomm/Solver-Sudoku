# @Author: flo
# @Date:   Tuesday, March-14-2017, 20:05:42
# @Email:  flo-github@outlook.fr
# @Filename: main.py
# @Last modified by:   flo
# @Last modified time: Tuesday, March-14-2017, 22:52:06


def getRow(grid, current, col):
    for i in range(0, 8):
        if grid[col][i] == current:
            return False
    return True


def getCol(grid, current, row):
    for i in range(0, 8):
        if grid[i][row] == current:
            return False
    return True


def getBlock(grid, current, col, row):
    while col % 3 != 0:
        col -= 1
    while row % 3 != 0:
        row -= 1

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[col + i][row + j] == current:
                return False
    return True


def display(grid):
    for i in range(0, len(grid)):
        tmp = ''
        for j in range(0, len(grid)):
            if j == 0:
                tmp += '|' + str(grid[i][j]) + '|' if grid[i][j] else '|.|'
            else:
                tmp += str(grid[i][j]) + '|' if grid[i][j] else '.|'
        print(tmp)
    print('')


def solver(grid, col, row):
    if col == 8 and row == 9:
        return True

    if row == 9:
        return solver(grid, col + 1, 0)

    if grid[col][row] != 0:
        return solver(grid, col, row + 1)

    for current in range(1, 10):
        if getRow(grid, current, col) and getCol(grid, current, row) and getBlock(grid, current, col, row):
            grid[col][row] = current

            if solver(grid, col, row + 1):
                return True

    grid[col][row] = 0
    return False


def main():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]

    print('Back: ')
    display(grid)

    solver(grid, 0, 0)

    print('After: ')
    display(grid)


if __name__ == '__main__':
    main()

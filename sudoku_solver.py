# Sudoku Solver
def solve_sudoku(sudoku):
    sudoku_solve = [row[:] for row in sudoku]
    row, col = 0, 0

    while not is_solve_sudoku(sudoku_solve):
        if sudoku_solve[row][col] == 0:
            while not is_valid_place(sudoku_solve, row, col):
                sudoku_solve[row][col] += 1
                if sudoku_solve[row][col] > 9:
                    sudoku_solve[row][col] = 0
                    row, col = check_revers_cells(sudoku_solve, sudoku, row, col)
                    sudoku_solve[row][col] += 1
        col += 1
        if col > 8:
            col = 0
            row += 1
        if row > 8:
            break
    return sudoku_solve


# check if the row is valid
def is_valid_in_row(sudoku, row, col):
    return sudoku[row].count(sudoku[row][col]) == 1


# check if the col is valid
def is_valid_in_col(sudoku, row, col):
    value = sudoku[row][col]
    return list(map(lambda row2: row2[col], sudoku)).count(value) == 1


# check if square is valid
def is_valid_square(sudoku, row, col):
    org_col = col
    org_row = row

    row = (row // 3) * 3
    col = (col // 3) * 3
    li_square = []

    for i in range(3):
        for j in range(3):
            li_square.append(sudoku[row][col])
            col += 1
        row += 1
        col = (org_col // 3) * 3

    return not li_square.count(sudoku[org_row][org_col]) > 1


def is_valid_place(sudoku, row, col):
    if sudoku[row][col] == 0:
        return False
    return is_valid_in_row(sudoku, row, col) and is_valid_in_col(sudoku, row, col) and is_valid_square(sudoku, row, col)


def is_solve_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if not is_valid_place(sudoku, row, col) or sudoku[row][col] == 0:
                return False
    return True


def check_revers_cells(sudoku, temp_sudoku, row, col):
    while True:
        row, col = reverse(row, col)
        if temp_sudoku[row][col] == 0:
            if sudoku[row][col] != 9:
                return row, col
            else:
                sudoku[row][col] = 0


def reverse(row, col):
    if col == 0:
        col = 8
        row -= 1
    else:
        col = col - 1
    return row, col


def print_sudoku(sudoku):
    print("______________________")
    for index_row, row in enumerate(sudoku):
        for index_col, cell in enumerate(row):
            print(f"{cell} ", end="")
            if (index_col + 1) % 3 == 0:
                print("|", end="")
        if (index_row + 1) % 3 == 0:
            print("\n______________________")
        else:
            print("")

if __name__ == '__main__':
    # Solver Sudoku

    sudoku2 = [
        [6, 0, 0, 1, 7, 0, 0, 0, 5],
        [0, 0, 0, 0, 4, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 8, 9, 0],
        [0, 3, 7, 8, 0, 0, 0, 0, 2],
        [5, 0, 0, 0, 0, 1, 0, 0, 9],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 2, 4, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 6, 0, 0],
        [7, 0, 0, 3, 0, 0, 0, 0, 0]
    ]
    print_sudoku(solve_sudoku(sudoku2))

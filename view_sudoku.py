# GUI - Sudoku
import pygame

b_check_color = (100, 0, 0)


def create_win_sudoku(win, board, background_color, board_original_element_color):
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont("Comic Sans Ms", 35)  # create font object (type of style, size)

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 * i + 50), (500, 50 + 50 * i), 4)
        else:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pygame.draw.line(win, (0, 0, 0), (50, 50 * i + 50), (500, 50 + 50 * i), 2)
        pygame.display.update()

    for i in range(9):
        for j in range(9):
            if board[i][j] > 0:
                value = myfont.render(str(board[i][j]), True, board_original_element_color)
                win.blit(value, ((j + 1) * 50 + 14, (i + 1) * 50 + 2))
    b_check = myfont.render("Check:", True, b_check_color)
    win.blit(b_check, (50, 497))
    b_check = myfont.render("Solve", True, b_check_color)
    win.blit(b_check, (400, 497))


def win_solve_sudoku(win, board, board_solve, board_original):
    # Show the solution in the board
    myfont = pygame.font.SysFont("Comic Sans Ms", 35)  # create font object (type of style, size)
    for row in range(9):
        for col in range(9):
            if board_original[row][col] == 0:  # change the value if it's not constant
                if board[row][col] != 0 and board_solve[row][col] != board[row][col]:
                    # if the user enter wrong input clear the cell
                    pygame.draw.rect(win, (230, 230, 230), (50 * col + 54, 50 * row + 54, 44, 44))
                board[row][col] = board_solve[row][col]
                value = myfont.render(str(board[row][col]), True, (100, 0, 0))
                win.blit(value, ((col + 1) * 50 + 14, (row + 1) * 50 + 2))


def message_wrong_winner(message, win):
    myfont = pygame.font.SysFont("Comic Sans Ms", 35)  # create font object (type of style, size)
    pygame.draw.rect(win, (230, 230, 230), (160, 505, 200, 40))
    b_check = myfont.render(message, True, b_check_color)
    win.blit(b_check, (160, 497))

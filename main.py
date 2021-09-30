import pygame
import requests
from sudoku_solver import solve_sudoku
from view_sudoku import win_solve_sudoku, message_wrong_winner, create_win_sudoku


WIDTH = 550
background_color = (230, 230, 230)
board_original_element_color = (0, 0, 0)
b_check_color = (100, 0, 0)
board_mark_element_color = (100, 0, 0)
response = requests.get(f"https://sugoku.herokuapp.com/board?difficulty=easy")
board = response.json()["board"]
board_original = [row[:] for row in board]  # copy the board
board_solve = solve_sudoku(board)  # solved board


def insert(win, position):
    myfont = pygame.font.SysFont("Comic Sans Ms", 35)
    buffer_i = position[1] % 50 - 4
    buffer_j = position[0] % 50 - 4
    i, j = position[1] // 50 - 1, position[0] // 50 - 1
    if i == 9:
        if 0 <= j <= 1:
            # If the user push on the button "check" so this function display on the board the answer
            message = "WINNER!!" if board == board_solve else "WRONG!"
            message_wrong_winner(message, win)
            pygame.display.update()
            return
        if 7 <= j <= 8:
            # If the user push on the button "solve" so this function display on the board the solution
            win_solve_sudoku(win, board, board_solve, board_original)
            pygame.display.update()
            return
    if i > 8 or j > 8 or i < 0 or j < 0:
        # Invalid position
        return

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if board_original[i][j] != 0:
                    return
                elif event.key == 8:  # If the user push on "Space back" so it's erase from board
                    board[i][j] = 0
                    pygame.draw.rect(win, background_color, (position[0] - buffer_j, position[1] - buffer_i, 44, 44))
                    pygame.display.update()
                    return
                elif 0 < event.key - 48 < 10:  # If the user push on "Number(1-9)" so it's mark on board
                    # Take the user number and put it in the board
                    # event.key - 48  =  The number
                    board[i][j] = event.key - 48  # The number
                    pygame.draw.rect(win, background_color, (position[0] - buffer_j, position[1] - buffer_i, 44, 44))
                    value = myfont.render(str(board[i][j]), True, board_mark_element_color)
                    win.blit(value, ((j + 1) * 50 + 14, (i + 1) * 50 + 2))
                    pygame.display.update()
                    return

# Main

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    create_win_sudoku(win, board, background_color, board_original_element_color)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # event.button == 1 --> left click
                pos = pygame.mouse.get_pos()  # return the position of the click
                insert(win, pos)
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == '__main__':
    main()

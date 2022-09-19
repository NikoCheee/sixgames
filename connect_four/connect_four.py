import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winnig_move(board, piece):
    # check for horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == piece:
                return True

    # check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] == piece:
                return True

    # check positively sloped diagonals for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] == piece:
                return True

    # check negatively sloped diagonals for win
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] == piece:
                return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, (0, 0, 255), (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, 'black', (c*SQUARESIZE+int(SQUARESIZE/2),
                                                 r*SQUARESIZE+SQUARESIZE+int(SQUARESIZE/2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, 'red',
                                       (c * SQUARESIZE + int(SQUARESIZE / 2), height - (r * SQUARESIZE + int(SQUARESIZE/2))), RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, 'yellow',
                                       (c * SQUARESIZE + int(SQUARESIZE / 2), height - (r * SQUARESIZE + int(SQUARESIZE/2))), RADIUS)
        pygame.display.update()


board = create_board()
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2) - 5

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
screen = pygame.display.set_mode((width, height))
draw_board(board)
pygame.display.update()
my_font = pygame.font.SysFont('smth', 95)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, 'black', (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, 'red', (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, 'yellow', (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, 'black', (0, 0, width, SQUARESIZE))
            # Ask for player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winnig_move(board, 1):
                        label = my_font.render("Player 1 win! Grac!!!", 1, 'red')
                        screen.blit(label, (40, 10))
                        game_over = True

            # Ask for player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winnig_move(board, 2):
                        label = my_font.render("Player 2 win! Grac!!!", 1, 'yellow')
                        screen.blit(label, (40, 10))
                        game_over = True

            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
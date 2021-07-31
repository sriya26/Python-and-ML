import numpy as np  # to create a matrix of 6x7


def new_board():
    board = np.zeros((6, 7))  # 6x7 matrix consisting of zeros
    return board


def player_turn():
    if turn == 0:
        piece = 1
    else:
        piece = 2
    return piece

def loc(board, choice):  # to check if the column selected is fully filled
    if board[5][choice] != 0:
        print("Invalid input")
        return True


def next_row(board, choice):  # # to check row for the selected column is not filled and whether the choice is valid
    for i in range(6):
        if board[i][choice] == 0:
            return i



def drop_piece(board, row, choice, piece):  # to drop a piece into the given position
    board[row][choice] = piece


def connect4(board, piece):
    # horizontal
    for j in range(4):  # column
        for k in range(6):  # row
            if board[k][j] == piece and board[k][j + 1] == piece and board[k][j + 2] == piece and board[k][
                j + 3] == piece:
                return True
    # vertical
    for j in range(7):
        for k in range(3):
            if board[k][j] == piece and board[k + 1][j] == piece and board[k + 2][j] == piece and board[k + 3][
                j] == piece:
                return True
    # diagonals
    for j in range(4):
        for k in range(3):
            if board[k][j] == piece and board[k + 1][j + 1] == piece and board[k + 2][j + 2] == piece and board[k + 3][
                j + 3] == piece:
                return True

    for j in range(4):
        for k in range(3, 6):
            if board[k][j] == piece and board[k - 1][j + 1] == piece and board[k - 2][j + 2] == piece and board[k - 3][
                j + 3] == piece:
                return True


def print_board(board):  # to flip the numpy array to see numbers filling from bottom to up
    print(np.flip(board, 0))


def draw(board):  # incase of draw condition
    for s in range(7):
        if board[5][s] != 0 and board[5][s + 1] != 0 and board[5][s + 2] != 0 and board[5][s + 3] != 0 and board[5][
            s + 4] != 0 and board[5][s + 5] != 0 and board[5][s + 6] != 0:
            return True


board = new_board()
print(board)
turn = 0  # to differentiate between player 1 and 2
gameover = False  # stops the game if a player wins

while not gameover:
    choice = int(input(f" Select from 0 to 6 (Player {player_turn()}): "))  # selecting the column
    gameover= loc(board, choice)
    if not gameover:
        row = next_row(board, choice)
        drop_piece(board, row, choice, player_turn())
        if connect4(board, player_turn()):
            print(f"Player {player_turn()}  wins!")
            gameover = True
        elif draw(board):
            print("Draw :)")
            gameover = True

    print_board(board)
    turn += 1
    turn = turn % 2  # to alternate between Player 1&2
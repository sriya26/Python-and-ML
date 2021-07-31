board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' ',
}  # dictionary to create a board
player = 1  # initialising 1st player
total_moves = 0  # to count the moves
check_end = 0  # to end game if any player wins before 9 total moves


def end_check():
    # checking moves of Player 1
    # for rows
    if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X':
        print('Player 1 won !')
        return 1
    if board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X':
        print('Player 1 Won!!')
        return 1
    if board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X':
        print('Player 1 Won!!')
        return 1

    # for diagonals
    if board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X':
        print('Player 1 Won!!')
        return 1
    if board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X':
        print('Player 1 Won!!')
        return 1

    # for columns
    if board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X':
        print('Player 1 Won!!')
        return 1
    if board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X':
        print('Player 1 Won!!')
        return 1
    if board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X':
        print('Player 1 Won!!')
        return 1

    # checking the moves of player 2
    # for rows
    if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O':
        print('Player 2 won !')
        return 1
    if board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
        print('Player 2 Won!!')
        return 1
    if board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
        print('Player 2 Won!!')
        return 1

    # for diagonals
    if board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O':
        print('Player 2 Won!!')
        return 1
    if board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O':
        print('Player 2 Won!!')
        return 1

    # for columns
    if board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O':
        print('Player 2 Won!!')
        return 1
    if board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O':
        print('Player 2 Won!!')
        return 1
    if board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O':
        print('Player 2 Won!!')
        return 1
    return 0  # if check fails


print('****************')
print('1|2|3')
print('- +- +-')
print('4|5|6')
print('- +- +-')
print('7|8|9')
print('****************')

while True:  # to show the status of the board
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    check_end = end_check()  # storing the return value in check_end

    if total_moves == 9 or check_end == 1:
        break

    while True:  # to take input from players
        if player == 1:  # choosing player
            p1_input = input('Player 1: ')
            if p1_input in board and board[p1_input] == ' ':  # to check if input is valid key and value is ''
                board[p1_input] = 'X'
                player = 2
                break

            else:  # on wrong input
                print('Invalid input, Please try again')
                continue
        else:  # for Player 2
            p2_input = input('Player 2: ')
            if p2_input in board and board[p2_input] == ' ':
                board[p2_input] = 'O'
                player = 1
                break
            else:
                print('Invalid input, please try again')
                continue
    total_moves += 1
    if total_moves == 9:
        print('Tie ;p')
    print('***************************')

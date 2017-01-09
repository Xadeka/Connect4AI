import copy

def won_horizontal(board):
    p1_count, p2_count = 0, 0
    for y in range(0, len(board)):
        for x in range(0, len(board[0])):
            if board[y][x] == 1:
                p1_count += 1
                p2_count = 0
            elif board[y][x] == 2:
                p1_count = 0
                p2_count += 1
            else:
                p1_count = 0
                p2_count = 0

            if p1_count == 4:
                return 1
            if p2_count == 4:
                return 2

    return 0

def won_vertical(board):
    p1_count, p2_count = 0, 0
    for x in range(0, len(board[0])):
        for y in range(0, len(board)):
            if board[y][x] == 1:
                p1_count += 1
                p2_count = 0
            elif board[y][x] == 2:
                p1_count = 0
                p2_count += 1
            else:
                p1_count = 0
                p2_count = 0

            if p1_count == 4:
                return 1
            if p2_count == 4:
                return 2

    return 0


def won_diagonal_left(board):
    # Iterating over 'starting' positions
    for row in range(0, len(board) - 3):
        for col in range(0, len(board[0]) - 3):
            winner = board[row][col] == board[row + 1][col + 1]
            if board[row+2][col+2] == winner:
                if board[row+3][col+3] == winner:
                    return winner
    return 0


def won_diagonal_right(board):
    # Iterating over 'starting' positions
    for row in range(3, len(board)):
        for col in range(0, len(board[0]) - 3):
            winner = board[row][col] == board[row - 1][col - 1]
            if board[row-2][col-2] == winner:
                if board[row-3][col-3] == winner:
                    return winner
    return 0


def win(board):
    winner = won_horizontal(board)
    if winner != 0:
        return winner

    winner = won_vertical(board)
    if winner != 0:
        return winner

    winner = won_diagonal_left(board)
    if winner != 0:
        return winner

    winner = won_diagonal_right(board)
    if winner != 0:
        return winner

    return winner


def get_possible_moves(board):
    moves = []
    for col in range(0, len(board[0])):
        if not board[0][col]:
            moves.append(col)
    return moves


def play(board, col, player):
    # Check if can be played
    b = copy.deepcopy(board)
    if col in get_possible_moves(b):
        for row in range(1, len(b)+1):
            if row == len(b) or b[row][col] != 0:
                b[row-1][col] = player
                return b
    return None

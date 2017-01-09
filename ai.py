import sys, argparse, ast, copy
import boardutils

board, player, time = None, None, None
choice = 0
MAX_DEPTH = 4

def switch_players(p):
    if p == 1:
        return 2
    return 1


# had to play with these values to get a decent result
def score(winner, depth):
    if winner == player:
        return depth - 10
    else:
        return 10 - depth
    return 0

def minmax(game, depth, current_player):
    global choice
    if depth > MAX_DEPTH:
        return 0
    possible_moves = boardutils.get_possible_moves(game)
    # if there is no contest
    if len(possible_moves) == 0:
        return 0
    winner = boardutils.win(game)
    if winner != 0:
        return score(winner, depth)
    depth += 1
    scores = [] # an array of scores
    moves = []  # an array of moves

    # Populate the scores array, recursing as needed
    for move in possible_moves:
        next_player = switch_players(current_player)
        possible_game = boardutils.play(game, move, next_player)
        scores.append(minmax(possible_game, depth, next_player))
        moves.append(move)

    if depth == 1:
        print(moves)
        print(scores)
        print(current_player == player)

    # Do the min or the max calculation
    if current_player == player:
        # This is the max calculation
        max_score_index = scores.index(max(scores))
        choice = moves[max_score_index]
        return scores[max_score_index]
    else:
        # This is the min calculation
        min_score_index = scores.index(min(scores))
        choice = moves[min_score_index]
        return scores[min_score_index]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b')
    parser.add_argument('-p')
    parser.add_argument('-t', type=int)
    args = vars(parser.parse_args())

    board = ast.literal_eval(args['b'])
    if args['p'] == 'player-one':
        player = 1
    else:
        player = 2

    time = args['t']

    minmax(board, 0, player)
    print(choice)

    sys.exit(choice)

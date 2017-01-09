import sys, argparse, ast
import boardutils
from tree import Tree, Node

board, player, time = None, None, None
def main():
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

    #TODO: Create or read the tree and start the ai

    sys.exit(4)


def iterative_deepening(game, max_depth):
    first_guess = 0
    for depth in range(1, max_depth + 1):
        first_guess = mtd(game, first_guess, depth)
        # if times_up():
            # break

    return first_guess


def alpha_beta_with_mem(game, alpha, beta, depth):
    n = tree.get_node(game)
    g = None
    if n:
        if n.lower >= beta:
            return n.lower
        if n.upper <= alpha:
            return n.upper

        alpha = max(alpha, n.lower)
        beta = max(beta, n.upper)

    if depth == 0:
        g = eval(n)
    elif n.is_max_node:
        g = -sys.maxsize
        a = alpha
        c = tree.get_nth_child(n, 1)
        while g > alpha and c.has_children():
            g = max(g, alpha_beta_with_mem(c, a, beta, depth - 1))
            a = max(a, g)
            c = next_brother(c)
    else: # n is a minnode
        g = sys.maxsize
        b = beta
        c = tree.get_nth_child(n, 1)
        while g > alpha and c.has_children():
            g = min(g, alpha_beta_with_mem(c, alpha, b, depth - 1))
            b = min(b, g)
            c = tree.next_sibling(c)

    # Traditional transposition table storing of bounds
    # Fail low result implies an upper bound
    if g <= alpha:
        n.upper = g
        #store n.upper
        tree.update_node(n)
    # Found an accurate minimax value -  will not occur if called with zero window
    if g > alpha and g < beta:
        n.lower = g
        n.upper = g
        #store n.lower, store n.upper
        tree.update_node(n)

    # Fail high result implies a lower bound
    if g >= beta:
        n.lowerbound = g
        #store n.lowerbound
        tree.update_node(n)

    return g


def mtd(game, f, depth):
    g = f
    upper = sys.maxsize
    lower = -sys.maxsize

    while upper > lower:
        # Update beta
        if g == lower:
            beta = g + 1
        else:
            beta = g

        g = alpha_beta_with_mem(game, beta - 1, beta, depth)

        # Update upper or lower bounds
        if g < beta:
            upper = g
        else:
            lower = g

    return g


if __name__ == '__main__':
    main()

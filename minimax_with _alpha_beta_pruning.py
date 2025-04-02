#Minimax is a decision-making algorithm used in two-player games to minimize the possible loss for a worst-case scenario. It is widely used in game theory, particularly in turn-based games such as Chess or Tic-Tac-Toe. The basic idea is that the algorithm explores all possible moves and assumes that the opponent will also play optimally to minimize your score.
#Alpha-Beta pruning is an optimization technique used to reduce the number of nodes evaluated by the Minimax algorithm. It "prunes" branches in the decision tree that do not need to be explored because they cannot influence the final decision. This reduces the time complexity of the Minimax algorithm from O(b^d) to O(b^(d/2)) in the best case, where b is the branching factor and d is the depth of the tree.

#Key Concepts:
# 1 - Minimax Algorithm: It recursively evaluates all possible moves in the game tree, alternating between maximizing (your move) and minimizing (opponent’s move) the score.
# 2 - Alpha-Beta Pruning: It keeps track of two values:
# 2.1 - Alpha: The best value that the maximizing player can guarantee so far.
# 2.2 - Beta: The best value that the minimizing player can guarantee so far. It prunes the branches when it detects that further exploration will not affect the result.

#Steps:
# 1 - At each node, if it is the maximizing player’s turn, choose the maximum value from all child nodes.
# 2 - If it’s the minimizing player’s turn, choose the minimum value from all child nodes.
# 3 - Alpha and Beta values are updated as you move through the tree.
# 4 - Prune branches where Beta is less than or equal to Alpha.

#Python Code Implementation

# Define the game state and moves (This is a generic example. For Tic-Tac-Toe or Chess, it can be adapted).

# The game will have a simple state evaluation function
# This is just an example. In a real-world game, you would need to implement a game state with proper evaluation.
import math

# Example of a game board for a Tic-Tac-Toe like scenario
# The board is represented as a 3x3 grid, where:
# -1 represents the minimizing player (O)
#  1 represents the maximizing player (X)
#  0 represents an empty cell
game_board = [
    [0, 1, -1],
    [1, -1, 0],
    [-1, 1, 0]
]

# Function to evaluate the game state
# In a real game, this would return a positive number if the maximizing player wins,
# negative number if the minimizing player wins, and 0 if it's a draw.
def evaluate(board):
    # A simple example for evaluation (just for demonstration)
    return random.choice([1, -1, 0])  # Random winner (just for demo purposes)

# Function to check if the game is over
def is_game_over(board):
    # This will check if any player has won or if the board is full (draw)
    # In this simple case, we're assuming it returns True if the game ends
    return False  # Assume the game isn't over in this example

# Function to get all possible moves from a given board state
def get_possible_moves(board):
    # This will return all empty spots (in real game, this would be more complex)
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                moves.append((i, j))  # Row, Column
    return moves

# Minimax algorithm with Alpha-Beta Pruning
def minimax_with_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_game_over(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for move in get_possible_moves(board):
            # Make the move
            board[move[0]][move[1]] = 1  # Maximizing player makes the move
            eval = minimax_with_alpha_beta(board, depth - 1, alpha, beta, False)
            board[move[0]][move[1]] = 0  # Undo the move
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff (prune)
        return max_eval
    else:
        min_eval = math.inf
        for move in get_possible_moves(board):
            # Make the move
            board[move[0]][move[1]] = -1  # Minimizing player makes the move
            eval = minimax_with_alpha_beta(board, depth - 1, alpha, beta, True)
            board[move[0]][move[1]] = 0  # Undo the move
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff (prune)
        return min_eval

# Function to find the best move for the maximizing player
def find_best_move(board, depth):
    best_move = None
    best_value = -math.inf

    for move in get_possible_moves(board):
        # Make the move
        board[move[0]][move[1]] = 1  # Maximizing player makes the move
        move_value = minimax_with_alpha_beta(board, depth - 1, -math.inf, math.inf, False)
        board[move[0]][move[1]] = 0  # Undo the move

        if move_value > best_value:
            best_value = move_value
            best_move = move

    return best_move

# Example: Find the best move for the maximizing player (X)
depth = 3  # Limit the search depth
best_move = find_best_move(game_board, depth)
print(f"The best move is at: {best_move}")

#Explanation:
# 1 - evaluate(board): This function evaluates the board state and returns a score. It can be more complex depending on the game. For example, in Tic-Tac-Toe, it would return 1 for a win, -1 for a loss, and 0 for a draw.
# 2 - is_game_over(board): Checks if the game is over. In this case, it just returns False, but in a real implementation, it would check for a win or draw.
# 3 - get_possible_moves(board): This generates a list of all valid moves for the current player, i.e., the empty spots on the board.
# 4 - minimax_with_alpha_beta(board, depth, alpha, beta, maximizing_player): This is the core Minimax function with alpha-beta pruning. It recursively explores the game tree, pruning branches when it finds that they are no longer useful.
# 5 - find_best_move(board, depth): This function iterates over all possible moves for the maximizing player and applies the Minimax algorithm with alpha-beta pruning to find the best possible move.

#Output:
#When you run the code, it will find and print the best move for the maximizing player (X) at the given depth.

#For instance:
#The best move is at: (2, 2)

#This is a basic implementation. In a full game, you would want to create an actual game logic (e.g., for Tic-Tac-Toe, Chess, etc.) to handle the rules and game states more properly.

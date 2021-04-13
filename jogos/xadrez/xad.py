#https://www.geeksforgeeks.org/chess-library-in-python/
import chess
import chess.svg
import random
board = chess.Board()
move_count = 0
while not board.is_game_over():
    legal_count = board.legal_moves.count()
    move_list = list(board.legal_moves)  # Find legal moves
    # print(str(move_list))
    which_move = random.randint(0, legal_count-1)  # Random move index
    first_move = move_list[which_move]  # Select move
    move_holder = chess.Move.from_uci(str(first_move))
    board.push(move_holder)
    move_count += 1  # Make the move
    print(board)
    print(board.turn)
    print(board.outcome(), board.result())
print(move_count)

import time
import sys
import random
import chess
import chess.svg
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget


board = chess.Board()
move_count = 0
'''
while not board.is_game_over():
    legal_count = board.legal_moves.count()
    print(legal_count)
    move_list = list(board.legal_moves)  # Find legal moves
    print(str(move_list))
    which_move = random.randint(0, legal_count-1)  # Random move index
    print(which_move)
    first_move = move_list[which_move]  # Select move
    print(first_move)
    move_holder = chess.Move.from_uci(str(first_move))
    board.push(move_holder)
    move_count += 1  # Make the move
    print(board)
    while board.is_check() and ck == 0:
        # input("cheque")
        ck=1

    ck = 0

print(board.outcome(), board.result())
'''


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 500, 500)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 480, 480)

        self.chessboard = chess.Board()

        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

    def paintEvent(self, event):
        self.chessboard.push(self.rand())
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)


    def rand(self):

        time.sleep(0.5)

        if self.chessboard.is_game_over() == True:
            print(self.chessboard.outcome())
            exit()

        legal_count = self.chessboard.legal_moves.count()

        move_list = list(self.chessboard.legal_moves)  # Find legal moves

        which_move = random.randint(0, legal_count-1)  # Random move index

        first_move = move_list[which_move]  # Select move

        move_holder = chess.Move.from_uci(str(first_move))

    


        self.e = move_holder
        return self.e


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
   
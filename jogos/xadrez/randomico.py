import time
import sys
import random
import chess
import chess.svg
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget


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
        self.game_over()
        self.rand()
        self.tela_jog()

    def tela_jog(self):
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

    def game_over(self):
        if self.chessboard.is_game_over() == True:
            print(self.chessboard.outcome())
            input()
            exit()

    def rand(self):
        legal_count = self.chessboard.legal_moves.count()
        move_list = list(self.chessboard.legal_moves)  # Find legal moves
        which_move = random.randint(0, legal_count-1)  # Random move index
        first_move = move_list[which_move]  # Select move
        move_holder = chess.Move.from_uci(str(first_move))

        self.chessboard.push(move_holder)
        time.sleep(0.5)



app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())

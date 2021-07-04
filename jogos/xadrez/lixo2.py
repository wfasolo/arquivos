#https://www.twilio.com/blog/play-chess-whatsapp-python-twilio

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

        self.jogador = 1
        self.setGeometry(100, 100, 500, 500)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 480, 480)

        self.chessboard = chess.Board()

        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

    def paintEvent(self, event):
        self.testes()
        self.vez()
        self.tela_jog()

    def tela_jog(self):
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

    def testes(self):
        if self.chessboard.is_check() == True:
            print("CHECK")
            print(str(list(self.chessboard.legal_moves)))
            self.tela_jog()
            time.sleep(5)

        if self.chessboard.is_checkmate() == True:
            print("CHECK MATE")
            time.sleep(5)

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

        time.sleep(0.5)
        return move_holder

    def vez(self):

        if self.jogador == 1:
            self.chessboard.push(self.rand())
            self.jogador = 2

        elif self.jogador == 2:
            jogada = input('jogada: ')
            print(jogada)
            if chess.Move.from_uci(jogada) in self.chessboard.legal_moves:
                self.chessboard.push_san(jogada)
                self.jogador = 1
            else:
                print("Jogada Invalida...")


app = QApplication([])
window = MainWindow()
window.show()
app.exec()

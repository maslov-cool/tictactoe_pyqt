import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Крестики-нолики')

        self.end_game = False
        self.player = 'X'

        self.main_layout = QVBoxLayout()
        self.choose_player_layout = QHBoxLayout()
        self.first_row_layout = QHBoxLayout()
        self.second_row_layout = QHBoxLayout()
        self.third_row_layout = QHBoxLayout()

        self.x_radio = QRadioButton('X')
        self.x_radio.setChecked(True)
        self.x_radio.toggled.connect(self.choose_player)
        self.o_radio = QRadioButton('O')
        self.o_radio.toggled.connect(self.choose_player)

        self.button_grid = [[], [], []]

        for i in range(9):
            btn = QPushButton()
            btn.clicked.connect(lambda checked, n=i: self.action(n // 3, n % 3))

            if i < 3:
                self.button_grid[0].append(btn)
            elif i < 6:
                self.button_grid[1].append(btn)
            else:
                self.button_grid[2].append(btn)

        self.result = QLabel()

        self.new_game_button = QPushButton('Новая игра')
        self.new_game_button.clicked.connect(self.new_game)

        self.choose_player_layout.addWidget(self.x_radio)
        self.choose_player_layout.addWidget(self.o_radio)

        for i in self.button_grid[0]:
            self.first_row_layout.addWidget(i)

        for i in self.button_grid[1]:
            self.second_row_layout.addWidget(i)

        for i in self.button_grid[2]:
            self.third_row_layout.addWidget(i)

        self.main_layout.addLayout(self.choose_player_layout)
        self.main_layout.addLayout(self.first_row_layout)
        self.main_layout.addLayout(self.second_row_layout)
        self.main_layout.addLayout(self.third_row_layout)
        self.main_layout.addWidget(self.result)
        self.main_layout.addWidget(self.new_game_button)

        self.setLayout(self.main_layout)

    def choose_player(self):
        if not self.x_radio.isChecked():
            self.player = 'O'
        else:
            self.player = 'X'
        self.new_game()

    def new_game(self):
        for i in self.button_grid:
            for j in i:
                j.setText('')
                j.setEnabled(True)
        self.result.setText('')

    def action(self, i, j):
        if not self.button_grid[i][j].text():
            self.button_grid[i][j].setText(self.player)

            if ((len({i.text() for i in self.button_grid[0]}) == 1 or
                len({self.button_grid[0][0].text(), self.button_grid[1][1].text(), self.button_grid[2][2].text()}) == 1
                or
                len({self.button_grid[0][0].text(), self.button_grid[1][0].text(), self.button_grid[2][0].text()}) == 1)
                    and self.button_grid[0][0].text()):
                self.result.setText(f'Выиграл {self.player}!')
                self.end_game = True

            elif (len({self.button_grid[2][0].text(), self.button_grid[1][1].text(), self.button_grid[0][2].text()})
                  == 1 or len({i.text() for i in self.button_grid[2]}) == 1) and self.button_grid[2][0].text():
                self.result.setText(f'Выиграл {self.player}!')
                self.end_game = True

            elif (len({self.button_grid[0][1].text(), self.button_grid[1][1].text(), self.button_grid[2][1].text()})
                  == 1 or len({i.text() for i in self.button_grid[1]}) == 1) and self.button_grid[1][1].text():
                self.result.setText(f'Выиграл {self.player}!')
                self.end_game = True

            elif (len({self.button_grid[2][2].text(), self.button_grid[1][2].text(), self.button_grid[0][2].text()})
                  == 1 and self.button_grid[2][2].text()):
                self.result.setText(f'Выиграл {self.player}!')
                self.end_game = True

            elif all(all(j.text() for j in i) for i in self.button_grid):
                self.result.setText(f'Ничья!')
                self.end_game = True

            if self.end_game:
                for i in self.button_grid:
                    for j in i:
                        j.setEnabled(False)

            if self.player == 'X':
                self.player = 'O'
            else:
                self.player = 'X'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = TicTacToe()
    program.show()
    sys.exit(app.exec())

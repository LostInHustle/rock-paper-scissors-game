from time import sleep
from random import choice
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class RPSGameUI(QMainWindow):
    def __init__(self: 'RPSGameUI', parent: object) -> None:
        super().__init__()
        self.parent = parent
        self.setFixedHeight(300)
        self.setFixedWidth(450)
        self.setWindowTitle("Rock-Paper-Scissors Game")
        layout = QGridLayout()

        title_line = QLabel("<h2>Let's Get Started😎</h2>")
        title_line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instruction = QLabel("'R' for rock!\n'P' for paper!\n'S' for scissors!")
        instruction.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_yourchoice = QLabel("Your Choice")
        self.yourchoice = QLineEdit()
        label_botschoice = QLabel("Bot's Choice")
        self.botschoice = QLineEdit()

        label_yourchoice.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.yourchoice.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.yourchoice.setFixedHeight(60)
        label_botschoice.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botschoice.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.botschoice.setFixedHeight(60)

        self.check_result_button = QPushButton("Check Result")
        self.play_again_button = QPushButton("Play Again")
        self.back_button = QPushButton("Back")

        self.check_result_button.setFixedWidth(400)
        self.check_result_button.setFixedHeight(60)
        self.play_again_button.setFixedWidth(200)
        self.play_again_button.setFixedHeight(45)
        self.back_button.setFixedWidth(200)
        self.back_button.setFixedHeight(45)

        layout.addWidget(title_line, 0, 0, 1, 2)
        layout.addWidget(instruction, 1, 0, 1, 2)
        layout.addWidget(label_yourchoice, 2, 0, 1, 1)
        layout.addWidget(label_botschoice, 2, 1, 1, 1)
        layout.addWidget(self.yourchoice, 3, 0, 1, 1)
        layout.addWidget(self.botschoice, 3, 1, 1, 1)
        layout.addWidget(self.check_result_button, 4, 0, 1, 2, alignment = Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.back_button, 5, 0, alignment = Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.play_again_button, 5, 1, alignment = Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.botschoice.setEnabled(False)
        self.check_result_button.setEnabled(False)
        self.play_again_button.setEnabled(False)
        self.yourchoice.textChanged.connect(self.check_input_text)
        self.check_result_button.clicked.connect(self.calculate_match_result)
        self.play_again_button.clicked.connect(self.play_again_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

    def check_input_text(self: 'RPSGameUI') -> None:
        input_text = self.yourchoice.text().strip()
        input_chars = input_text.split(' ')
        if input_chars:
            self.check_result_button.setEnabled(True)

    def calculate_match_result(self: 'RPSGameUI') -> None:
        choices = {'r': "Rock", 'p': "Paper", 's': "Scissors"}
        input_text = self.yourchoice.text().strip().lower()
        if input_text in choices:
            yourchoice = input_text
            botschoice = choice(list(choices.keys()))
            self.yourchoice.setText(str(choices[yourchoice]))
            self.botschoice.setText(str(choices[botschoice]))
            self.yourchoice.setEnabled(False)
            self.check_result_button.setEnabled(False)
            sleep(0.5)
            if yourchoice == botschoice:
                QMessageBox.information(self, "Result", "Congratulations to both sides for the draw!")
            elif (yourchoice == 'r' and botschoice == 'p') or \
                (yourchoice == 'p' and botschoice == 's') or \
                    (yourchoice == 's' and botschoice == 'r'):
                QMessageBox.critical(self, "Result", "I'm sorry you lost this time." + ' ' + \
                                     "I hope you can win next time... - Aaron the Programmer")
            else:
                QMessageBox.information(self, "Result", "Congratulations on winning the game!" + ' ' + \
                                        "Would you like to give it a thumbs up? - Aaron the Programmer")
            self.play_again_button.setEnabled(True)
        else:
            self.yourchoice.setEnabled(False)
            QMessageBox.warning(self, "Warning", "This is not a valid choice...")            
            self.yourchoice.clear()
            self.yourchoice.setEnabled(True)

    def play_again_button_clicked(self: 'RPSGameUI') -> None:
        self.yourchoice.clear()
        self.botschoice.clear()
        self.yourchoice.setEnabled(True)
        self.check_result_button.setEnabled(True)
        self.play_again_button.setEnabled(False)

    def back_button_clicked(self: 'RPSGameUI') -> None:
        self.hide()
        self.parent.show()
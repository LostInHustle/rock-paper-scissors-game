from rps_game_ui import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class RPSLoginUI(QMainWindow):
    def __init__(self: 'RPSLoginUI') -> None:
        super().__init__()
        self.child = None
        self.setFixedHeight(200)
        self.setFixedWidth(300)
        self.setWindowTitle("Rock-Paper-Scissors Login")
        layout = QGridLayout()

        title_line = QLabel("<h2>Login Page</h2>")
        title_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_username = QLabel("Username")
        self.username = QLineEdit()
        label_password = QLabel("Password")
        self.password = QLineEdit()

        label_username.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.username.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_button = QPushButton("Login")
        self.quit_button = QPushButton("Quit")
        self.login_button.setFixedWidth(120)
        self.quit_button.setFixedWidth(120)

        layout.addWidget(title_line, 0, 0, 1, 2)
        layout.addWidget(label_username, 1, 0, 1, 1)
        layout.addWidget(self.username, 1, 1, 1, 1)
        layout.addWidget(label_password, 2, 0, 1, 1)
        layout.addWidget(self.password, 2, 1, 1, 1)
        layout.addWidget(self.quit_button, 3, 0, alignment = Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.login_button, 3, 1, alignment = Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.login_button.clicked.connect(self.login_button_clicked)
        self.quit_button.clicked.connect(lambda: QApplication.quit())
    
    def login_button_clicked(self: 'RPSLoginUI') -> None:
        username = self.username.text().strip()
        password = self.password.text().strip()
        self.username.clear()
        self.password.clear()

        if username and password:
            self.hide()
            self.child.show()
        else:
            QMessageBox.warning(self, 'Failure', "Wrong username or password...")
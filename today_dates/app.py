from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)
import sys
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.today = (datetime.now()).strftime("%a, %Y-%m-%d")

        self.button_is_checked = True

        self.setWindowTitle("Date Application")
        self.button = QPushButton("What is today's date?")
        self.button.clicked.connect(self.date_button)

        self.setCentralWidget(self.button)

    def date_button(self):
        self.button.setText(self.today)
        print(self.today)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
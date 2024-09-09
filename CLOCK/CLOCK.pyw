from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
import time
import sys

class TransparentClock(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set up the label
        self.label = QLabel(self)
        self.label.setFont(QFont('Arial', 48))  
        self.label.setStyleSheet("color: purple;")  
        self.label.setAttribute(Qt.WA_TranslucentBackground)

        # Set up the button
        self.close_button = QPushButton('Close', self)
        self.close_button.clicked.connect(self.close_application)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.close_button)
        layout.setAlignment(Qt.AlignCenter) 
        self.setLayout(layout)

        self.resize(320, 150)  # Increase height to fit the button

        # Position the clock in the bottom-right corner of the screen
        screen_geometry = QApplication.desktop().availableGeometry()  
        self.setGeometry(screen_geometry.width() - 320, screen_geometry.height() - 150, 320, 150)

        # Set up the timer for updating the clock
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_clock)
        self.update_timer.start(1000)

        self.update_clock()  

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S') 
        self.label.setText(current_time) 

    def close_application(self):
        self.close()  # This will close the application

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = TransparentClock() 
    clock.show() 

    sys.exit(app.exec_())  

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Full-Screen Background Image")
         # Set the window to full screen

        # Apply CSS to set the background image
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('sam.jpg');
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }
        """)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

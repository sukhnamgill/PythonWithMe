import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QFileDialog, QListWidget
)
from PyQt5.QtCore import Qt
import os

class DJMusicSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DJ Music Selector")
        self.setGeometry(200, 200, 400, 300)
        
        self.layout = QVBoxLayout()

        # Button to open file dialog
        self.button = QPushButton("Select Music Files")
        self.button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.button)

        # List to display selected files
        self.music_list = QListWidget()
        self.layout.addWidget(self.music_list)

        self.setLayout(self.layout)

    def open_file_dialog(self):
        # Select multiple music files
        files,_ = QFileDialog.getOpenFileNames(
            self,
            "Select Music Files",
            "",
            "Audio Files (*.mp3 *.wav *.ogg *.flac);;All Files (*)"
        )
        if files:
            self.music_list.clear()
            for file_path in files:
                file_name = os.path.basename(file_path)
                self.music_list.addItem(file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DJMusicSelector()
    window.show()
    sys.exit(app.exec_())

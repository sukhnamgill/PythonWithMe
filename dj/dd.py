import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


class DragLabel(QLabel):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.setStyleSheet("background-color: lightblue; padding: 10px;")
        self.setFixedSize(100, 40)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setText(self.text())
            drag.setMimeData(mime_data)
            drag.exec_(Qt.CopyAction)


class DropLabel(QLabel):
    def __init__(self, parent):
        super().__init__("Drop Here", parent)
        self.setStyleSheet("background-color: lightgray; padding: 10px;")
        self.setFixedSize(150, 40)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        text = event.mimeData().text()
        self.setText("Dropped: " + text)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Drag & Drop")
        self.setGeometry(300, 300, 300, 150)

        self.drag_label = DragLabel("🎵 Drag me", self)
        self.drag_label.move(30, 30)

        self.drop_label = DropLabel(self)
        self.drop_label.move(30, 90)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

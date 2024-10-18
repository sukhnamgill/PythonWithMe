from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def main():
    app=QApplication(sys.argv)
    win=QWidget()
    lab_2=QLabel(win)
    lab_2.setText("hello")
    lab_2.setAlignment(Qt.AlignCenter)
    lab_1=QLabel(win)
    lab_1.setPixmap(QPixmap("my.jpg"))
    win.setGeometry(15,25,550,550)
    








    win.show()

    sys.exit(app.exec_())
def hovered():
    print("link is hovered")
if __name__=="__main__":
    main()
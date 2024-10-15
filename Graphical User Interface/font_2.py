from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
def win():
    app=QApplication(sys.argv)
    w=QWidget()
    lab=QLabel(w)
    w.setGeometry(200,200,200,250)
    
    lab.setText("Programe 2")
    lab.move(20,30)
    font=QFont()
    font.setFamily("Arial")
    font.setBold(2)
    font.setPointSize(16)
    lab.setFont(font)
    w.setWindowTitle("programe 2")
    w.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    win()
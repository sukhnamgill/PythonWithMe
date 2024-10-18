from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
def win():
    app=QApplication(sys.argv)
    w=QWidget()
    ac=QLabel(w)
    w.setGeometry(20,30,550,550)
    btn1=QPushButton("button 1")
    btn2=QPushButton("button 2")
    btn1.styleSheet()
    # ac.setText("hello world")
    # ac.move(50,50)
    lo=QHBoxLayout()
    lo.addWidget(btn1)
    ac.setText("iam text")
    # lo.addStretch()
    lo.addWidget(ac)

    w.setLayout(lo)

    
    # btn1.setText("Button 1")
    # btn2.setText("Button 2")
    btn1.move(110,10)
    # btn2.move(10,80)


    
    w.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    win()
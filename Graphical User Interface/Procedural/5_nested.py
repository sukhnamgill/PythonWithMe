from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
def window():
    app=QApplication(sys.argv)
    win=QWidget()
    #add label
    lab=QLabel(win)
    lab.setText("Hello sukhnam")
    win.setGeometry(20,20,520,520)
    b1=QPushButton("button1")
    b2=QPushButton("button2")
    b6=QPushButton("new added ")
    
    # vertical box layout
    bv=QHBoxLayout()
    bv.addWidget(b1)
    bv.addStretch()
    bv.addWidget(b2)
    bv.addStretch()
    bv.addWidget(b6)
    
   
    b3=QPushButton("button3")
    b4=QPushButton("button4")

    #horizental box layout
    bh=QVBoxLayout()
    b5=QPushButton("new_button")
    bh.addWidget(b3)
    bh.addStretch()
    bh.addWidget(b4)
    bh.addStretch()
    bh.addWidget(b5)
    # bv.addStretch()
 #main box layout
    
    bh.addLayout(bv)
    
    win.setLayout(bh)

    win.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    window()
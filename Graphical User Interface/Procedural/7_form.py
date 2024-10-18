from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
# How to make form in Python PYQT-5
def main():
    app=QApplication(sys.argv)
    win=QWidget()
    lab=QLabel(win)
    win.resize(350,260)
    # lab.move(20,20)
    #NAME
    lab.setText("Enter name:")
    box=QFormLayout(win)
    el=QLineEdit()
    box.addRow(lab,el)
    #ADDRESS
    #input lines
    lab2=QLabel(win)
    lab2.setText("arrdeass")
    el2=QTextEdit()
    el3=QLineEdit()

    vl=QVBoxLayout()
    vl.addWidget(el2)
    vl.addWidget(el3)
    box.addRow(lab2,vl)
    
    
    #Sexual indentity
    lab3=QLabel(win)
    lab3.setText("Gender")
    #horizental box
  
    hb=QHBoxLayout()
    cbtn1=QRadioButton("Boy")
    cbtn2=QRadioButton("Girl")
    cbtn3=

    
    hb.addWidget(cbtn1)
    hb.addWidget(cbtn2)
    hb.addWidget(cbtn3)
    box.addRow(lab3,hb)
    box.addRow(QPushButton("SUBMIT"),QPushButton("CANCEL"))



    




    win.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
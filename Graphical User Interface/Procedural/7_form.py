from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
# How to bluemake form in Python PYQT-5
def main():
    app=QApplication(sys.argv)
    win=QWidget()
    lab=QLabel(win)
    win.resize(350,260)
    win.setStyleSheet("QWidget{background-color:rgb(240,234,192);color:black;font-family: Lucida Console, Courier New, monospace}")
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
    # bel=el2,el3
    el3.setStyleSheet("QTextEdit{background-color:yellow;border:2px solid red}")

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
    cbtn3=QRadioButton("Other")
    cbtn1.setStyleSheet("QRadioButton { color: white; background-color: black ;border-radius:5px; padding:5px}")
    cbtn2.setStyleSheet("QRadioButton { color: white; background-color: black ;border-radius:5px; padding:5px}")
    cbtn3.setStyleSheet("QRadioButton { color: white; background-color: black ;border-radius:5px;padding:5px}")
    btn1=QPushButton("SUBMIT")
    btn2=QPushButton("CANCEL")
    btn1.setStyleSheet("""QPushButton{border:2px solid black;
    padding:10px;
    border-radius:10px}
    
    """)
    
    hb.addWidget(cbtn1)
    hb.addWidget(cbtn2)
    hb.addWidget(cbtn3)
    box.addRow(lab3,hb)
    box.addRow(btn1,btn2)

    win.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
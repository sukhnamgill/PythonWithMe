from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

def function_1():
    lab.setText("print button is clicked")
   

    

app =QApplication(sys.argv)
    # w=QWidget()
w=QDialog()
lab=QLabel(w)
lab.setText("Iam programe three")
lab.move(20,20)
b=QPushButton(w)
b.setText("Print")
b.move(20,30)
   
b.clicked.connect(function_1)
w.setGeometry(200,200,200,200)
w.setWindowTitle("button programe")
   
w.show()





sys.exit(app.exec_())

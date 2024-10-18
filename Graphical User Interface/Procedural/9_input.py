from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
def main():
    app=QApplication(sys.argv)
    win=QWidget()
    lb=QLabel(win)
    win.setGeometry(200,200,500,250)
    win.setWindowTitle("sukhnam")
     
    # lb.setText("iam artist 19")
    # font=QFont()
    # font.setPointSize(16)
    # win.setFont(lb)

    w1=QLineEdit()
    w1.setValidator(QIntValidator())
    w1.setMaxLength(4)
    w1.setFont(QFont("Arial",16))
    box=QFormLayout(win)
    box.addRow("int only",w1)

    w2=QLineEdit()
    w2.setValidator(QDoubleValidator(0.99,99.99,2))
    box.addRow("double only",w2)

    w3=QLineEdit()
    w3.setInputMask("+99_9999999999")
    box.addRow("Phone-number",w3)
    w4=QLineEdit()
    w4.setEchoMode(QLineEdit.Password)
    box.addRow("password",w4)
    # w5=QLineEdit()
    # w5.textChanged.connect(changed)
    # box.addRow("text cahnged",w5)
    w6=QLineEdit("hello")
    w6.setReadOnly(True)
    box.addRow("not chanageble",w6)
    w4.editingFinished.connect(done)






    # win.setLayout(box)
    win.show()
    sys.exit(app.exec_())
def done():
    print("text is done !!")
if __name__=='__main__':
    main()
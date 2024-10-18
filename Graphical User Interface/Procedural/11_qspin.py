from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
def main():
    def run():
        s=(str(qs.value()))
        lab.setText(s)
        lab.move(50,50)
        font=QFont()
        font.setFamily("Ariel")
        font.setPointSize(int(s))
        win.setFont(font)
    app=QApplication(sys.argv)
    win=QWidget()
    lab=QLabel(win)
    # lab.setText("hello world")
    qs=QSpinBox()
    qs.setMaximum(950)
    qs.valueChanged.connect(run)
    box=QFormLayout()
    box.addRow("select value",qs)
    
    win.setLayout(box)



    win.show()
    sys.exit(app.exec_())
    
    
    
if __name__=="__main__":
    main()

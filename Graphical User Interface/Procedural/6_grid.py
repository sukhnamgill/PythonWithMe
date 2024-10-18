from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
def window():
    app=QApplication(sys.argv)
    win=QWidget()
    win.resize(200,200)
    lab=QLabel(win)
    grid=QGridLayout()
    # lab.setText("hello")
    for i in range(5):
        for j in range(5):
            grid.addWidget(QPushButton("button1"),i,j)
    grid.addWidget(QLabel("ima label"),6,6,10,20)
    win.setLayout(grid)        
    win.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    window()
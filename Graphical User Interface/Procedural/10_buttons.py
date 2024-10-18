from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
def main():
    app=QApplication(sys.argv)
    win=QWidget()
    # lab=QLabel(win)
    # lab.setText("ima artist 19")
    b1=QPushButton()
    box=QFormLayout(win)
    b2=QPushButton("boys")
    b2.setEnabled(False)
    b1.setIcon(QIcon(QPixmap("my.jpg")))
    b1.setIconSize(QSize(200,25))
    box.addRow("button",b1)
    box.addRow("disable button",b2)

    cb=QComboBox()
    cb.addItems(["javascript", "c","pyhton"])
    box.addRow("list",cb)
    win.show()
    sys.exit(app.exec_())
    
if __name__=="__main__":
    main()


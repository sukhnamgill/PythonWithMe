from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
def main():
    app=QApplication(sys.argv)
    win=QWidget()
    lab=QLabel(win)
    lab.setText("iam text")
    def run():
        value=sl.value()
        print("value changed",value)
        font=QFont('arial',value)
        win.setFont(font)

    sl=QSlider(Qt.Horizontal)
    sl.valueChanged.connect(run)
    # sl.setMinimum(10)
    # sl.setMaximum(50)
    # sl.setSingleStep(5)
    win.setWindowIcon(QIcon("my.jpg"))
    box=QVBoxLayout()
    box.addWidget(sl)
    box.stretch(1)
    box.addWidget(lab)
    win.setLayout(box)
    

    win.show()
    sys.exit(app.exec_())
    
if __name__ =='__main__':
    main()
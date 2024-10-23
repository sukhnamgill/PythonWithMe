from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class Esy(QWidget):
    def __init__(self):
        super(Esy,self).__init__()
        self.setGeometry(5,30,500,600)
        bot=QFrame()
        boxm=QFormLayout(bot)
        boxm.addRow("Enter name",QLineEdit())

        bot.setFrameShape(QFrame.StyledPanel)
        lab=QLabel("Name SUkhan sinfh g")

        top=QFrame()
        top.setFrameShape(QFrame.StyledPanel)
        #an-other
        bottom=QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        box=QVBoxLayout(self)
        box.addWidget(bot)
        box.addWidget(top)
        
       
        # box.addWidget(bottom)

        # bot.setStyleSheet("QFrame{background-color:red}")
        # top.setStyleSheet("QFrame{background-color:gray}")
        # bottom.setStyleSheet("QFrame{background-color:pink}")

        split=QSplitter(Qt.Horizontal)
        split.addWidget(bot)
        split.addWidget(top)
        split.setSizes([200,300])
        box.addWidget(split)
        split2=QSplitter(Qt.Vertical)
        split2.addWidget(bottom)
        split2.addWidget(QLabel("iam sukhnam"))
        box.addWidget(split2)
        # split.setSizes([200,300])
        # split2=QSplitter(Qt.Vertical)
        # split2.addWidget(split)
        # split2.addWidget(QLabel("hello"))
        # box.addWidget(split2)
        # QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        # add=QFrame(self)
        # boxh=QHBoxLayout(add)
        # boxh.addWidget(QLabel("iam fien"))
        # add.setFrameShape(QFrame.StyledPanel)



def main():
    app=QApplication(sys.argv)
    win=Esy()
    win.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
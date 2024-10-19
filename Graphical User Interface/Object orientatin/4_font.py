from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class Font(QWidget):
    def __init__(self,parent=None):
        super(Font,self).__init__(parent)
        lab=QLabel("hello iam finr",self)
        lab.setFixedWidth(1300)
        lab.setFixedHeight(500)

        #button for font
        b1=QPushButton("Select the font",self)
        b1.clicked.connect(self.chfont)
        b1.move(50,50)
        #set geometery
        self.setGeometry(20,20,500,500)

    def chfont(self):
        font,ok=QFontDialog.getFont(self)
        if(ok):
            self.setFont(font)


def main():
    app=QApplication(sys.argv)
    win=Font()
    win.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
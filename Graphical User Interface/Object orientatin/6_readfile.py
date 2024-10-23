from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Read(QWidget):
    def __init__(self,parent=None):
        super(Read,self).__init__(parent)
        self.setWindowTitle("Read Text")
        self.setGeometry(0,25,600,250)
        # Button and its calling function
        self.btn=QPushButton("Open File",self)
        self.btn.clicked.connect(self.open_file)

        # make Text 
        self.text_area=QTextEdit(self)

        # vertical box 
        vrti_box=QVBoxLayout(self)
        vrti_box.addWidget(self.btn)
        # vrti_box.addStretch()
        vrti_box.addWidget(self.text_area)
        vrti_box.addStretch()
    #Function To Open File
    def open_file(self):
        fl=QFileDialog(self)
        file_details=fl.getOpenFileName(self,"helo","d:\\","*.txt")
        print(file_details)
        f=open(file_details[0],'r')
        s=f.read()
        print(s)
        self.text_area.setText(s)



def main():
    app=QApplication(sys.argv)
    win=Read()
    win.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()



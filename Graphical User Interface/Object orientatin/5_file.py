from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class File(QWidget):
    def __init__(self,parent=None):
        super(File,self).__init__(parent)
        #add button
        btn=QPushButton("open File",self)
        btn.clicked.connect(self.file_open)
        self.lab=QLabel(self)
        #set picture
        
        
    # declare function 
    def file_open(self):
        
        file=QFileDialog.getOpenFileName(self,"file open",'d:\\',"*.jpg")
        QMessageBox.information(self,"messaage",f" You are selected {file}")
        self.lab.setPixmap(QPixmap(file[0]))
        self.lab.setFixedHeight(500)
        self.lab.setFixedWidth(500)

        print(file)
    


def main():
    app=QApplication(sys.argv)
    win=File()
    win.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()






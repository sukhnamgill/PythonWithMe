from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Es(QWidget):
    def __init__(self):
        super(Es,self).__init__()
        #set title and geometry
        self.setWindowTitle("Stack details")
        self.setGeometry(0,50,600,600)
        #add qwidgets
        self.w1=QWidget()
        self.w2=QWidget()
        self.w3=QWidget()

        # add QStackedWidget
        self.st=QStackedWidget(self)
        self.st.addWidget(self.w1)
        self.st.addWidget(self.w2)
        self.st.addWidget(self.w3)

        #add lists box
        self.lis=QListWidget(self)
        self.lis.insertItem(0,"Name")
        self.lis.insertItem(1,"Class")
        self.lis.insertItem(2,"Collage")
         # Connection function
        
        self.lis.currentRowChanged.connect(self.change)
        
        # add layout
        box=QHBoxLayout(self)
        box.addWidget(self.lis)
        box.addWidget(self.st)

       
        # calling functons 
        self.fun1()
        self.fun2()
        self.fun3()

        #define functions
    def fun1(self):
        form=QFormLayout(self.w1)
        form.addRow(QLabel("name"),QLineEdit())
    def fun2(self):
        form=QFormLayout(self.w2)
        form.addRow(QLabel("Class"),QLineEdit())
    def fun3(self):
        form=QFormLayout(self.w3)
        form.addRow(QLabel("College"),QLineEdit())
    #change function
    def change(self,i):
        print(f"value changed {i}")
        n=self.st.setCurrentIndex(i)
      





def main():
    app=QApplication(sys.argv)
    win=Es()
    win.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()

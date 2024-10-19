from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Window(QWidget):
    def __init__(self,Parent=None):
        super(Window,self).__init__(Parent)
        self.setGeometry(50,50,250,100)
        #buttons
        btn1=QPushButton("selct language")
        btn2=QPushButton("age")
        btn3=QPushButton("name")
        #button.clicked(calling functions)
        btn1.clicked.connect(self.getval)
        btn2.clicked.connect(self.age)
        btn3.clicked.connect(self.name)
        #Input lines
        self.l1=QLineEdit()
        self.l2=QLineEdit()
        self.l3=QLineEdit()
        # self.l1.setText()
        #Binding in the Form
        form=QFormLayout(self)
        form.addRow(btn1,self.l1)
        form.addRow(btn2,self.l2)
        form.addRow(btn3,self.l3)

        #defining functions
    def getval(self):
        print("Iam get val")
        item=["Apple","Samsung","Asus","OLG"]
        item,ok=QInputDialog.getItem(self,"Select Compnay","Names",item,0,False)
        if ok:
            self.l1.setText(item)


    def age(self):
        num,ok=QInputDialog.getInt(self,"Select Ram","Memory",False)
        if(ok):
            self.l2.setText(str(num))
        
    def name(self):
        name,ok=QInputDialog.getText(self,"enter name","name",False)
        if(ok):
            self.l3.setText(name)
        # print("Iam name")

        



#main function declaring
def main():
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Health(QTabWidget):
    def __init__(self,parent=None):
        super(Health,self).__init__(parent)
        self.setGeometry(50,50,1000,500)
        font=QFont("arial",25)
        self.setFont(font)

        #tab bar
        self.tab_1=QWidget()
        self.tab_2=QWidget()
        self.tab_3=QWidget()
       
        self.addTab(self.tab_1,"Calory Counter")
        self.addTab(self.tab_2,"Exercises")
        self.addTab(self.tab_3,"Diet")
        
        #calling functions
        self.ui_1()
        self.ui_2()
        self.ui_3()

    def ui_1(self):
        form=QFormLayout(self.tab_1)
        form.maximumSize()
        
        self.txt=QSpinBox()
        form.addRow("AGE",self.txt)
        self.txt_2=QSpinBox()
        form.addRow("WEIGHT",self.txt_2)
        self.txt_3=QSpinBox()
        form.addRow("HEIGHT ",self.txt_3)
        self.boy=QRadioButton("Boy")
        self.girl=QRadioButton("Girl")
        box=QHBoxLayout()
        
        box.addWidget(self.girl)
        box.addWidget(self.boy)
        form.addRow("SEX       ",box)
    def ui_2(self):
        self.st=QStackedWidget()
        self.stack_1=QWidget()
        self.stack_2=QWidget()
        self.stack_3=QWidget()

        self.st.addWidget(self.stack_1)
        self.st.addWidget(self.stack_2)
        self.st.addWidget(self.stack_3)

        self.li=QListWidget()
        self.li.insertItem(1,"hello")
        self.li.insertItem(2,"bye bye")
        self.li.currentRowChanged.connect(self.display)

    # calling functions
        box=QHBoxLayout(self.tab_2)
        box.addWidget(self.st)
        box.addWidget(self.li)

        

        self.option_1()
        self.option_2()
        self.option_3()

        
    def ui_3(self):
        # Qwidgets 
        self.st1=QWidget()
        self.st2=QWidget()
        self.st3=QWidget()
        #stack add widget vitamin
        self.stack=QStackedWidget()
        self.stack.addWidget(self.st1)
        self.stack.addWidget(self.st2)
        self.stack.addWidget(self.st3)
        # list insert Vitamin
        self.lis=QListWidget()
        self.lis.insertItem(1,"vitamin 1")
        self.lis.insertItem(2,"vitamin2")
        self.lis.insertItem(3,"vitamin 3")
        self.lis.currentRowChanged.connect(self.check)

        #box layout of vitamin
        box=QHBoxLayout(self.tab_3)
        box.addWidget(self.lis)
        box.addWidget(self.stack)

        self.fun1()
        self.fun2()
        self.fun3()
        
    def fun1(self):
        s=QPushButton(self.st1)
        s.setText("iam butoon")
    def fun2(self):
        lab=QLabel(self.st2)
        lab.setPixmap(QPixmap("my2.jpg"))
    def fun3(self):
        pass
    def display(self,i):
        self.st.setCurrentIndex(i)
    def check(self,i):
        print("value changed of vitamin",i)
        self.stack.setCurrentIndex(i)


    #stack of ui 2
    def option_1(self):
        print("optin is clicked")
        n=QPushButton(self.stack_1)
        n.setText("iam sack button")
        # n.move(0,150)
    def option_2(self):
        lab=QLabel(self.stack_2)
        lab.setPixmap(QPixmap('my.jpg'))

    def option_3(self):
        pass




def main():
    app=QApplication(sys.argv)
    win=Health()
    win.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
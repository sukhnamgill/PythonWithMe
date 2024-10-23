from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class Tab(QTabWidget):
    def __init__(self,parent=None):
        super(Tab,self).__init__(parent)
        self.setWindowTitle("Tab Bar")
        self.setGeometry(0,25,500,300)
        # variable
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        
        #tab 
        self.addTab(self.tab1,"Bio")
        self.addTab(self.tab2,"class")
        self.addTab(self.tab3,"collage")

        self.fun_1()
        self.fun_2()
        self.fun_3()

    # declaring functions

    def fun_1(self):
        name=QLabel(" Enter Name")
        l1=QLineEdit()
        form=QFormLayout(self.tab1)
        
        form.addRow(name,l1)
        age=QLabel("Enter Age ")
        l2=QSpinBox()
        form.addRow(age,l2)
    def fun_2 (self):
        item=['bca','mca','btek']
        form=QFormLayout(self.tab2)
        
        lab=QLabel("Class")
        cm=QComboBox()
        cm.addItems([' Plain BCA','MCA','IBM AI DS BCA','Cyber Seq','Hotel Management'])
        form.addRow(lab,cm)
        
    def fun_3(self):
        btn=QPushButton("submit")
        btn2=QToolButton()
        btn3=QRadioButton("Ct university")
        box=QVBoxLayout(self.tab3)
        box.addWidget(btn3)
        # box.addWidget(btn2)
        box.addWidget(btn)



def main():
    app=QApplication(sys.argv)
    win=Tab()
    win.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
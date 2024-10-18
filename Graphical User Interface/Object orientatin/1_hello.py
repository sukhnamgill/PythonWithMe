import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Hello(QWidget):
    i=1
    
    def __init__(self,Parent=None):
        super(Hello,self).__init__(Parent)
        self.setGeometry(15,15,1200,600)
        self.lab=QLabel("Press next to Check my best friend",self)
        self.lab.setFixedWidth(1000)
        self.font=QFont("arial",25)
        self.setFont(self.font)
        self.lab.move(0,90)
        self.ui()
        self.lay()
        self.lab.setStyleSheet("""
        {
        color: white;
        background-color: black;
        border: 2px solid black;
        
        }
        """)
    
    def ui(self):
        self.button=QPushButton("Next")
        self.button.clicked.connect(self.next1)
        self.buttonbac=QPushButton("back")
        self.buttonbac.clicked.connect(self.back)
        # self.buttonbac.move(250,0)
        self.sl=QSlider(self)
        self.sl.valueChanged.connect(self.changed1)
        self.sl.setMaximum(27)
        self.sl.setMinimum(11)
        self.sl.move(150,300)

    def lay(self):
        self.box=QHBoxLayout(self)
        self.box.addWidget(self.button)
        self.box.stretch(1)
        self.box.addWidget(self.buttonbac)
        
        self.box.stretch(1)
        self.box.addWidget(self.sl)
        self.setLayout(self.box)

    def changed1(self):
        print("value change")
        value=self.sl.value()
        print(value)
        self.font=QFont("arial",value)
        self.setFont(self.font)
        

    def next1 (self):
        self.i=self.i+1
        self.hello()
        print(self.i)

    def back (self):
        self.i=self.i-1
        print(self.i)
        self.hello()

    def hello(self):
        
        if(self.i==5):
            self.button.setEnabled(False)
            self.lab.setText("jasmeet is my best friend")
        elif(self.i==4):
            self.button.setEnabled(True)
            self.lab.setText("Harjeet is my best frined")

        
        # elif(self.i>1):
            
        elif(self.i==2):
            self.lab.setText("Arshpreet is my best friend")
            self.buttonbac.setEnabled(False)
            
        elif (self.i==3):
            self.lab.setText("Gurkirat is my best friend")
            self.buttonbac.setEnabled(True)

        else:
            pass
            
    



def main():
    app=QApplication(sys.argv)
    win=Hello()
    win.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
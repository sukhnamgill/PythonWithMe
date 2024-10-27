from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Health(QTabWidget):
    def __init__(self,parent=None):
        super(Health,self).__init__(parent)
        self.setGeometry(50,50,1000,500)
        font=QFont("arial",20)
        self.setWindowIcon(QIcon('health.png'))
        self.setWindowTitle("Health")
        
       
        # self.setStyleSheet("""QTabWidget{
        # background-color:black
        # }""")

        #tab bar
        self.tab_1=QWidget()
        self.tab_2=QWidget()
        self.tab_3=QWidget()
        self.tab_1.setStyleSheet("""QWidget{
        background-color:white;
        font-family: -apple-system;
        color:black;
        font-weight:900;
        font-size:20px;
        border:1px solid black;
        border-radius:10px;
        padding:10px}""")
        # self.setStyleSheet("""QWidget{
        # background:black;
        # color:white;
        # font-weight:900;
        # background-repeat:no-repeat;
        # opacity: 0.2;

        # font-size:20px;
        # border:1px solid white;
        # border-radius:10px;
        # padding:10px}""")
        self.setStyleSheet("""QTabWidget{
        background-color:white}
        QTabBar::tab{
        color:#A2AAAD;
        background-color:white;
        border-radius:4px;
        margin:5px;
        padding:5px}
        QTabBar::tab:hover{
        border:1px solid #A2AAAD;}
        QTabBar::tab:selected{
        background-color:#A2AAAD;
        color:white;}""")
       
       
        self.addTab(self.tab_1,"Calory Counter")
        self.addTab(self.tab_2,"Exercises")
        self.addTab(self.tab_3,"Diet")
        
        
        #calling functions
        self.ui_1()
        self.ui_2()
        self.ui_3()
        self.setFont(font)
# this is  first 
    def ui_1(self):
        
        

        form=QFormLayout(self.tab_1)
        lab=QLabel(self.tab_1)
        buton=QPushButton(self.tab_1)
        buton.setIcon(QIcon('g.png'))
        buton.setIconSize(QSize(201,201))
        
      
        
        lab.setText("Welcome In Calory-Counter ")
        form.addRow(buton,lab)
        lab.setStyleSheet("""QLabel{
        background-color:white;
        color:#0b6958;
        border:None;
        font-size:50px}""")
        buton.setStyleSheet("""QPushButton{border:None}""")
        # form.maximumSize()
        
        self.txt=QSpinBox()
        
        form.addRow("AGE",self.txt)
        self.txt_2=QSpinBox()
        form.addRow("WEIGHT",self.txt_2)
        self.txt_3=QSpinBox()
        form.addRow("HEIGHT ",self.txt_3)
        self.boy=QRadioButton("Boy")
        self.girl=QRadioButton("Girl")
       
        #classes of spinbox to stylesheet
        
        self.boy.setStyleSheet("""QRadioButton{
                                 background-color:#9db6fc;
                               border:1px silid #9db6fc;
                               color:white;}""")
        box=QHBoxLayout()
        self.girl.setStyleSheet("""QRadioButton{
                                 background-color:#f5abef;
                                border:1px solid #f5abef;
                               color:white;}""")
        calculate=QPushButton("calculate")
        reset=QPushButton("reset")
        calculate.clicked.connect(self.calculate)
        reset.clicked.connect(self.reset)
        box2=QHBoxLayout()
        box.addWidget(self.girl)
        box.addWidget(self.boy)
        form.addRow("SEX       ",box)

        box2.addWidget(reset)
        box2.addWidget(calculate)
        form.addRow(box2)
    def calculate(self,i):
        print("calculate button is pressed",i)
        new=QDialog()
        new.setWindowTitle("Result")
        new.exec_()

        n=self.txt_2.value()
        print(n)
    def reset(self):
        print("reset")
        self.txt_3.setValue(0)
    def ui_2(self):
        self.st=QStackedWidget()
        self.stack_1=QWidget()
        self.stack_2=QWidget()
        self.stack_3=QWidget()
        self.stack_4=QWidget()

        self.st.addWidget(self.stack_1)
        self.st.addWidget(self.stack_2)
        self.st.addWidget(self.stack_3)
        self.st.addWidget(self.stack_4)

        self.li=QListWidget()
        self.li.insertItem(1,"Chest")
        self.li.insertItem(2,"Leg")
        self.li.insertItem(3,"Bieciep")
        self.li.insertItem(4,"triceip")
        self.li.currentRowChanged.connect(self.display)

    # calling functions
        box=QHBoxLayout(self.tab_2)
        box.addWidget(self.li)
        box.addWidget(self.st)
        self.li.setFixedWidth(130)
        self.li.setStyleSheet("""QListWidget{
        background-color:white;
        padding:5px;
        font-size:20px;
        color:#A2AAAD;
        border-radius:9px;
        
        }
        QListWidget::item:hover {
        background-color:white ; 
        color:#A2AAAD;
        border:1px solid #A2AAAD;
        border-radius:4px;
    }
    QListWidget::item:selected{
    background-color:#A2AAAD;
    color:white;
    
    border-radius:4px;
    
    }""")

        

        self.option_1()
        self.option_2()
        self.option_3()
        self.option_4()

        
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
        lab.setText("helo")
        self.mov=QMovie("fi.gif")
        lab.setMovie(self.mov)
        self.mov.start()
    def fun3(self):
        pass
    
    def display(self,i):
        self.st.setCurrentIndex(i)
    def check(self,i):
        print("value changed of vitamin",i)
        self.stack.setCurrentIndex(i)


    #stack of ui 2
    def option_1(self):
        lab1=QLabel(self.stack_1)
        mov1=QMovie('fi.gif')
        mov1.setScaledSize(QSize(300,300))
        lab1.setMovie(mov1)
        mov1.start()

        lab=QLabel(self.stack_1)
        mov=QMovie('fi.gif')
        mov.setScaledSize(QSize(300,300))
        lab.setMovie(mov)
        mov.start()

        lab2=QLabel(self.stack_1)
        mov2=QMovie('fi.gif')
        mov2.setScaledSize(QSize(300,300))
        lab2.setMovie(mov2)
        mov2.start()

        lab3=QLabel(self.stack_1)
        mov3=QMovie('fi.gif')
        mov3.setScaledSize(QSize(300,300))
        lab3.setMovie(mov3)
        mov3.start()
        #pack in to layout 
        grid=QGridLayout(self.stack_1)
        grid.addWidget(lab,0,0)
        grid.addWidget(lab1,0,1)
        grid.addWidget(lab2,1,0)
        grid.addWidget(lab3,1,1)
        
    def option_2(self):
        # lab=QLabel(self.stack_2)
        # mov=QMovie('fi.gif')
        # lab.setMovie(mov)
        # mov.start()
        pass

    def option_3(self):
        # lab=QLabel(self.stack_3)
        # mov=QMovie('fi.gif')
        # lab.setMovie(mov)
        # mov.start()
        pass
        
    def option_4(self):
        # lab=QLabel(self.stack_4)
        # mov=QMovie('fi.gif')
        # lab.setMovie(mov)
        # mov.start()
        pass



def main():
    app=QApplication(sys.argv)
    win=Health() 
   
    win.show()
   
    
    
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
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
        self.txt.setRange(10,80)
        form.addRow("AGE(Years)",self.txt)
        self.txt_2=QLineEdit("25.250")
        
        self.txt_2.setValidator(QDoubleValidator(0.99,99.99,3))
        # self.txt_2.
        
        form.addRow("WEIGHT (KG)",self.txt_2)
        self.txt_3=QSpinBox()
        self.txt_3.setRange(60,279)
        form.addRow("HEIGHT(CM) ",self.txt_3)
        
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
                               color:white;}
                                """)
        calculate=QPushButton("Calculate")
        self.boy.setChecked(True)
        reset=QPushButton("Reset")
        reset.setStyleSheet("""QPushButton{background-color:yellow;
                                color:black;
                                border:None;
                                border-radius:4px;}
                            QPushButton:hover{
                            background-color:red;}""")
        calculate.setStyleSheet("""QPushButton{background-color:green;
                                color:white;
                                border:None;
                                border-radius:4px;}
                                QPushButton:hover{
                            background-color:orange;}""")
        calculate.clicked.connect(self.calculate)
        reset.clicked.connect(self.reset)
        box2=QHBoxLayout()
        box.addWidget(self.girl)
        box.addWidget(self.boy)
        self.combo=QComboBox()
        self.combo.addItems(["Simple Exercise","Modrate Exercise","Hard Exercise"])
        form.addRow("Duty",self.combo)
        form.addRow("GENDER      ",box)

        box2.addWidget(reset)
        box2.addWidget(calculate)
        form.addRow(box2)
    def calculate(self,i):
        print("calculate button is pressed",i)
        

        age=self.txt.value()
        weight=self.txt_2.text()
        weight=float(weight)
        height=self.txt_3.value()
        gender_girl=self.girl.isChecked()
        gender_boy=self.boy.isChecked()
        combo=self.combo.currentText()
        men_bmr=88.362+(13.397*weight)+(4.799*height)-5.677*age
        women_bmr=447.593+(9.247*weight)+(3.098*height)-4.330*age

        #printing on the console for debuging
        print("age is ",age)
        print("weight is ",weight)
        print("height is ",height)
        print("girl",gender_girl)
        print("boy",gender_boy)
        print("combo is ",combo)
        if gender_girl==True:
            print("Girl Section Running..")
            
            if combo=='Simple Exercise':
                print("simple exercise..")
                self.kcal=women_bmr*1.375
            elif combo=='Modrate Exercise':
                print("moderate..")
                self.kcal=women_bmr*1.55
            else:
                print("hard exercise")
                self.kcal=women_bmr*1.75
        else:
            print("Boy Section Running..")
            if combo=='Simple Exercise':
                print("simple exercise..")
                self.kcal=men_bmr*1.375
            elif combo=='Modrate Exercise':
                print("moderate..")
                self.kcal=men_bmr*1.55
            else:
                print("hard exercise")
                self.kcal=men_bmr*1.75
        print(self.kcal)
        text_kcal=self.kcal
        
        text_kcal=str(text_kcal)

        #new window functon
        new=QDialog()
        new.setGeometry(50,50,400,200)
        new.setWindowTitle("Result")
        new.setStyleSheet("""QDialog{
                          background-color:black;
                          color:white;
                          }""")
        new.setFont(QFont("Arial",20))
        lab=QLabel("Calorie You Shoud To Take")
        lab.setStyleSheet("""QLabel{color:white;
                          font-size:25px;
                          font-family: -apple-system, -apple-system,  
                BlinkMacSystemFont, 'Segoe UI', Roboto,  
                Oxygen, Ubuntu, Cantarell, 'Open Sans',  
                'Helvetica Neue', sans-serif; }""")
        lab2=QLabel(new)
        lab2.setStyleSheet("""QLabel{color:white;
                           font-size:25px;
                           font-family: 'Courier New', Courier, monospace;}""")
        lab2.setText(text_kcal)
        box=QVBoxLayout(new)
        box.addWidget(lab)
        box.addWidget(lab2)

        new.exec_()
    def reset(self):
        print("reset")
        self.txt_3.setValue(60)
        self.txt_2.setText("50.250")
        self.txt.setValue(15)
        
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
        self.st4=QWidget()
        self.st5=QWidget()
        self.st6=QWidget()
        #stack add widget vitamin
        self.stack=QStackedWidget()
        self.stack.addWidget(self.st1)
        self.stack.addWidget(self.st2)
        self.stack.addWidget(self.st3)
        self.stack.addWidget(self.st4)
        self.stack.addWidget(self.st5)
        self.stack.addWidget(self.st6)
        # list insert Vitamin
        self.lis=QListWidget()
        self.lis.setFixedWidth(135)
        # self.lis.setStyleSheet("""QListWidget{background-color:white;
        #                        color:white;
        #                        border:None;
        #                        font-size:}""")
        self.lis.setStyleSheet("""QListWidget{
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
        self.lis.insertItem(1,"vitamin A")
        self.lis.insertItem(2,"vitamin B")
        self.lis.insertItem(3,"vitamin C")
        self.lis.insertItem(4,"vitamin D")
        self.lis.insertItem(5,"vitamin E")
        self.lis.insertItem(6,"vitamin K")
        self.lis.currentRowChanged.connect(self.check)

        #box layout of vitamin
        box=QHBoxLayout(self.tab_3)
        box.addWidget(self.lis)
        box.addWidget(self.stack)

        self.fun1()
        self.fun2()
        self.fun3()
        self.fun4()
        self.fun5()
        self.fun6()
        
        
    def fun1(self):
        lab=QLabel(self.st1)
        lab.setPixmap(QPixmap('sam.jpg'))
    def fun2(self):
        lab=QLabel(self.st2)
        lab.setPixmap(QPixmap('sam.jpg'))
    def fun3(self):
        lab=QLabel(self.st3)
        lab.setPixmap(QPixmap('sam.jpg'))
        
    def fun4(self):
        lab=QLabel(self.st4)
        lab.setPixmap(QPixmap('sam.jpg'))
    def fun5(self):
        lab=QLabel(self.st5)
        lab.setPixmap(QPixmap('sam.jpg'))
    def fun6(self):
        lab=QLabel(self.st6)
        lab.setPixmap(QPixmap('sam.jpg'))
    
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
        lab1=QLabel(self.stack_2)
        mov1=QMovie('fi.gif')
        mov1.setScaledSize(QSize(300,300))
        lab1.setMovie(mov1)
        mov1.start()

        lab=QLabel(self.stack_2)
        mov=QMovie('fi.gif')
        mov.setScaledSize(QSize(300,300))
        lab.setMovie(mov)
        mov.start()

        lab2=QLabel(self.stack_2)
        mov2=QMovie('fi.gif')
        mov2.setScaledSize(QSize(300,300))
        lab2.setMovie(mov2)
        mov2.start()

        lab3=QLabel(self.stack_2)
        mov3=QMovie('fi.gif')
        mov3.setScaledSize(QSize(300,300))
        lab3.setMovie(mov3)
        mov3.start()
        #pack in to layout 
        grid=QGridLayout(self.stack_2)
        grid.addWidget(lab,0,0)
        grid.addWidget(lab1,0,1)
        grid.addWidget(lab2,1,0)
        grid.addWidget(lab3,1,1)
        

    def option_3(self):
        lab1=QLabel(self.stack_3)
        mov1=QMovie('fi.gif')
        mov1.setScaledSize(QSize(300,300))
        lab1.setMovie(mov1)
        mov1.start()

        lab=QLabel(self.stack_3)
        mov=QMovie('fi.gif')
        mov.setScaledSize(QSize(300,300))
        lab.setMovie(mov)
        mov.start()

        lab2=QLabel(self.stack_3)
        mov2=QMovie('fi.gif')
        mov2.setScaledSize(QSize(300,300))
        lab2.setMovie(mov2)
        mov2.start()

        lab3=QLabel(self.stack_3)
        mov3=QMovie('fi.gif')
        mov3.setScaledSize(QSize(300,300))
        lab3.setMovie(mov3)
        mov3.start()
        #pack in to layout 
        grid=QGridLayout(self.stack_3)
        grid.addWidget(lab,0,0)
        grid.addWidget(lab1,0,1)
        grid.addWidget(lab2,1,0)
        grid.addWidget(lab3,1,1)
        
    def option_4(self):
        lab1=QLabel(self.stack_4)
        mov1=QMovie('fi.gif')
        mov1.setScaledSize(QSize(300,300))
        lab1.setMovie(mov1)
        mov1.start()

        lab=QLabel(self.stack_4)
        mov=QMovie('fi.gif')
        mov.setScaledSize(QSize(300,300))
        lab.setMovie(mov)
        mov.start()

        lab2=QLabel(self.stack_4)
        mov2=QMovie('fi.gif')
        mov2.setScaledSize(QSize(300,300))
        lab2.setMovie(mov2)
        mov2.start()

        lab3=QLabel(self.stack_4)
        mov3=QMovie('fi.gif')
        mov3.setScaledSize(QSize(300,300))
        lab3.setMovie(mov3)
        mov3.start()
        #pack in to layout 
        grid=QGridLayout(self.stack_4)
        grid.addWidget(lab,0,0)
        grid.addWidget(lab1,0,1)
        grid.addWidget(lab2,1,0)
        grid.addWidget(lab3,1,1)

def main():
    app=QApplication(sys.argv)
    win=Health() 
   
    win.show()
  
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
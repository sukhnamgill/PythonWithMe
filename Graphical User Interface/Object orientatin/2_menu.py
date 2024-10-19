from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,20,600,450)
        lab=QLabel("sukhnam",self)
        lab.move(400,30)
        lab.setFixedWidth(700)
        self.font=QFont("arial",20)
        lab.setFont(self.font)
        #add menu bar
        menu=self.menuBar()
        file=menu.addMenu('FILE')
        more=file.addMenu("more")
        more2=more.addMenu("one more")
        more2.addAction('save')
        action=file.addAction("OPEN")
        action2=file.addAction("CLOSE")
        action3=file.addAction("GENDER")
        # action3.addAction("more")
        menu2=self.menuBar()
        edit=menu.addMenu("EDIT")
       
        
        act2=edit.addAction("MINUS")
        # edit = file.addMenu("Edit")
        # edit.addAction("copy")
        # edit.addAction("paste")
        

        # save
        # save=QAction("save",self)
        # save.setShortcut("ctrl+v")
        # act3=edit.addAction(save)
        # save.associatedWidgets('helo')
        save3=QAction(QIcon("add.jpg"),"Save 3",self)
        sam=file.addAction(save3)





        file.triggered[QAction].connect(self.hello)
        edit.triggered[QAction].connect(self.hello)


    def hello(self,q):
        print(q.text())
        








def main():
    app=QApplication(sys.argv)
    win=Win()
    win.show()
    sys.exit(app.exec_())     
if __name__=='__main__':
    main()   
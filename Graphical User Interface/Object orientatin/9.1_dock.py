from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class Window(QMainWindow):
    def __init__(self,parent=None):
        super(Window,self).__init__(parent)
        
        self.setGeometry(20,29,500,600)
        self.setWindowTitle("sukhnam")
        bar=QMenuBar(self)
        menu=bar.addMenu("File")
        s=menu.addAction("call me")
        menu.addAction("Are you miss me")
        save=menu.addMenu("more")
        save.addAction("Good Luck you")
        self.setCentralWidget(QTextEdit())
        
        
        bar.move(50,0)
        # box.addWidget(self.setCentralWidget(QTextEdit("enter")))
        

        lis=QListWidget()
        lis.addItems(["apple","Orange","Santra","amb"])
        lis.move(0,50)
        self.dock=QDockWidget("dockage",self)
        self.dock.setWidget(lis)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)






        print("function call")
def main():
    app=QApplication(sys.argv)
    win=Window()
    win.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
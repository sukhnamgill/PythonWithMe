from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Zalwa(QMainWindow):
    def __init__(self,parent=None):
        super(Zalwa,self).__init__(parent)
        self.setGeometry(50,60,600,600)
        menu_bar=QMenuBar(self)
        main=menu_bar.addMenu("FILE")
        open_=main.addAction("Open")
        close_=main.addAction("Close")
        save_=main.addAction("Save")
        saveas_=main.addAction("Save as")
        main.triggered[QAction].connect(self.get_val)
    

        cal=QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20,50)
        cal.setFixedHeight(500)
        cal.setFixedWidth(500)
        cal.clicked[QDate].connect(self.date_func)
    def date_func(self,j):
        print(j.toString())

        #add status bar
        self.status=QStatusBar()
    
    def get_val(self,j):
        print(j.text())
        self.status.showMessage(f"The file is {j.text()}ing ....",5000)
        self.setStatusBar(self.status)






def main():
    app=QApplication(sys.argv)
    win=Zalwa()
    win.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Dia(QWidget):
    def __init__(self,parent=None):
        super(Dia,self).__init__(parent)
        btn=QPushButton(self)
        btn.setText("OPEN DIALOG")
        self.setGeometry(10,50,600,600)
        btn.clicked.connect(self.open_dialog)
        
    def open_dialog(self):
        s=QDialog(self)
        sb=QPushButton(s)
        sb.setText("ADD WINDOWs")
        sb.clicked.connect(self.add_window)
        sb.move(10,50)
        # s.setWindowModality(Qt.ApplicationModal) 
        s.exec_()
    def add_window(self):
        m=QMdiSubWindow(self)
        m.setWidget(QTextEdit())
        # m.setWidget()
        m.show()



def main():
    app=QApplication(sys.argv)
    win=Dia()
    win.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
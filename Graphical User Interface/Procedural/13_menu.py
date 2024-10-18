from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
def main():
    app=QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Menu Bar Example without Class")
    window.setGeometry(100, 100, 600, 400)

    # Create a menu bar
    menu_bar = window.menuBar()

    # Create the 'File' menu and add actions
    file_menu = menu_bar.addMenu("File")
 



    window.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
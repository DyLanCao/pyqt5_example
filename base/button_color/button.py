import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
global ival
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button color:https://www.cnblogs.com/dylancao/'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        global ival
        ival = 0
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.button = QPushButton('Color', self)
        self.button.setToolTip('This is an example button about color ')
        self.button.setStyleSheet("background-color: red")
        self.button.move(100,70)
        self.button.clicked.connect(self.on_click)
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        global ival
        ival += 1
        if ival == 1:
        	self.button.setStyleSheet("background-color: red")
        elif ival == 2:
        	self.button.setStyleSheet("background-color: #ffff00;")
        elif ival == 3:
        	ival = 0
        	self.button.setStyleSheet("background-color: rgb(0,255,255)")

        print('PyQt5 button click:',ival)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import *  
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setFixedWidth(600)
        self.setFixedHeight(600)

       # stylesheet = \
       #     ".QWidget {\n" \
       #     + "border: 1px solid white;\n" \
       #     + "border-radius: 1px;\n" \
       #     + "background-color: rgb(0, 155, 255);\n" \
       #     + "}"
        with open('ui.qss') as file:
            css = file.readlines()
            css =''.join(css).strip('\n')
        self.setStyleSheet(css)

        #self.setStyleSheet(stylesheet)
        self.widget = QWidget(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.widget)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


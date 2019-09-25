#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a submenu.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initBarMenu()

    def pause(self):
        print("pause file")

    def next(self):
        print("next file")

    def prev(self):
        print("prev file")

    def stop(self):
        print("stop file")

    def start(self):
        print("start file")

    def initBarMenu(self):         

        pauseAct = QAction(QIcon('pause85.png'), 'Pause', self)
        pauseAct.setShortcut('Ctrl+P')
        #exitAct.setStatusTip('Exit application')
        pauseAct.triggered.connect(self.pause)

        exitAct = QAction(QIcon('start.png'), 'Start', self)
        exitAct.setShortcut('Ctrl+Q')
        #exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.start)

        prevAct = QAction(QIcon('left_arr.png'), 'Left', self)
        prevAct.setShortcut('Ctrl+L')
        #exitAct.setStatusTip('Exit application')
        prevAct.triggered.connect(self.prev)

        nextAct = QAction(QIcon('right_arr.png'), 'Right', self)
        nextAct.setShortcut('Ctrl+R')
        #exitAct.setStatusTip('Exit application')
        nextAct.triggered.connect(self.next)

        stopAct = QAction(QIcon('stop.png'), 'Stop', self)
        stopAct.setShortcut('Ctrl+S')
        #exitAct.setStatusTip('Exit application')
        stopAct.triggered.connect(self.stop)

        self.statusBar()

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(pauseAct)
        toolbar.addAction(exitAct)
        toolbar.addAction(prevAct)
        toolbar.addAction(nextAct)
        toolbar.addAction(stopAct)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self) 
        impMenu.addAction(impAct)

        newAct = QAction('New', self)        

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        editMenu = menubar.addMenu('Edit')

        impMenu = QMenu('Delete', self)
        pasteMenu = QMenu('Paste', self)
        editMenu.addMenu(impMenu)
        editMenu.addMenu(pasteMenu)

        helpMenu = menubar.addMenu('Help')

        aboutMenu = QMenu('About', self)
        copyMenu = QMenu('CopyRight', self)
        helpMenu.addMenu(aboutMenu)
        helpMenu.addMenu(copyMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Audacity')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

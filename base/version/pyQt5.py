import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5 import QtCore

app = QApplication(sys.argv)
qev = QWebEngineView()
qev.show()

print(QtCore.qVersion())

def runTest():
    try:
        from PyQt5.QtTest import QTest
        from PyQt5.QtCore import Qt
        QTest.keyClick(qev, Qt.Key_Tab)
        print('finished')
    except Exception as e:
        print('exception:', e)
    finally:
        exit()

qev.page().loadFinished.connect(runTest)
qev.load(QUrl('http://google.com'))
app.exec_()

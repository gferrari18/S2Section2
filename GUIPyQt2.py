import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.resize(500,500)
        self.setWindowTitle("PyQt5")

        self.label = QLabel(self)
        self.label.setText("Hello World!")
        self.label.move(50,20)

        self.label2 = QLabel(self)
        self.label2.setText("kkk eae men")
        self.label2.move(50,100)


        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.label.setFont(font)



app = QApplication(sys.argv)
q1 = mainwindow()
q1.label.setText("ai fica complicado")



def main():
    app = QApplication(sys.argv)
    w = q1
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
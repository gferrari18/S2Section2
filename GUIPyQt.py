import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    w=QWidget()
    w.setGeometry(900,900,900,200) #(HORIZONTAL place, Vertical Place, width, height)
    w.setWindowTitle("kkk eae men")

    b = QLabel(w)
    b.setText("Hello World!")
    b.move(20,20)

    w.show ()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()

from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic

class UiLoad(QWidget):
    def __init__(self):
        super.__init__(self)
        uic.loadUi("MonitoringUi.ui", self)


app = QApplication(sys.argv)
window = QWidget()
window.show()
sys.exit(app.exec())
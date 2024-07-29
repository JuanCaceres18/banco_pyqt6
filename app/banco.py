from PyQt6.QtWidgets import QApplication
from gui.login import Login

# Clase que va a ejecutar la app
class Banco():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()

        # Ejecutar app
        self.app.exec()
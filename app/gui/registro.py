from PyQt6 import uic # Convertir la gui en código PYTHON
from PyQt6.QtWidgets import QMessageBox

class RegisterWindow():
    def __init__(self):
        # Cargar interfaz gráfica
        self.registro = uic.loadUi("./app/gui/registro.ui")
        self.registro.show()
    
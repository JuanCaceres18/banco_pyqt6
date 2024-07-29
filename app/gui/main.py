from PyQt6 import uic # Convertir la gui en código PYTHON
from PyQt6.QtWidgets import QMessageBox
from data.user import UserData
from model.user import User

class MainWindow():
    def __init__(self):
        # Cargar interfaz gráfica
        self.main = uic.loadUi("./app/gui/main.ui")
        self.main.showMaximized()

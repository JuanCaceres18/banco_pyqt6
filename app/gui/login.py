from PyQt6 import uic # Convertir la gui en código PYTHON
from PyQt6.QtWidgets import QMessageBox
from data.user import UserData
from model.user import User
from gui.main import MainWindow

class Login():
    def __init__(self):
        # Cargar interfaz gráfica
        self.login = uic.loadUi("./app/gui/login_gui.ui")
        # Establecer mensaje de error en vacío
        self.login.txt_error.setText("")
        self.login.show()
        self.initGUI()

    # Función para validar datos
    def ingresar(self):
        if len(self.login.input_user.text()) < 2:
            self.login.txt_error.setText("Ingresa un usuario válido")
            # Pongo el cursor en ese campo donde está el error
            self.login.input_user.setFocus() 
        elif len(self.login.input_password.text()) < 3:
            self.login.txt_error.setText("Ingresa una contraseña válida")
            self.login.input_password.setFocus()
        else:
            self.login.txt_error.setText("")
            # Creo el usuario
            usu = User(usuario=self.login.input_user.text(), clave= self.login.input_password.text())
            usuData = UserData()
            res = usuData.login(usu)
            if res:
                self.main = MainWindow()
                # Ocultar ventana de login
                self.login.hide()
            else:
                self.login.txt_error.setText("Datos incorrectos")
                       
    def initGUI(self):
        # Qué hace el botón cuando le damos click
        self.login.btn_acceder.clicked.connect(self.ingresar)
        
        
        

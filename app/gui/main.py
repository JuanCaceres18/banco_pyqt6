from PyQt6 import uic # Convertir la gui en código PYTHON
from PyQt6.QtWidgets import QMessageBox

class MainWindow():
    def __init__(self):
        # Cargar interfaz gráfica
        self.main = uic.loadUi("./app/gui/main.ui")
        self.initGUI()
        self.main.showMaximized()

    
    # Abrir opciones de menú
    def initGUI(self):
        self.main.btnRegistrar_transferencia.triggered.connect(self.abrirRegistro)

    def abrirRegistro(self):
        # Cargar interfaz gráfica
        self.registro = uic.loadUi("./app/gui/registro.ui")
        self.registro.btnRegistrar.clicked.connect(self.registrarTransferencia)
        self.registro.show()

    def registrarTransferencia(self):
        # Si el CBTipo tiene este texto, significa que no seleccionó nada
        if self.registro.cbTipo.currentText() == "--Selecciona una opción--":
            message = QMessageBox()
            message.setText("Debe seleccionar el tipo de documento")
            message.exec()
        elif self.registro.cbMotivo.currentText() == "--Selecciona una opción--":
            message = QMessageBox()
            message.setText("Debe seleccionar el motivo de giro")
            message.exec()
        elif len(self.registro.txtDocumento.text()) < 4:
            message = QMessageBox()
            message.setText("El número de documento no puede tener menos de 4 caracteres")
            message.exec()
        elif not self.registro.txtMonto.text().isnumeric() or int(self.registro.txtMonto.text()) < 0:
            message = QMessageBox()
            message.setText("Debe ingresar un monto válido")
            message.exec()
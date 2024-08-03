from PyQt6 import uic # Convertir la gui en código PYTHON
from PyQt6.QtWidgets import QMessageBox
from data.ciudad import CiudadData
from data.transferencia import TransferenciaData
from model.movimientos import Transferencia

class MainWindow():
    def __init__(self):
        # Cargar interfaz gráfica
        self.main = uic.loadUi("./app/gui/main.ui")
        self.initGUI()
        self.main.showMaximized()

    
    # Abrir opciones de menú
    def initGUI(self):
        self.main.btnRegistrar_transferencia.triggered.connect(self.abrirRegistro)
        self.main.btnReportar_transferencia.triggered.connect(self.abrirDeposito)
        # Cargar interfaz gráfica
        self.registro = uic.loadUi("./app/gui/registro.ui")
         # Cargar interfaz gráfica
        self.deposito = uic.loadUi("./app/gui/deposito.ui")

    def abrirRegistro(self):
        self.registro.btnRegistrar.clicked.connect(self.registrarTransferencia)
        self.registro.show()
    
    def abrirDeposito(self):
        self.deposito.btnRegistrar.clicked.connect(self.registrarTransferencia)
        self.deposito.show()
        self.llenarComboCiudades()


################### Transferencias ##################################
    def registrarTransferencia(self):
        # Si el CBTipo tiene este texto, significa que no seleccionó nada
        if self.registro.cbTipo.currentText() == "--Selecciona una opción--":
            message = QMessageBox()
            message.setText("Debe seleccionar el tipo de documento")
            message.exec()
            self.registro.cbTipo.setFocus()
        elif self.registro.cbMotivo.currentText() == "--Selecciona una opción--":
            message = QMessageBox()
            message.setText("Debe seleccionar el motivo de giro")
            message.exec()
            self.registro.cbMotivo.setFocus()
        elif len(self.registro.txtDocumento.text()) < 4:
            message = QMessageBox()
            message.setText("El número de documento no puede tener menos de 4 caracteres")
            message.exec()
            self.registro.txtDocumento.setFocus()
        elif not self.registro.txtMonto.text().isnumeric() or int(self.registro.txtMonto.text()) < 0:
            message = QMessageBox()
            message.setText("Debe ingresar un monto válido")
            message.exec()
            self.registro.txtMonto.setText("0")
            self.registro.txtMonto.setFocus()
        else:
            transferencia = Transferencia(
                tipo= self.registro.cbTipo.currentText(),
                documento= self.registro.txtDocumento.text(),
                monto= float(self.registro.txtMonto.text()),
                motivo= self.registro.cbMotivo.currentText(),
                dolares= self.registro.checkTransferencia.isChecked(),
                internacional=self.registro.checkDolares.isChecked()
            )
            # print("trans: ", self.registro.checkTransferencia.isChecked())
            # print("dollar: ", self.registro.checkDolares.isChecked())
            objData = TransferenciaData()
            mBox = QMessageBox()
            if objData.registrar(info=transferencia):
                mBox.setText("Transferencia registrada!")
                self.limpiarCamposTransferencia()
            else:
                mBox.setText("Error en la transferencia!")    
            mBox.exec()
    
    def limpiarCamposTransferencia(self):
        self.registro.cbTipo.setCurrentIndex(0)
        self.registro.cbMotivo.setCurrentIndex(0)
        self.registro.txtDocumento.setText("")
        self.registro.txtMonto.setText("0")
        self.registro.checkDolares.setChecked(False)
        self.registro.checkTransferencia.setChecked(False)
        self.registro.cbTipo.setFocus()

################### Depósitos ############################
    def llenarComboCiudades(self):
        objData = CiudadData()
        datos = objData.listaCiudades()
        for item in datos:
            self.deposito.cbLugar.addItem(item[1])
    
    def validarCamposDeposito(self)->bool:
        if (not self.deposito.cbTipo.currentText() == "--Selecciona una opción--" or not self.deposito.txtDocumento.text() or not self.deposito.txtMonto.text() or not self.deposito.txtPrimerNombre.text() or not self.deposito.txtPrimerApellido.text() or not self.deposito.cbSexo.currentText() == "--Selecciona una opción--" or not self.deposito.cbLugar.currentText() == "--Selecciona una opción--"):
            return False
        else:
            return True
    
    def registrarDeposito(self):
        if self.validarCamposDeposito():
            message = QMessageBox()
            message.setText("Debe seleccionar el tipo de documento")
            message.exec()

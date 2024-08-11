from PyQt6 import uic # Convertir la gui en código PYTHON
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt6.QtCore import QDate
from data.ciudad import CiudadData
from data.historial import HistorialData
from data.transferencia import TransferenciaData
from model.movimientos import Transferencia
from model.movimientos import DepositoInternacional
from data.deposito import DepositoData

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
        self.main.btnHistorial_de_transferencias.triggered.connect(self.abrirHistorial)
        # Cargar interfaz gráfica
        self.registro = uic.loadUi("./app/gui/registro.ui")
         # Cargar interfaz gráfica
        self.deposito = uic.loadUi("./app/gui/deposito.ui")
        self.historial = uic.loadUi("./app/gui/historial.ui")


    def abrirRegistro(self):
        self.registro.btnRegistrar.clicked.connect(self.registrarTransferencia)
        self.registro.show()
    
    def abrirDeposito(self):
        self.deposito.btnRegistrar.clicked.connect(self.registrarDeposito)
        self.deposito.show()
        self.llenarComboCiudades()

    def abrirHistorial(self):
        self.historial.btnBuscar.clicked.connect(self.buscar)
        self.historial.tblHistorial.setColumnWidth(1, 250)
        self.historial.tblHistorial.setColumnWidth(3, 250)
        self.historial.show()
        self.llenarTablaHistorial()



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
        if (self.deposito.cbTipo.currentText() == "--Selecciona una opción--" or not self.deposito.txtDocumento.text() or not self.deposito.txtMonto.text() or not self.deposito.txtPrimerNombre.text() or not self.deposito.txtPrimerApellido.text() or self.deposito.cbSexo.currentText() == "--Selecciona una opción--" or self.deposito.cbLugar.currentText() == "--Selecciona una opción--"):
            return False
        else:
            return True
    
    def limpiarCamposDeposito(self):
        self.deposito.cbTipo.setCurrentIndex(0)
        self.deposito.cbMotivo.setCurrentIndex(0)
        self.deposito.txtDocumento.setText("")
        self.deposito.txtMonto.setText("0")
        self.deposito.txtPrimerNombre.setText("")
        self.deposito.txtSegundoNombre.setText("")
        self.deposito.txtPrimerApellido.setText("")
        self.deposito.txtSegundoApellido.setText("")
        self.deposito.cbSexo.setCurrentIndex(0)
        self.deposito.cbLugar.setCurrentIndex(0)
        self.deposito.checkTerminos.setChecked(False)
        miFecha = QDate(2000,1,1)
        self.deposito.date.setDate(miFecha)
        self.registro.txtDocumento.setFocus()
    
    def registrarDeposito(self):
        message = QMessageBox()
        if not self.validarCamposDeposito():
            message.setText("Debe llenar los campos obligatorios (*)")
            message.exec()
        elif self.deposito.checkTerminos.isChecked() == False:
            message.setText("Debe aceptar los términos")
            message.exec()
            self.deposito.checkTerminos.setFocus()
        # Si el monto no es numérico o si es menor a 1
        elif not self.deposito.txtMonto.text().isnumeric() or float(self.deposito.txtMonto.text()) < 1:
            message.setText("El monto debe ser mayor a 0")
            self.deposito.txtMonto.setText("0")
            message.exec()
            self.deposito.txtMonto.setFocus()

        else:
            fechaN = self.deposito.date.date().toPyDate()
            deposito = DepositoInternacional(
                tipo= self.deposito.cbTipo.currentText(),
                documento= self.deposito.txtDocumento.text(),
                monto= float(self.deposito.txtMonto.text()),
                motivo= self.deposito.cbMotivo.currentText(),
                nombre1= self.deposito.txtPrimerNombre.text(),
                nombre2= self.deposito.txtSegundoNombre.text(),
                apellido1= self.deposito.txtPrimerApellido.text(),
                apellido2= self.deposito.txtSegundoApellido.text(),
                sexo = self.deposito.cbSexo.currentText(),
                lugarNacimiento= self.deposito.cbLugar.currentText(),
                terminos = self.deposito.checkTerminos.isChecked(),
                fechaNacimiento= fechaN
            )
            # print("trans: ", self.registro.checkTransferencia.isChecked())
            # print("dollar: ", self.registro.checkDolares.isChecked())
            objData = DepositoData()
            mBox = QMessageBox()
            if objData.registrar_deposito(info=deposito):
                mBox.setText("Depósito registrado!")
                mBox.exec()
                self.limpiarCamposDeposito()
            else:
                mBox.setText("Depósito no registrado!")    
                mBox.exec()

################### Historial ############################
    def buscar(self):
        his = HistorialData()
        data = his.buscarPorFecha(self.historial.txtDesde.date().toPyDate(), self.historial.txtHasta.date().toPyDate(), self.historial.cbTipo.currentText(), self.historial.txtDocumento.text())
        print(data)
        fila = 0
        nombre = None
        # Mostrar las filas
        self.historial.tblHistorial.setRowCount(len(data))
        for item in data:
            # Coloco el id
            self.historial.tblHistorial.setItem(fila, 0, QTableWidgetItem(str(item[0])))
            if nombre:
                self.historial.tblHistorial.setItem(fila, 1, QTableWidgetItem("{} {} {} {}".format(nombre)))
            else:
                self.historial.tblHistorial.setItem(fila, 1, QTableWidgetItem("{} {} {} {}".format(str(item[10]), str(item[11]), str(item[12]), str(item[13]))))
                nombre = "{} {} {} {}".format(str(item[10]), str(item[11]), str(item[12]), str(item[13]))

            if str(item[6]) == 'True':
                self.historial.tblHistorial.setItem(fila, 2, QTableWidgetItem(str("USD " + item[2])))
            else:
                self.historial.tblHistorial.setItem(fila, 2, QTableWidgetItem(str("ARS " + item[2])))

            if str(item[5]) == 'True':
                self.historial.tblHistorial.setItem(fila, 3, QTableWidgetItem(str("Transferencia internacional " + item[2])))
            else:
                self.historial.tblHistorial.setItem(fila, 3, QTableWidgetItem(str("Transferencia Nacional " + item[2])))
            self.historial.tblHistorial.setItem(fila, 4, QTableWidgetItem(str(item[7])))
            if str(item[17]) == 'True':
                self.historial.tblHistorial.setItem(fila, 5, QTableWidgetItem("SI"))
            else: 
                self.historial.tblHistorial.setItem(fila, 5, QTableWidgetItem("NO"))

            fila = fila+1


    def llenarTablaHistorial(self):
        pass
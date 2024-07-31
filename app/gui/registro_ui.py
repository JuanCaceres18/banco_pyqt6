# Form implementation generated from reading ui file 'c:\Users\User\OneDrive\Escritorio\Proyecto_Banco\app\gui\registro.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_registro(object):
    def setupUi(self, registro):
        registro.setObjectName("registro")
        registro.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        registro.resize(596, 356)
        registro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5 = QtWidgets.QLabel(parent=registro)
        self.label_5.setGeometry(QtCore.QRect(40, 10, 191, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("c:\\Users\\User\\OneDrive\\Escritorio\\Proyecto_Banco\\app\\gui\\../../../../../../Downloads/logo_banco.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(parent=registro)
        self.label_3.setGeometry(QtCore.QRect(300, 40, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(parent=registro)
        self.label.setGeometry(QtCore.QRect(60, 130, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cbTipo = QtWidgets.QComboBox(parent=registro)
        self.cbTipo.setGeometry(QtCore.QRect(30, 160, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbTipo.setFont(font)
        self.cbTipo.setObjectName("cbTipo")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.label_2 = QtWidgets.QLabel(parent=registro)
        self.label_2.setGeometry(QtCore.QRect(320, 130, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=registro)
        self.label_4.setGeometry(QtCore.QRect(60, 210, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=registro)
        self.label_6.setGeometry(QtCore.QRect(320, 210, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cbMotivo = QtWidgets.QComboBox(parent=registro)
        self.cbMotivo.setGeometry(QtCore.QRect(30, 240, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbMotivo.setFont(font)
        self.cbMotivo.setObjectName("cbMotivo")
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.txtDocumento = QtWidgets.QLineEdit(parent=registro)
        self.txtDocumento.setGeometry(QtCore.QRect(320, 160, 201, 31))
        self.txtDocumento.setObjectName("txtDocumento")
        self.txtMonto = QtWidgets.QLineEdit(parent=registro)
        self.txtMonto.setGeometry(QtCore.QRect(320, 240, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtMonto.setFont(font)
        self.txtMonto.setObjectName("txtMonto")
        self.checkTransferencia = QtWidgets.QCheckBox(parent=registro)
        self.checkTransferencia.setGeometry(QtCore.QRect(40, 300, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkTransferencia.setFont(font)
        self.checkTransferencia.setObjectName("checkTransferencia")
        self.checkDolares = QtWidgets.QCheckBox(parent=registro)
        self.checkDolares.setGeometry(QtCore.QRect(230, 300, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkDolares.setFont(font)
        self.checkDolares.setObjectName("checkDolares")
        self.btnRegistrar = QtWidgets.QPushButton(parent=registro)
        self.btnRegistrar.setGeometry(QtCore.QRect(320, 290, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btnRegistrar.setStyleSheet("background-color: rgb(5, 178, 89);\n"
"color: white;\n"
"border: none;\n"
"border-radius: 10px;")
        self.btnRegistrar.setObjectName("btnRegistrar")

        self.retranslateUi(registro)
        QtCore.QMetaObject.connectSlotsByName(registro)

    def retranslateUi(self, registro):
        _translate = QtCore.QCoreApplication.translate
        registro.setWindowTitle(_translate("registro", "Dialog"))
        self.label_3.setText(_translate("registro", "Registro de transferencias"))
        self.label.setText(_translate("registro", "Tipo de documento"))
        self.cbTipo.setItemText(0, _translate("registro", "--Selecciona una opción--"))
        self.cbTipo.setItemText(1, _translate("registro", "DNI - Documento Nacional de Identidad"))
        self.cbTipo.setItemText(2, _translate("registro", "PSS - Pasaporte"))
        self.cbTipo.setItemText(3, _translate("registro", "VISA"))
        self.label_2.setText(_translate("registro", "Número de documento"))
        self.label_4.setText(_translate("registro", "Motivo del giro"))
        self.label_6.setText(_translate("registro", "Monto"))
        self.cbMotivo.setItemText(0, _translate("registro", "--Selecciona una opción--"))
        self.cbMotivo.setItemText(1, _translate("registro", "Honorarios/Servicios técnicos"))
        self.cbMotivo.setItemText(2, _translate("registro", "Remesas/Giros"))
        self.cbMotivo.setItemText(3, _translate("registro", "Donaciones"))
        self.txtMonto.setText(_translate("registro", "0"))
        self.checkTransferencia.setText(_translate("registro", "Transferencia internacional?"))
        self.checkDolares.setText(_translate("registro", "Dólares?"))
        self.btnRegistrar.setText(_translate("registro", "Registrar"))
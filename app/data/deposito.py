import conexion as con
from model.movimientos import DepositoInternacional
from datetime import datetime 

class DepositoData():
    def __init__(self):
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            
            sql_create_table_deposito = """
                CREATE TABLE IF NOT EXISTS deposito
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                monto NUMERIC,
                tipo TEXT,
                documento TEXT,
                internacional BOOLEAN,
                dolares BOOLEAN,
                fecha_registro DATETIME,
                fecha_nacimiento DATETIME,
                motivo TEXT,
                pnombre TEXT,
                snombre TEXT,
                papellido TEXT,
                sapellido TEXT,
                sexo TEXT,
                ciudad_nacimiento TEXT,
                terminos BOOLEAN
                )
            """
            self.cursor.execute(sql_create_table_deposito)
            self.db.commit()
            self.cursor.close()
            self.db.close()
            print("Tabla deposito creada!")
        except Exception as ex:
            print("Tabla deposito OK: ", ex)


    def registrar_deposito(self, info:DepositoInternacional): # Voy a recibir un usuario de tipo Usuario
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # Devuelvo referencia a la base de datos
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        self.cursor.execute("""
            INSERT INTO deposito VALUES(null, '{}','{}','{}','{}','{}','{}','{}','{}', '{}','{}','{}','{}','{}','{}','{}')
        """.format(info._monto, info._tipo, info._documento, info._internacional, info._dolares,fecha, info._fechaNacimiento, info._motivo, info._nombre1, info._nombre2, info._apellido1, info._apellido2, info._sexo, info._lugarNacimiento, info._terminos))
        self.db.commit()
        # Si las filas afectadas dan como resultado 1, entonces sí se produjo el insert.
        if self.cursor.rowcount == 1:
            return True
        else:
            return False
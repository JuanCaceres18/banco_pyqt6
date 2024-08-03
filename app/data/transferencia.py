import conexion as con
from model.movimientos import Transferencia
from datetime import datetime 

class TransferenciaData():
    def __init__(self):
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            
            sql_create_table_transferencias = """
                CREATE TABLE IF NOT EXISTS transferencias
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                monto NUMERIC,
                tipo TEXT,
                documento TEXT,
                internacional BOOLEAN,
                dolares BOOLEAN,
                fecha_registro DATETIME,
                verificado BOOLEAN,
                motivo TEXT)
            """
            self.cursor.execute(sql_create_table_transferencias)
            self.db.commit()
            self.cursor.close()
            self.db.close()
            print("Tabla transferencias creada!")
        except Exception as ex:
            print("Tabla transferencia OK: ", ex)


    def registrar(self, info:Transferencia): # Voy a recibir un usuario de tipo Usuario
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # Devuelvo referencia a la base de datos
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        self.cursor.execute("""
            INSERT INTO transferencias VALUES(null, '{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._monto, info._tipo, info._documento, info._internacional, info._dolares,fecha, False, info._motivo))
        self.db.commit()
        # Si las filas afectadas dan como resultado 1, entonces sí se produjo el insert.
        if self.cursor.rowcount == 1:
            return True
        else:
            return False
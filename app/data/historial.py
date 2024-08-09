import conexion as con

class HistorialData():
    def buscarPorFecha(self, fechaDesde, fechaHasta):
        # Devuelvo referencia a la base de datos
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        sql = """
        SELECT D.*, T.monto as monto1, T.motivo as motivo1, T.dolares as dolares1 FROM transferencias T
        INNER JOIN deposito D ON D.tipo=T.tipo and D.documento=T.documento  
        WHERE T.fecha_registro >= '{}' and T.fecha_registro <= '{}'
        """
        res = self.cursor.execute(sql)
        self.cursor.close()
        self.db.close()
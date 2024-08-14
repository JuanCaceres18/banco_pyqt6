import conexion as con

class HistorialData():
    def buscarPorFecha(self, fechaDesde, fechaHasta, tipo,documento):
        # Devuelvo referencia a la base de datos
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        sql = """
        SELECT T.id as transaccion, D.*, T.verificado FROM transferencias T
        INNER JOIN deposito D ON D.tipo=T.tipo and D.documento=T.documento  
        WHERE T.fecha_registro >= '{}' and T.fecha_registro <= '{}' and D.documento='{}' and D.tipo = '{}'
        and T.motivo=D.motivo and T.monto=D.monto
        """.format(fechaDesde, fechaHasta, documento, tipo)
        res = self.cursor.execute(sql)
        data = res.fetchall()
        return data
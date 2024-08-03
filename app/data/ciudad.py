import conexion as con
from model.movimientos import Transferencia

class CiudadData():
    def listaCiudades(self):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        res = self.cursor.execute("SELECT * FROM ciudades ORDER BY nombre")
        ciudades = res.fetchall()
        return ciudades

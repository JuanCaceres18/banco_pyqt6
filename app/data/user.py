import conexion as con
from model.user import User

class UserData():
    def login(self, usuario:User): # Voy a recibir un usuario de tipo Usuario
        # Devuelvo referencia a la base de datos
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        res = self.cursor.execute("SELECT * FROM usuarios WHERE usuario='{}' AND clave='{}'".format(usuario._usuario, usuario._clave))
        fila = res.fetchone()
        self.cursor.close()
        self.db.close()
        # Si la fila me devuelve algo, entonces...
        if fila:
            usuario = User(nombre=fila[1], usuario=fila[1])
            return usuario
        else:
            return None
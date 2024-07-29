import sqlite3

class Conexion:
    # Crear base de datos si no existe
    def __init__(self):
        try:
            self.con = sqlite3.connect("banco.db")
            self.cargar_tablas()
        except Exception as ex:
            print(ex)
    
    def cargar_tablas(self):
        sql_table = """CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT UNIQUE,
        clave TEXT)
        """

        # Utilizo la conexión creada anteriormente
        cur = self.con.cursor()
        cur.execute(sql_table)
        cur.close()

        self.crear_admin()
    
    # Crear usuario admin
    def crear_admin(self):
        try:
            sql_admin = "INSERT INTO usuarios VALUES(null, '{}', '{}', '{}')".format("Administrador", "admin", "root")
            cur = self.con.cursor()
            cur.execute(sql_admin)
            self.con.commit()
            cur.close()
        except Exception as ex:
            print("Ya se creó el usuario: ", ex)
    
    def conectar(self):
        return self.con
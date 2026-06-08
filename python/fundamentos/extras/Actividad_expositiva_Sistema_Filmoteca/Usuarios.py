#Importar clases e instancias
from conexion import Conexion
from peliculas import Pelicula
from pedidos import Pedido
from peliculas import pel1
from peliculas import pel2
from peliculas import pel3
from peliculas import pel4
from peliculas import pel5

class Usuario:
    usuarios = []
    tipo_usuario = ["Administrador", "Usuario"]
    
    def __init__(self, ID, username, email, password, tipo_usuario_ID, created_by=1):
        self.ID = ID
        self.username = username
        self.email = email
        self.password_hash = password
        self.tipo_usuario = tipo_usuario_ID
        self.saldo_pendiente = 0
        self.created_by = created_by
        Usuario.usuarios.append(self.username)
        
    def realizar_pedido(self, pelicula, cantidad):
        print("Comprando película...")
        if pelicula == pel1.titulo:
            if cantidad > pel1.stock:
                print("Stock no disponible.")
            else:
                total = pel1.precio_unitario * cantidad
                self.saldo_pendiente += total
                pel1.stock -= cantidad
                print(f"\nPelícula/s comprada/s éxitosamente\nSaldo a pagar total: ${self.saldo_pendiente}")
                print(f"Stock actual de {pel1.titulo}: {pel1.stock}")
        elif pelicula == pel2.titulo:
            if cantidad > pel2.stock:
                print("Stock no disponible.")
            else:
                total = pel2.precio_unitario * cantidad
                self.saldo_pendiente += total
                pel2.stock -= cantidad
                print(f"\nPelícula/s comprada/s éxitosamente\nSaldo a pagar total: ${self.saldo_pendiente}")
                print(f"Stock actual de {pel2.titulo}: {pel2.stock}")
        elif pelicula == pel3.titulo:
            if cantidad > pel3.stock:
                print("Stock no disponible.")
            else:
                total = pel3.precio_unitario * cantidad
                self.saldo_pendiente += total
                pel3.stock -= cantidad
                print(f"\nPelícula/s comprada/s éxitosamente\nSaldo a pagar total: ${self.saldo_pendiente}")
                print(f"Stock actual de {pel3.titulo}: {pel3.stock}")
        elif pelicula == pel4.titulo:
            if cantidad > pel4.stock:
                print("Stock no disponible.")
            else:
                total = pel4.precio_unitario * cantidad
                self.saldo_pendiente += total
                pel4.stock -= cantidad
                print(f"\nPelícula/s comprada/s éxitosamente\nSaldo a pagar total: ${self.saldo_pendiente}")
                print(f"Stock actual de {pel4.titulo}: {pel4.stock}")
        elif pelicula == pel5.titulo:
            if cantidad > pel5.stock:
                print("Stock no disponible.")
            else:
                total = pel5.precio_unitario * cantidad
                self.saldo_pendiente += total
                pel5.stock -= cantidad
                print(f"\nPelícula/s comprada/s éxitosamente\nSaldo a pagar total: ${self.saldo_pendiente}")
                print(f"Stock actual de {pel5.titulo}: {pel5.stock}")
        
    def pagar_saldo(self, monto):
        if monto > self.saldo_pendiente:
            print("Error: monto más alto que el saldo a pagar.")
        else:
            print("Pagando saldo...")
            self.saldo_pendiente -= monto
            if self.saldo_pendiente <= 0.0:
                print("Saldo totalmente pagado.")
            else:
                print(f"Parte del saldo pagado, pero aún quedan ${self.saldo_pendiente} por pagar")
    
    def cambiar_contrasena(self, nueva_contrasena):
        print("Actualizando contraseña...")
        self.password_hash = nueva_contrasena
        
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
    
        sql = """INSERT INTO Usuarios(password_hash)
        VALUES(%s)"""
        valores = (self.password_hash)
        cursor.execute(sql, valores)
        
        conexion.commit()
        print("Contraseña actualizada correctamente.")
        cursor.close()
        conexion.close()
        
    def mostrar_usuarios(self, id):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """SELECT id_usuario, id_tipo_usuario, username, email
        FROM Usuarios
        WHERE deleted = 0"""
        cursor.execute(sql)
        listaUsuarios = cursor.fetchall()
        tipo = ""
        if listaUsuarios[id-1][1] == 2:
            tipo = "Administrador"
        elif listaUsuarios[id-1][1] == 1:
            tipo = "Usuario"
        print("\nImprimiendo información del usuario...")
        print(f"Nombre de usuario: {listaUsuarios[id-1][2]}")
        print(f"Email: {listaUsuarios[id-1][3]}")
        print(f"Tipo de usuario: {tipo}")
        print(f"Saldo pendiente: {self.saldo_pendiente}")
        
user1 = Usuario(1, "SuperDONO17", "donovansaez@liceovvh.cl", "JAOSF)=/JF", 1)
user2 = Usuario(2, "IncrediJavi", "javierazapata@liceovvh.cl", "nsKSJ=(/!/%", 2)
user3 = Usuario(3, "MegaDav", "davidtobar@liceovvh.cl", "NAu9!)47", 2)
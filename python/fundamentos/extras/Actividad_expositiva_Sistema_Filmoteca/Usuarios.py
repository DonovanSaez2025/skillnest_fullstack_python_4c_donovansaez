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
    
    def __init__(self, ID, username, email, password, tipo_usuario_ID, saldo_pendiente=0, created_by=1):
        self.ID = ID
        self.username = username
        self.email = email
        self.password_hash = password
        self.tipo_usuario = tipo_usuario_ID
        self.saldo_pendiente = saldo_pendiente
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
                # Contacto SQL
                conexion = Conexion.conectar()
                cursor = conexion.cursor()
                sql = """UPDATE Películas
                SET stock = %s
                WHERE id_pelicula = %s"""
                valores = (pel1.stock, pel1.ID)
                cursor.execute(sql, valores)
                conexion.commit()
                cursor.close()
                conexion.close()
        elif pelicula == pel2.titulo:
            if cantidad > pel2.stock:
                print("Stock no disponible.")
            else:
                total = pel2.precio_unitario * cantidad
                self.saldo_pendiente += total
                pel2.stock -= cantidad
                print(f"\nPelícula/s comprada/s éxitosamente\nSaldo a pagar total: ${self.saldo_pendiente}")
                print(f"Stock actual de {pel2.titulo}: {pel2.stock}")
                # Contacto SQL
                conexion = Conexion.conectar()
                cursor = conexion.cursor()
                sql = """UPDATE Películas
                SET stock = %s
                WHERE id_pelicula = %s"""
                valores = (pel2.stock, pel2.ID)
                cursor.execute(sql, valores)
                conexion.commit()
                cursor.close()
                conexion.close()
        elif pelicula == pel3.titulo:
            if cantidad > pel3.stock:
                print("Stock no disponible.")
            else:
                total = pel3.precio_unitario * cantidad
                self.saldo_pendiente += total
                pel3.stock -= cantidad
                print(f"\nPelícula/s comprada/s éxitosamente\nSaldo a pagar total: ${self.saldo_pendiente}")
                print(f"Stock actual de {pel3.titulo}: {pel3.stock}")
                # Contacto SQL
                conexion = Conexion.conectar()
                cursor = conexion.cursor()
                sql = """UPDATE Películas
                SET stock = %s
                WHERE id_pelicula = %s"""
                valores = (pel3.stock, pel3.ID)
                cursor.execute(sql, valores)
                conexion.commit()
                cursor.close()
                conexion.close()
        elif pelicula == pel4.titulo:
            if cantidad > pel4.stock:
                print("Stock no disponible.")
            else:
                total = pel4.precio_unitario * cantidad
                self.saldo_pendiente += total
                pel4.stock -= cantidad
                print(f"\nPelícula/s comprada/s éxitosamente\nSaldo a pagar total: ${self.saldo_pendiente}")
                print(f"Stock actual de {pel4.titulo}: {pel4.stock}")
                # Contacto SQL
                conexion = Conexion.conectar()
                cursor = conexion.cursor()
                sql = """UPDATE Películas
                SET stock = %s
                WHERE id_pelicula = %s"""
                valores = (pel4.stock, pel4.ID)
                cursor.execute(sql, valores)
                conexion.commit()
                cursor.close()
                conexion.close()
        elif pelicula == pel5.titulo:
            if cantidad > pel5.stock:
                print("Stock no disponible.")
            else:
                total = pel5.precio_unitario * cantidad
                self.saldo_pendiente += total
                pel5.stock -= cantidad
                print(f"\nPelícula/s comprada/s éxitosamente\nSaldo a pagar total: ${self.saldo_pendiente}")
                print(f"Stock actual de {pel5.titulo}: {pel5.stock}")
                # Contacto SQL
                conexion = Conexion.conectar()
                cursor = conexion.cursor()
                sql = """UPDATE Películas
                SET stock = %s
                WHERE id_pelicula = %s"""
                valores = (pel5.stock, pel5.ID)
                cursor.execute(sql, valores)
                conexion.commit()
                cursor.close()
                conexion.close()
        # Contacto SQL
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """UPDATE Usuarios
        SET saldo_pendiente = %s
        WHERE id_usuario = %s"""
        valores = (self.saldo_pendiente, self.ID)
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        
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
        # Contacto SQL
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """UPDATE Usuarios
        SET saldo_pendiente = %s
        WHERE id_usuario = %s"""
        valores = (self.saldo_pendiente, self.ID)
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
    
    def cambiar_contrasena(self, nueva_contrasena):
        print("Actualizando contraseña...")
        self.password_hash = nueva_contrasena
        # Contacto SQL
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """UPDATE Usuarios
        SET password_hash = %s
        WHERE id_usuario = %s"""
        valores = (self.password_hash)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Contraseña actualizada correctamente.")
        cursor.close()
        conexion.close()
        
    def mostrar_usuarios(self):
        #Contacto SQL
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """SELECT t.nombre_tipo_usuario, u.username, u.email, u.saldo_pendiente
        FROM Usuarios u
        INNER JOIN Tipos_de_usuario t
        ON u.id_tipo_usuario = t.id_tipo_usuario
        WHERE id_usuario = %s AND u.deleted = 0 AND t.deleted = 0"""
        valores = (self.ID,)
        cursor.execute(sql, valores)
        listaUsuario = cursor.fetchall()
        cursor.close()
        conexion.close()
        #Imprimir información
        print("\nImprimiendo información del usuario...")
        print(f"Nombre de usuario: {listaUsuario[0][1]}")
        print(f"Email: {listaUsuario[0][2]}")
        print(f"Tipo de usuario: {listaUsuario[0][0]}")
        print(f"Saldo pendiente: ${listaUsuario[0][3]}")
        
user1 = Usuario(1, "SuperDONO17", "donovansaez@liceovvh.cl", "JAOSF)=/JF", 1)
user2 = Usuario(2, "IncrediJavi", "javierazapata@liceovvh.cl", "nsKSJ=(/!/%", 2)
user3 = Usuario(3, "MegaDav", "davidtobar@liceovvh.cl", "NAu9!)47", 2)
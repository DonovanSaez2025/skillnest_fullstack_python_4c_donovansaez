#Importar clases e instancias
from conexion import Conexion
from pedidos import Pedido

class Pelicula:
    peliculas = []
    formatos = ["VHS", "Betamax", "LaserDisc", "DVD", "Blu-ray"]
    
    def __init__(self, ID, titulo, anio, precio_unitario, stock, formato_ID, estado_restauracion=False):
        self.ID = ID
        self.titulo = titulo
        self.anio = anio
        if estado_restauracion == "si":
            self.estado_restauracion = True
        else:
            self.estado_restauracion = False
        self.precio_unitario = precio_unitario
        self.stock = stock
        self.formato_ID = formato_ID
        Pelicula.peliculas.append(self.titulo)
        
    def actualizar_stock(self, cantidad):
        print("Actualizando stock...")
        self.stock += cantidad
        # Contacto SQL
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """UPDATE Películas
        SET stock = %s
        WHERE id_pelicula = %s"""
        valores = (self.stock, self.ID)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Stock actualizado, stock actual de la película: {self.stock}")
        cursor.close()
        conexion.close()
        
    
    def restaurar_pelicula(self):
        print("Restaurando película...")
        self.estado_restauracion = True
        print("Película restaurada con éxito.")
        # Contacto SQL
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """UPDATE Películas
        SET restaurado = %s
        WHERE id_pelicula = %s"""
        valores = (1, self.ID)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Stock actualizado, stock actual de la película: {self.stock}")
        cursor.close()
        conexion.close()
        
    def mostrar_info_pelicula(self):
        #Contacto SQL
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """SELECT p.titulo_pelicula, p.anio_publicacion, f.nombre_formato, p.restaurado, p.stock, p.precio_unitario
        FROM Películas p
        INNER JOIN Formatos f
        ON p.id_formato = f.id_formato
        WHERE p.deleted = 0 AND f.deleted = 0"""
        cursor.execute(sql)
        listaPeliculas = cursor.fetchall()
        print(listaPeliculas)
        #Establecer estado de restauracion
        rest = ""
        if listaPeliculas[self.ID-1][3] == 1:
            rest = "Restaurado"
        else:
            rest = "No restaurado"
        #Imprimir información
        print("\nMostrando información de la película...")
        print(f"Título: {listaPeliculas[self.ID-1][0]}")
        print(f"Año de publicación: {listaPeliculas[self.ID-1][1]}")
        print(f"Formato: {listaPeliculas[self.ID-1][2]}")
        print(f"Estado de restauración: {rest}")
        print(f"Stock: {listaPeliculas[self.ID-1][4]}")
        print(f"Precio unitario: {listaPeliculas[self.ID-1][5]}")
        
    @classmethod
    def mostrar_formatos(cls):
        #Contacto SQL
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """SELECT nombre_formato, descripcion_formato
        FROM Formatos
        WHERE deleted = 0"""
        cursor.execute(sql)
        listaFormatos = cursor.fetchall()
        #Imprimir información
        print("\nMostrando información de los formatos...")
        print(f"{listaFormatos[0][0]}: {listaFormatos[0][1]}")
        print(f"{listaFormatos[1][0]}: {listaFormatos[1][1]}")
        print(f"{listaFormatos[2][0]}: {listaFormatos[2][1]}")
        print(f"{listaFormatos[3][0]}: {listaFormatos[3][1]}")
        print(f"{listaFormatos[4][0]}: {listaFormatos[4][1]}")
        
pel1 = Pelicula(1, "Bugs Bunny's 3rd Movie: 1001 Rabbit Tales", 1981, 5.99, 10, 1)
pel2 = Pelicula(2, "The Bugs Bunny Road-Runner Movie", 1979, 3.99, 3, 2)
pel3 = Pelicula(3, "Looney Looney Looney Bugs Bunny Movie", 1982, 9.99, 5, 3)
pel4 = Pelicula(4, "Space Jam", 1996, 15.99, 30, 4, "si")
pel5 = Pelicula(5, "Daffy Duck's Quackbusters", 1988, 20.99, 25, 5, "si")
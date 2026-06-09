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
        WHERE id_pelicula = %s AND deleted = 0"""
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
        WHERE id_pelicula = %s AND deleted = 0"""
        valores = (1, self.ID)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Película restaurada correctamente.")
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
        WHERE p.id_pelicula = %s AND p.deleted = 0 AND f.deleted = 0"""
        valores = (self.ID,)
        cursor.execute(sql, valores)
        listaPelicula = cursor.fetchall()
        print(listaPelicula)
        #Establecer estado de restauracion
        rest = ""
        if listaPelicula[0][3] == 1:
            rest = "Restaurado"
        else:
            rest = "No restaurado"
        #Imprimir información
        print("\nMostrando información de la película...")
        print(f"Título: {listaPelicula[0][0]}")
        print(f"Año de publicación: {listaPelicula[0][1]}")
        print(f"Formato: {listaPelicula[0][2]}")
        print(f"Estado de restauración: {rest}")
        print(f"Stock: {listaPelicula[0][4]}")
        print(f"Precio unitario: {listaPelicula[0][5]}")
        
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
        for i in range(0, len(listaFormatos)):
            print(f"{listaFormatos[i][0]}: {listaFormatos[i][1]}")
        
pel1 = Pelicula(1, "Bugs Bunny's 3rd Movie: 1001 Rabbit Tales", 1981, 5.99, 10, 1)
pel2 = Pelicula(2, "The Bugs Bunny Road-Runner Movie", 1979, 3.99, 3, 2)
pel3 = Pelicula(3, "Looney Looney Looney Bugs Bunny Movie", 1982, 9.99, 5, 3)
pel4 = Pelicula(4, "Space Jam", 1996, 15.99, 30, 4, "si")
pel5 = Pelicula(5, "Daffy Duck's Quackbusters", 1988, 20.99, 25, 5, "si")
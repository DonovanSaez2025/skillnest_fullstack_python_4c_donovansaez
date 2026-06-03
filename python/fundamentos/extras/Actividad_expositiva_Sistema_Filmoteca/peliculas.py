class Pelicula:
    peliculas = []
    
    def __init__(self, titulo, anio, precio_unitario, stock, formato, estado_restauracion=False):
        self.titulo = titulo
        self.anio = anio
        if estado_restauracion == "Si":
            self.estado_restauracion = True
        else:
            self.estado_restauracion = False
        self.precio_unitario = precio_unitario
        self.stock = stock
        self.formato = formato
        Pelicula.peliculas.append(self.titulo)
        
    def actualizar_stock(self, cantidad):
        print("Actualizando stock...")
        self.stock += cantidad
        print(f"Stock actualizado, stock actual de la película: {self.stock}")
    
    def restaurar_pelicula(self):
        if self.estado_restauracion == True:
            print(f"La película {self.titulo} ya está restaurada")
        else:
            print("Restaurando película...")
            self.estado_restauracion = True
            print("Película restaurada con éxito.")
        
    def mostrar_info_pelicula(self):
        print("Mostrando información de la película...")
        print(f"Título: {self.titulo}")
        print(f"Año de publicación: {self.anio}")
        print(f"Formato: {self.formato}")
        print(f"Estado de restauración: {self.estado_restauracion}")
        print(f"Stock: {self.stock}")
        print(f"Precio unitario: {self.precio_unitario}")
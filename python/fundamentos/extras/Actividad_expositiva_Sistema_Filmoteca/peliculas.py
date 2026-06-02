class Pelicula:
    peliculas = []
    
    def __init__(self, titulo, anio, estado_restauracion, precio_unitario, stock, formato):
        self.titulo = titulo
        self.anio = anio
        self.estado_restauracion = estado_restauracion
        self.stock = stock
        self.precio_unitario = precio_unitario
        self.formato = formato
        Pelicula.peliculas.append(self.titulo)
        
    def actualizar_stock(self, cantidad):
        pass
    
    def restaurar_pelicula(self):
        pass
        
    def mostrar_info_pelicula(self):
        print("Mostrando información de la película...")
        print(f"Título: {self.titulo}")
        print(f"Año de publicación: {self.anio}")
        print(f"Formato: {self.formato}")
        print(f"Estado de restauración: {self.estado_restauracion}")
        print(f"Stock: {self.stock}")
        print(f"Precio unitario: {self.precio_unitario}")
    
#Crear instancias    
pel1 = Pelicula("Bugs Bunny's 3rd Movie: 1001 Rabbit Tales", 1981, "No restaurado", 5.99, 10, "VHS")
pel2 = Pelicula("The Bugs Bunny Road-Runner Movie", 1979, "No restaurado", 3.99, 3, "Betamax")
pel3 = Pelicula("Looney Looney Looney Bugs Bunny Movie", 1982, "No restaurado", 9.99, 5, "LaserDisc")
pel4 = Pelicula("Space Jam", 1996, "Restaurado", 15.99, 30, "DVD")
pel5 = Pelicula("Daffy Duck's Quackbusters", 1988, "Restaurado", 20.99, 25, "Blu-ray")
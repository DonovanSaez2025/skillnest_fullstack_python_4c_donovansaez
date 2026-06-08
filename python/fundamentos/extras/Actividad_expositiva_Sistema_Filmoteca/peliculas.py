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
        print(f"Stock actualizado, stock actual de la película: {self.stock}")
    
    def restaurar_pelicula(self):
        print("Restaurando película...")
        self.estado_restauracion = True
        print("Película restaurada con éxito.")
        
    def mostrar_info_pelicula(self):
        print("Mostrando información de la película...")
        print(f"Título: {self.titulo}")
        print(f"Año de publicación: {self.anio}")
        print(f"Formato: {Pelicula.formatos[self.formato_ID - 1]}")
        print(f"Estado de restauración: {self.estado_restauracion}")
        print(f"Stock: {self.stock}")
        print(f"Precio unitario: {self.precio_unitario}")
        
    @classmethod
    def mostrar_formatos(cls):
        print("Mostrando información de los formatos...")
        print(f"{cls.formatos[0]}: El primer formato de video casero")
        print(f"{cls.formatos[1]}: Competidor del VHS")
        print(f"{cls.formatos[2]}: Precursor del DVD")
        print(f"{cls.formatos[3]}: Derrotó al VHS por su mayor capacidad en GB en lugar de horas de grabación")
        print(f"{cls.formatos[4]}: Compitiendo con el DVD al día de hoy")
        
pel1 = Pelicula(1, "Bugs Bunny's 3rd Movie: 1001 Rabbit Tales", 1981, 5.99, 10, 1)
pel2 = Pelicula(2, "The Bugs Bunny Road-Runner Movie", 1979, 3.99, 3, 2)
pel3 = Pelicula(3, "Looney Looney Looney Bugs Bunny Movie", 1982, 9.99, 5, 3)
pel4 = Pelicula(4, "Space Jam", 1996, 15.99, 30, 4, "si")
pel5 = Pelicula(5, "Daffy Duck's Quackbusters", 1988, 20.99, 25, 5, "si")
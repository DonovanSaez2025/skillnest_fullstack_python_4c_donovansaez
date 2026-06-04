class Pelicula:
    peliculas = []
    formatos = ["VHS", "Betamax", "LaserDisc", "DVD", "Blu-ray"]
    
    def __init__(self, ID, titulo, anio, precio_unitario, stock, formato_ID, estado_restauracion=False):
        self.ID = ID
        self.titulo = titulo
        self.anio = anio
        if estado_restauracion == "Si":
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
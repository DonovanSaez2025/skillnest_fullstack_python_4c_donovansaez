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
        
    def mostrar_info_pelicula(self):
        print("Mostrando información de la película...")
class Pelicula:
    
    peliculas = []
    
    def __init__(self, titulo, formato, precio_unitario):
        self.titulo = titulo
        self.formato = formato
        Pelicula.peliculas.append(titulo)
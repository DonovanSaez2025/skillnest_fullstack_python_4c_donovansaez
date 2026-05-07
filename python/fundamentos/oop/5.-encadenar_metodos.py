# Clase usuario streaming
class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = ["top 10 mejores años", "simulador de nacer"]

    def agregar_a_lista(self, titulo):
        #Agrega un contenido a la lista de reproducción del usuario.
        self.lista_reproduccion.append(titulo)
        print(f"\nLista de reproducción de {self.nombre}:\n- {"\n- ".join(self.lista_reproduccion)}")
        return self

    def ver_contenido(self, titulo):
        #Simula que el usuario reproduce un contenido.
        print(f"\n{self.nombre} está viendo ahora: {titulo}")
        return self

    def cambiar_suscripcion(self, nueva_suscripcion):
        #Cambia el tipo de suscripción del usuario.
        self.suscripcion = nueva_suscripcion
        print(f"\nNueva suscripción de {self.nombre}: {self.suscripcion}")
        return self

    def mostrar_info_usuario(self):
        #Muestra la información del usuario y su lista de reproducción.
        print("\nMostrando información del usuario:")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripción: {self.suscripcion}")
        if len(self.lista_reproduccion) == 0:
            print(f"Lista de reproducción: vacía")
        else:
            print(f"Lista de reproducción: \n- {"\n- ".join(self.lista_reproduccion)}")

matias = UsuarioStreaming("Matías", "matias@liceovvh.cl", "Gratis")

def metodosEncadenados():
    while True:
        titulo = input("Ingresa el título de un vídeo: ").strip()
        print(f"\n{" | ".join(matias.lista_reproduccion)}")
        verTitulo = input("Ingresa el título de un video para verlo: ").strip()
        nuevaSuscripcion = input("Ingresa el nuevo rango de suscripción (Gratis, Estándar, Premium): ")
        if titulo == "":
            print("El título mo puede estar vacío.")
            continue
        if (verTitulo in matias.lista_reproduccion) == False:
            print("Vídeo para ver no encontrado.")
            continue
        if nuevaSuscripcion != "Gratis" and nuevaSuscripcion != "Estándar" != nuevaSuscripcion != "Premium":
            print("Nueva suscripción inválida.")
            continue
        matias.agregar_a_lista(titulo).ver_contenido(verTitulo).cambiar_suscripcion(nuevaSuscripcion).mostrar_info_usuario()
        break
metodosEncadenados()
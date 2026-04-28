import os
# Clase usuario streaming
class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

    def agregar_a_lista(self, titulo):
        #Agrega un contenido a la lista de reproducción del usuario.
        self.lista_reproduccion.append(titulo)
        print(f"Lista de reproducción de {self.nombre}:\n{" || ".join(self.lista_reproduccion)}")

    def ver_contenido(self, titulo):
        #Simula que el usuario reproduce un contenido.
        print(f"{self.nombre} está viendo ahora: {titulo}")

    def cambiar_suscripcion(self, nueva_suscripcion):
        #Cambia el tipo de suscripción del usuario.
        self.suscripcion = nueva_suscripcion
        print(f"Nueva suscripción de {self.nombre}: {self.suscripcion}")

    def mostrar_info_usuario(self):
        #Muestra la información del usuario y su lista de reproducción.
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripción: {self.suscripcion}")
        if len(self.lista_reproduccion) == 0:
            print(f"Lista de reproducción: vacía")
        else:
            print(f"Lista de reproducción: \n- {"\n- ".join(self.lista_reproduccion)}")

matias = UsuarioStreaming("Matías", "matias@liceovvh.cl", "Gratis")
sebastian = UsuarioStreaming("Sebastian", "sebastian@liceovvh.cl", "Estándar")
camilo = UsuarioStreaming("Camilo", "camilo@gmail.com", "Premium")

# Función para limpiar la consola
def limpiarConsola():
    os.system('cls')

# Menú while
Continue = True
while Continue:
    print("\n--- Métodos clase ---")
    print("--- Método 1: Agregar a la lista ---")
    print("--- Método 2: Ver contenido ---")
    print("--- Método 3: Cambiar suscripción ---")
    print("--- Método 4: Mostrar info del usuario ---")
    opcion = input("Ingresa una opción 1-4: ")
    if opcion == "1":
        limpiarConsola()
        usuario = input("Selecciona un usuario (matias, sebastian, camilo): ")
        if usuario == "matias":
            titulo = input(f"Ingresa el título video para la lista de {matias.nombre}: ").strip()
            if titulo != "":
                matias.agregar_a_lista(titulo)
            else:
                print("El título no puede estar vacío")
        elif usuario == "sebastian":
            titulo = input(f"Ingresa el título video para la lista de {sebastian.nombre}: ").strip()
            if titulo != "":
                sebastian.agregar_a_lista(titulo)
            else:
                print("El título no puede estar vacío")
        elif usuario == "camilo":
            titulo = input(f"Ingresa el título video para la lista de {camilo.nombre}: ").strip()
            if titulo != "":
                camilo.agregar_a_lista(titulo)
            else:
                print("El título no puede estar vacío")
        else:
            print("Usuario no encontrado.")
    elif opcion == "2":
        limpiarConsola()
        usuario = input("Selecciona un usuario (matias, sebastian, camilo): ")
        if usuario == "matias":
            if len(matias.lista_reproduccion) == 0:
                print(f"La lista de {matias.nombre} está vacía.")
            else:
                print(f"Lista de reproducción de {matias.nombre}:\n- {"\n- ".join(matias.lista_reproduccion)}")
                titulo = input("Selecciona un video par ver: ")
                if titulo in matias.lista_reproduccion:
                    matias.ver_contenido(titulo)
                else:
                    print(f"Ese video no está en la lista de {matias.nombre}.")
        elif usuario == "sebastian":
            if len(sebastian.lista_reproduccion) == 0:
                print(f"La lista de {sebastian.nombre} está vacía.")
            else:
                print(f"Lista de reproducción de {sebastian.nombre}:\n- {"\n- ".join(sebastian.lista_reproduccion)}")
                titulo = input("Selecciona un video par ver: ")
                if titulo in sebastian.lista_reproduccion:
                    sebastian.ver_contenido(titulo)
                else:
                    print(f"Ese video no está en la lista de {sebastian.nombre}.")
        elif usuario == "sebastian":
            if len(camilo.lista_reproduccion) == 0:
                print(f"La lista de {camilo.nombre} está vacía.")
            else:
                print(f"Lista de reproducción de {camilo.nombre}:\n- {"\n- ".join(camilo.lista_reproduccion)}")
                titulo = input("Selecciona un video par ver: ")
                if titulo in camilo.lista_reproduccion:
                    camilo.ver_contenido(titulo)
                else:
                    print(f"Ese video no está en la lista de {camilo.nombre}.")
        else:
            print("Usuario no encontrado.")
    elif opcion == "3":
        limpiarConsola()
        usuario = input("Selecciona un usuario (matias, sebastian, camilo): ")
        if usuario == "matias":
            print(f"Suscripción actual de {matias.nombre}: {matias.suscripcion}")
            cambioSuscripcion = input("Cambiar suscripción (Gratis, Estándar, Premium): ").strip()
            if cambioSuscripcion != "Gratis" and cambioSuscripcion != "Estándar" and cambioSuscripcion != "Premium":
                print("Suscripción no válida.")
            else:
                matias.cambiar_suscripcion(cambioSuscripcion)
        elif usuario == "sebastian":
            print(f"Suscripción actual de {sebastian.nombre}: {sebastian.suscripcion}")
            cambioSuscripcion = input("Cambiar suscripción (Gratis, Estándar, Premium): ").strip()
            if cambioSuscripcion != "Gratis" and cambioSuscripcion != "Estándar" and cambioSuscripcion != "Premium":
                print("Suscripción no válida.")
            else:
                sebastian.cambiar_suscripcion(cambioSuscripcion)
        elif usuario == "camilo":
            print(f"Suscripción actual de {camilo.nombre}: {camilo.suscripcion}")
            cambioSuscripcion = input("Cambiar suscripción (Gratis, Estándar, Premium): ").strip()
            if cambioSuscripcion != "Gratis" and cambioSuscripcion != "Estándar" and cambioSuscripcion != "Premium":
                print("Suscripción no válida.")
            else:
                camilo.cambiar_suscripcion(cambioSuscripcion)
    elif opcion == "4":
        limpiarConsola()
        usuario = input("Selecciona un usuario (matias, sebastian, camilo): ")
        if usuario == "matias":
            matias.mostrar_info_usuario()
        elif usuario == "sebastian":
            sebastian.mostrar_info_usuario()
        elif usuario == "camilo":
            camilo.mostrar_info_usuario()
        else:
            print("Usuario no encontrado.")
    elif opcion == "0":
        break
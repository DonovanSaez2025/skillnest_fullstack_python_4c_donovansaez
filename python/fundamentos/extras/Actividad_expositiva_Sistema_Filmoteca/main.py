from conexion import Conexion
from usuarios import Usuario
from peliculas import Pelicula
import os

# Función para limpiar la consola
def limpiarConsola():
    os.system('cls')

while True:
    print("\n--- Sistema de filmoteca ---")
    print("--- 1: Realizar un pedido de películas ---")
    print("--- 2: Pagar saldo pendiente ---")
    print("--- 3: Cambiar contraseña ---")
    print("--- 4: Mostrar un usuario ---")
    print("--- 5: Actualizar stock de una película ---")
    print("--- 6: Restaurar una película---")
    print("--- 7: Mostrar información de una película ---")
    print("--- 8: Mostrar los formatos ---")
    print("--- 0: Salir ---")
    opcion = input("Ingresa una opción: ")
    
    if opcion == "1":
        limpiarConsola()
        i = 0
        while i < len(Pelicula.peliculas):
            print(f"- {Pelicula.peliculas[i]} - Stock: {Pelicula.peliculas[i].stock}")
            i+=1
        pelicula = input("Selecciona una película (título completo): ").strip()
        if pelicula in Pelicula.peliculas:
            cantidad = int(input("Ingresa la cantidad de esa película que quieras comprar: "))
        else:
            print("Película inváida.")
        
    elif opcion == "2":
        limpiarConsola()
    elif opcion == "3":
        limpiarConsola()
    elif opcion == "4":
        limpiarConsola()
    elif opcion == "5":
        limpiarConsola()
    elif opcion == "6":
        limpiarConsola()
    elif opcion == "7":
        limpiarConsola()
    elif opcion == "8":
        limpiarConsola()
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")
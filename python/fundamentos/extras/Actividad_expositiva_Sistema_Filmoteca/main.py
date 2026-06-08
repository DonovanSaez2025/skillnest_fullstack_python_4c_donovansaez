# Importar clases
from conexion import Conexion
from usuarios import Usuario
from peliculas import Pelicula
from pedidos import Pedido
# Importar instancias
from usuarios import user1
from usuarios import user2
from usuarios import user3
from peliculas import pel1
from peliculas import pel2
from peliculas import pel3
from peliculas import pel4
from peliculas import pel5
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
        print(f"Usuarios registrados: \n- {("\n- ").join(Usuario.usuarios)}")
        user = input("Ingresa tu nombre de usuario: ")
        if user == user1.username:
            print(f"Películas:\n -{("\n -").join(Pelicula.peliculas)}")
            pelicula = input("Selecciona una película (título completo): ").strip()
            if pelicula in Pelicula.peliculas:
                cantidad = int(input("Ingresa la cantidad de esa película que quieras comprar: "))
                if cantidad < 1:
                    print("Cantidad inválida.")
                else:
                    user1.realizar_pedido(pelicula, cantidad)
            else:
                print("Película inváida.")
        elif user == user2.username:
            print(f"Películas:\n -{("\n -").join(Pelicula.peliculas)}")
            pelicula = input("Selecciona una película (título completo): ").strip()
            if pelicula in Pelicula.peliculas:
                cantidad = int(input("Ingresa la cantidad de esa película que quieras comprar: "))
                if cantidad < 1:
                    print("Cantidad inválida.")
                else:
                    user2.realizar_pedido(pelicula, cantidad)
            else:
                print("Película inváida.")
        elif user == user3.username:
            print(f"Películas:\n -{("\n -").join(Pelicula.peliculas)}")
            pelicula = input("Selecciona una película (título completo): ").strip()
            if pelicula in Pelicula.peliculas:
                cantidad = int(input("Ingresa la cantidad de esa película que quieras comprar: "))
                if cantidad < 1:
                    print("Cantidad inválida.")
                else:
                    user3.realizar_pedido(pelicula, cantidad)
            else:
                print("Película inváida.")
        else:
            print("Usuario inválido.")
    elif opcion == "2":
        limpiarConsola()
        print(f"Usuarios registrados: \n- {("\n- ").join(Usuario.usuarios)}")
        user = input("Ingresa tu nombre de usuario: ")
        if user == user1.username:
            if user1.saldo_pendiente == "0":
                print("El usuario no tiene un saldo que pagar.")
            else:
                print(f"Saldo a pagar: ${user1.saldo_pendiente}")
                monto = float(input("Ingresa un monto de dinero: "))
                if monto < 1:
                    print("Monto de dinero inválido.")
                else:
                    user1.pagar_saldo(monto)
        elif user == user2.username:
            if user2.saldo_pendiente == "0":
                print("El usuario no tiene un saldo que pagar.")
            else:
                print(f"Saldo a pagar: ${user2.saldo_pendiente}")
                monto = float(input("Ingresa un monto de dinero: "))
                if monto < 1:
                    print("Monto de dinero inválido.")
                else:
                    user2.pagar_saldo(monto)
        elif user == user3.username:
            if user3.saldo_pendiente == "0":
                print("El usuario no tiene un saldo que pagar.")
            else:
                print(f"Saldo a pagar: ${user3.saldo_pendiente}")
                monto = float(input("Ingresa un monto de dinero: "))
                if monto < 1:
                    print("Monto de dinero inválido.")
                else:
                    user3.pagar_saldo(monto)
        else:
            print("Usuario inválido.")
    elif opcion == "3":
        limpiarConsola()
        print(f"Usuarios registrados: \n- {("\n- ").join(Usuario.usuarios)}")
        user = input("Ingresa tu nombre de usuario: ")
        if user == user1.username:
            nuev_cont = input("Ingresa una nueva contraseña (mínimo 8 caracteres): ").strip()
            if nuev_cont == user1.password_hash:
                print("La contraseña es la misma.")
            elif len(nuev_cont) < 8:
                print("La contraseña es muy corta.")
            else:
                user1.cambiar_contrasena(nuev_cont)
        elif user == user2.username:
            nuev_cont = input("Ingresa una nueva contraseña (mínimo 8 caracteres): ").strip()
            if nuev_cont == user2.password_hash:
                print("La contraseña es la misma.")
            elif len(nuev_cont) < 8:
                print("La contraseña es muy corta.")
            else:
                user2.cambiar_contrasena(nuev_cont)
        elif user == user3.username:
            nuev_cont = input("Ingresa una nueva contraseña (mínimo 8 caracteres): ").strip()
            if nuev_cont == user3.password_hash:
                print("La contraseña es la misma.")
            elif len(nuev_cont) < 8:
                print("La contraseña es muy corta.")
            else:
                user3.cambiar_contrasena(nuev_cont)
        else:
            print("Usuario inválido.")
    elif opcion == "4":
        limpiarConsola()
        print(f"Usuarios registrados: \n- {("\n- ").join(Usuario.usuarios)}")
        user = input("Ingresa tu nombre de usuario: ")
        if user == user1.username:
            id = 1
            user1.mostrar_usuarios(id)
        elif user == user2.username:
            id = 2
            user1.mostrar_usuarios(id)
        elif user == user3.username:
            id = 3
            user3.mostrar_usuarios(id)
        else:
            print("Usuario inválido.")
    elif opcion == "5":
        limpiarConsola()
        print(f"Películas: \n- {("\n- ").join(Pelicula.peliculas)}")
        pel = input("Ingresa el título de una película: ")
        if pel == pel1.titulo:
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad < 1:
                print("Cantidad inválida.")
            else:
                pel1.actualizar_stock(cantidad)
        elif pel == pel2.titulo:
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad < 1:
                print("Cantidad inválida.")
            else:
                pel2.actualizar_stock(cantidad)
        elif pel == pel3.titulo:
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad < 1:
                print("Cantidad inválida.")
            else:
                pel3.actualizar_stock(cantidad)
        elif pel == pel4.titulo:
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad < 1:
                print("Cantidad inválida.")
            else:
                pel4.actualizar_stock(cantidad)
        elif pel == pel5.titulo:
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad < 1:
                print("Cantidad inválida.")
            else:
                pel5.actualizar_stock(cantidad)
        else:
            print("Película no encontrada")
    elif opcion == "6":
        limpiarConsola()
        print(f"Películas: \n- {("\n- ").join(Pelicula.peliculas)}")
        pel = input("Ingresa el título de una película: ")
        if pel == pel1.titulo:
            if pel1.estado_restauracion == True:
                print("Esta película ya está restaurada.")
            else:
                confirmacion = input("¿Restaurar película? (si/no): ").strip()
                if confirmacion.lower() == "si":
                    pel1.restaurar_pelicula()
        elif pel == pel2.titulo:
            if pel2.estado_restauracion == True:
                print("Esta película ya está restaurada.")
            else:
                confirmacion = input("¿Restaurar película? (si/no): ").strip()
                if confirmacion.lower() == "si":
                    pel2.restaurar_pelicula()
        elif pel == pel3.titulo:
            if pel3.estado_restauracion == True:
                print("Esta película ya está restaurada.")
            else:
                confirmacion = input("¿Restaurar película? (si/no): ").strip()
                if confirmacion.lower() == "si":
                    pel3.restaurar_pelicula()
        elif pel == pel4.titulo:
            if pel4.estado_restauracion == True:
                print("Esta película ya está restaurada.")
            else:
                confirmacion = input("¿Restaurar película? (si/no): ").strip()
                if confirmacion.lower() == "si":
                    pel4.restaurar_pelicula()
        elif pel == pel5.titulo:
            if pel5.estado_restauracion == True:
                print("Esta película ya está restaurada.")
            else:
                confirmacion = input("¿Restaurar película? (si/no): ").strip()
                if confirmacion.lower() == "si":
                    pel5.restaurar_pelicula()
        else:
            print("Película no encontrada")
    elif opcion == "7":
        limpiarConsola()
        print(f"Películas: \n- {("\n- ").join(Pelicula.peliculas)}")
        pel = input("Ingresa el título de una película: ")
        if pel == pel1.titulo:
            pel1.mostrar_info_pelicula()
        elif pel == pel2.titulo:
            pel2.mostrar_info_pelicula()
        elif pel == pel3.titulo:
            pel3.mostrar_info_pelicula()
        elif pel == pel4.titulo:
            pel4.mostrar_info_pelicula()
        elif pel == pel5.titulo:
            pel5.mostrar_info_pelicula()
        else:
            print("Película no encontrada")
    elif opcion == "8":
        limpiarConsola()
        Pelicula.mostrar_formatos()
    elif opcion == "9":
        limpiarConsola()
        print(f"Cantidad de pedidos: {Pedido}")
        id = int(input("Ingresa el ID del pedido: "))
        if id-1 < 0 or id > len(Pedido.pedidos):
            print("ID inválido.")
        else:
            Pedido.mostrarPedido(id-1)
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")
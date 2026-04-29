import os
# 1. Crear una función que reciba una lista de números enteros
# y muestre cuál es el número mayor y cuál es el menor.
def numeroMayorMenor(listado):
    listaNum = listado
    menor = min(listaNum)
    mayor = max(listaNum)
    print(f"El número menor es: {menor}\nEl número mayor es: {mayor}")

def ejercicio1():
    limit = int(input("Ingresa el límite de valores: "))
    listadoNum = []
    for i in range(0, limit):
        num = int(input("Ingresa un número entero: "))
        listadoNum.append(num)
    numeroMayorMenor(listadoNum)

# 2. Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
def contarVocales(texto):
    vocales = 0
    for i in range(0, len(texto)):
        if texto[i] == "a" or texto[i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i] == "u":
            vocales += 1
        elif texto[i] == "á" or texto[i] == "é" or texto[i] == "í" or texto[i] == "ó" or texto[i] == "ú":
            vocales += 1
    print(f"En el texto '{texto}' hay {vocales} vocales")
        
def ejercicio2():
    texto = input("Ingresa un texto: ").strip()
    contarVocales(texto.lower())

# 3. Crear una función que reciba una lista de nombres
# y muestre únicamente aquellos que tengan más de 5 letras.
def mostrarNombres(listaNombres):
    mayor5 = []
    for i in range(0, len(listaNombres)):
        if len(listaNombres[i]) > 5:
            mayor5.append(listaNombres[i])
    print(f"Nombres con más de 5 letras: {", ".join(mayor5)}")

def ejercicio3():
    limit = int(input("Ingresa el límite de valores: "))
    listaNombres = []
    for i in range(0, limit):
        nombre = input("Ingresa un nombre: ")
        listaNombres.append(nombre)
    mostrarNombres(listaNombres)

# 4. Crear una función que reciba una lista de notas (números decimales),
# calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
def promedioNotas(listaNotas):
    suma = sum(listaNotas)
    promedio = suma / len(listaNotas)
    if promedio >= 4.0:
        print(f"Con un promedio de {promedio}, el estudiante aprueba.")
    else:
        print(f"Con un promedio de {promedio}, el estudiante reprueba.")

def ejercicio4():
    limit = int(input("Ingresa el límite de notas: "))
    listaNotas = []
    go = False
    for i in range(0, limit):
        nota = float(input("Ingresa una nota del estudiante: "))
        if nota > 7.0 or nota < 1.0:
            print("Error: las notas no pueden ser mayores a 7.0 y menores a 1.0")
            go = False
            break
        else:
            listaNotas.append(nota)
            go = True
    if go == True:
        promedioNotas(listaNotas)

# 5. Crear una función que reciba una lista de precios de productos
# y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def descuentoProducto(listaPrecios):
    pass

def ejercicio5():
    pass

# 6. Crear una función que reciba un número entero y determine si es par o impar.
def parImpar(numero):
    pass

def ejercicio6():
    pass

# 7. Crear una función que reciba una lista de edades
# y muestre cuántas personas son mayores de edad (18 años o más).
def mayoresEdad(listaEdades):
    pass

def ejercicio7():
    pass

# 8. Crear una función que reciba una lista de palabras
# y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def palabrasRepetidas(listaPalabras):
    pass

def ejercicio8():
    pass

# 9. Crear una función que reciba una lista de números
# y genere una nueva lista que contenga únicamente los números positivos.
def numerosPositivos(listaNumeros):
    pass

def ejercicio9():
    pass

# 10. Crear una función que reciba una lista de productos
# (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.
def stockMenor(listaProductos):
    pass

def ejercicio10():
    pass

# Limpiar consola
def limpiarConsola():
    os.system('cls')

#Menú While
Continue = True
while Continue:
    print("\n--- Ejercicios funciones ---")
    print("--- Ejercicio 1 ---")
    print("--- Ejercicio 2 ---")
    print("--- Ejercicio 3 ---")
    print("--- Ejercicio 4 ---")
    print("--- Ejercicio 5 ---")
    print("--- Ejercicio 6 ---")
    print("--- Ejercicio 7 ---")
    print("--- Ejercicio 8 ---")
    print("--- Ejercicio 9 ---")
    print("--- Ejercicio 10 ---")
    opcion = input("Selecciona un ejercicio (1-10): ")
    
    if opcion == "1":
        limpiarConsola()
        ejercicio1()
    elif opcion == "2":
        limpiarConsola()
        ejercicio2()
    elif opcion == "3":
        limpiarConsola()
        ejercicio3()
    elif opcion == "4":
        limpiarConsola()
        ejercicio4()
    elif opcion == "5":
        limpiarConsola()
        ejercicio5()
    elif opcion == "6":
        limpiarConsola()
        ejercicio6()
    elif opcion == "7":
        limpiarConsola()
        ejercicio7()
    elif opcion == "8":
        limpiarConsola()
        ejercicio8()
    elif opcion == "9":
        limpiarConsola()
        ejercicio9()
    elif opcion == "10":
        limpiarConsola()
        ejercicio10()
    elif opcion == "0":
        print("Saliendo...")
        break
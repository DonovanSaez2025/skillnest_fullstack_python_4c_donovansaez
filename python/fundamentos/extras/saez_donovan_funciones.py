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
    if texto == "":
        print("Error: no puede estar vacío.")
    else:
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
    i = 0
    while i < limit:
        nombre = input("Ingresa un nombre: ").strip()
        if nombre == "":
            print("Error: no puede estar vacío.")
        else:
            listaNombres.append(nombre)
            i+=1
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
    i = 0
    while i < limit:
        nota = float(input("Ingresa una nota del estudiante: "))
        if nota > 7.0 or nota < 1.0:
            print("Error: las notas no pueden ser mayores a 7.0 y menores a 1.0")
        else:
            listaNotas.append(nota)
            i+=1
    promedioNotas(listaNotas)

# 5. Crear una función que reciba una lista de precios de productos
# y aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
def descuentoProducto(listaPrecios):
    subtotal = sum(listaPrecios)
    descuento = subtotal - (subtotal * 0.1)
    print(f"Precio total: ${subtotal}\nCon descuento: ${descuento}")
    
def ejercicio5():
    limit = int(input("Ingresa el límite de productos: "))
    listaPrecios = []
    for i in range(0, limit):
        precio = float(input("Ingresa el precio de un producto: "))
        listaPrecios.append(precio)
    descuentoProducto(listaPrecios)

# 6. Crear una función que reciba un número entero y determine si es par o impar.
def parImpar(num):
    if num == 0:
        print("Número 0")
    elif num % 2 == 0:
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")

def ejercicio6():
    num = int(input("Ingresa un número entero: "))
    parImpar(num)

# 7. Crear una función que reciba una lista de edades
# y muestre cuántas personas son mayores de edad (18 años o más).
def mayoresEdad(listaEdades):
    mayorEdad = 0
    for i in range(0, len(listaEdades)):
        if listaEdades[i] >= 18:
            mayorEdad += 1
    if mayorEdad == 0:
        print(f"No hay personas mayores de edad.")
    elif mayorEdad == 1:
        print(f"Solo hay {mayorEdad} persona mayor de edad.")
    elif mayorEdad > 1:
        print(f"hay {mayorEdad} personas mayores de edad.")

def ejercicio7():
    limit = int(input("Ingresa el límite de valores: "))
    listaEdades = []
    i = 0
    while i < limit:
        edad = int(input("Ingresa la edad de una persona: "))
        if edad < 0 or edad > 123:
            print("Edad imposible.")
        else:
            listaEdades.append(edad)
            i+=1
    mayoresEdad(listaEdades)

# 8. Crear una función que reciba una lista de palabras
# y permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
def palabrasRepetidas(listaPalabras):
    palabraBuscar = input("Ingresa una palabra para buscar en la lista de palabras: ")
    repeticion = 0
    for i in range(0, len(listaPalabras)):
        if listaPalabras[i] == palabraBuscar:
            repeticion += 1
    if repeticion == 0:
        print(f"La palabra '{palabraBuscar}' no está en la lista.")
    elif repeticion == 1:
        print(f"La palabra '{palabraBuscar}' aparece {repeticion} vez en la lista.")
    elif repeticion > 1:
        print(f"La palabra '{palabraBuscar}' aparece {repeticion} veces en la lista.")

def ejercicio8():
    limit = int(input("Ingresa el límite de palabras: "))
    listaPalabras = []
    i = 0
    while i < limit:
        palabra = input("Ingresa una palabra: ").strip()
        if palabra == "":
            print("Error: no puede estar vacío.")
        else:
            listaPalabras.append(palabra.lower())
            i+=1
    palabrasRepetidas(listaPalabras)

# 9. Crear una función que reciba una lista de números
# y genere una nueva lista que contenga únicamente los números positivos.
def numerosPositivos(listaNum):
    numPos = []
    for i in range(0, len(listaNum)):
        if listaNum[i] > 0:
            numPos.append(str(listaNum[i]))
    print(f"Números positivos en la lista: {" | ".join(numPos)}")

def ejercicio9():
    limit = int(input("Ingresa el límite de valores: "))
    listaNum = []
    for i in range(0, limit):
        num = float(input("Ingresa un número entero positivo o negativo: "))
        listaNum.append(num)
    numerosPositivos(listaNum)
        

# 10. Crear una función que reciba una lista de productos
# (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.
def stockMenor(listaProductos):
    pass

def ejercicio10():
    limit = int(input("Ingresa un límite de productos: "))
    listaProductos = {"nombres": [], "stock": []}
    i = 0
    while i < limit:
        nombreProd = input("Ingresa el nombre de un producto: ").strip()
        stockProd = int(input("Ingresa el stock de ese producto: "))
        if nombreProd == "" or stockProd < 0:
                print("Error: valores inválidos.")
        else:
            listaProductos["nombres"].append(nombreProd)
            listaProductos["stock"].append(stockProd)
            i += 1
    stockMenor(listaProductos)

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
    opcion = input("Selecciona un ejercicio (1-10): ").strip()
    
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
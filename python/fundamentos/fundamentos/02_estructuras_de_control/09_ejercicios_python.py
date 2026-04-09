#Ejercicio 1: Números Pares Dinámicos
'''Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). 
El programa debe imprimir los primeros $n$ números pares positivos.'''
def parDinamico():
    num = int(input("¿Cuántos números pares deseas ver? ")) #Pedir número al usuario
    for i in range(num + 1):
        if i % 2 == 0:
            print(i)
            
#Ejercicio 2: Verificador de Edad y Acceso
'''Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+).
Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.'''
def verificadorEdad():
    nacimiento = int(input("Ingresa tu año de nacimiento: "))
    anioPresente = 2026
    if nacimiento < 0:
        print("Ese no es un año válido")
    else:
        edad = anioPresente - nacimiento
        if edad < 18 and edad >= 1:
            print(f"Tienes {edad} años, eres menor de edad, te faltan {18 - edad} años para ser adulto.")
        elif edad >= 18:
            print(f"Tienes {edad} años, ya eres mayor de edad.")
    
#Ejercicio 3: Calculadora de Descuentos
'''Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100,
aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.'''
def calculadoraDescuento():
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresa la cantidad del producto: "))
    precioTotal = precio * cantidad
    descuento = 0.15
    if precioTotal > 100:
        subtotal = precioTotal - (precioTotal * descuento)
        #Los "$" son por signo dólar, no por confusión con JS
        print(f"Precio total: ${precioTotal}, se aplicó el descuento del 15% y se han descontado ${precioTotal * descuento}, el subtotal a pagar es ${subtotal}")
    elif precioTotal <= 100:
        print(f"Precio a pagar: ${precioTotal}")

#Ejercicio 4: Clasificador de Números
'''Pide un número al usuario e indica si es: Positivo-Par,
Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.'''
def clasificadorNum():
    num = int(input("Ingresa un número: "))
    caract1 = ""
    caract2 = ""

    if num == 0:
        print("El número es 0")
    elif num < 0:
        caract1 = "negativo"
        if num % 2 == 0:
            caract2 = "par"
        else:
            caract2 = "impar"
        print(f"El número {num} es {caract2} y {caract1}")
    elif num > 0:
        caract1 = "positivo"
        if num % 2 == 0:
            caract2 = "par"
        else:
            caract2 = "impar"
        print(f"El número {num} es {caract2} y {caract1}")

#Ejercicio 5: Tabla de Multiplicar Personalizada
'''Solicita un número entero y muestra su tabla de multiplicar del 1 al 12,
pero solo muestra los resultados que sean múltiplos de 3.'''
def multiplicarPersonalizada():
    num = int(input("Ingresa un número: "))
    tablaMultiplicar = []
    mostrar = []
    for i in range(13):
        multiplicacion = num * i
        if multiplicacion % 3 == 0:
            tablaMultiplicar.append(multiplicacion)
    print(tablaMultiplicar)

#Ejercicio 6: Sumatoria con Centinela
'''Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario
ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).'''
def sumatoriaCentinela():
    total = 0
    while 0 < 1:
        num = int(input("Ingresa un número a sumar: "))
        if (num < 0):
            break
        else:
            total += num
    print(f"La suma total es {total}")

#Ejercicio 7: Contador de Vocales
'''Pide al usuario una frase o palabra. Utiliza un bucle para recorrer
la cadena y contar cuántas vocales tiene en total.'''
def contadorVocales():
    texto = input("Ingresa una frase o palabra: ")
    vocales = 0
    for i in range(len(texto)):
        #Detectar vocales
        if texto[i].lower() == "a" or texto[i].lower() == "e" or texto[i].lower() == "i" or texto[i].lower() == "o" or texto[i].lower() == "u":
            vocales += 1
        #Detectar vocales sin tilde
        elif texto[i].lower() == "á" or texto[i].lower() == "é" or texto[i].lower() == "í" or texto[i].lower() == "ó" or texto[i].lower() == "ú":
            vocales += 1
    print(f"Hay {vocales} vocales en total en el string '{texto}'")

#Ejercicio 8: Validación de Contraseña
'''Define una contraseña en una variable. Pide al usuario que la intente adivinar.
Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.'''
def validarContrasena():
    acceso = False
    contrasena = "hola123"
    for i in range(3):
        contrasenaInput = input("Ingresa la contraseña: ")
        if contrasenaInput == contrasena:
            acceso = True
            break
        else:
            print("Contraseña incorrecta.")
    if acceso == True:
        print("Acceso permitido.")
    else:
        print("Acceso bloqueado.")

#Ejercicio 9: Registro de Nombres
'''Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y,
al final, imprímelos en orden inverso al que fueron ingresados.'''
def registroNombres():
    registro = []
    for i in range(5):
        nombre = input("Ingresa un nombre: ")
        registro.append(nombre)
    registro.reverse()
    for i in range(len(registro)):
        print(registro[i])

#Ejercicio 10: Promedio de Notas
'''Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo.
Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.'''
def promedioNotas():
    notasLimit = int(input("Ingresa la cantidad límite de notas: "))
    notas = []
    for i in range(notasLimit):
        nota = float(input("Ingresa una nota: "))
        notas.append(nota)
    promedio = sum(notas) / len(notas)
    alta = max(notas)
    baja = min(notas)
    print(f"El promedio final del alumno es de {promedio}, la nota más alta fue {alta} y la más baja fue {baja}")
    
promedioNotas()
#Ejercicio 11: Filtro de Arreglos
'''Dado un arreglo de números generado por el usuario,crea un nuevo arreglo que
contenga solo los números que sean mayores a 50. Muestra ambos arreglos.'''

#Ejercicio 12: Buscador de Elementos
'''Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y
el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.'''

#Ejercicio 13: Simulación de Inventario
'''Crea dos arreglos: uno para nombres_productos y otro para precios.Permite al usuario
ingresar 3 productos con sus precios. Luego, muestra una lista formateada:
Producto: [Nombre] - Precio: $[Valor].'''

#Ejercicio 14: Generador de Lista de Compras
'''Usa un bucle while para que el usuario agregue artículos a una lista de compras.
El proceso termina cuando el usuario escribe "terminar".
Al final, muestra la lista ordenada alfabéticamente.'''

#Ejercicio 15: Análisis de Temperaturas
'''Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
El promedio semanal.
- Cuántos días la temperatura fue superior a 25 grados.
- El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).'''
"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""
# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)
def nivelesImprimir():
    print("Imprimiendo niveles del 0 al 100")
    for i in range(101):
        print(f"Nivel {i}")
    
# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)
'''Imprime las posiciones de esos potenciadores, desde la posición 2 hasta la posición 500.
Ejemplo de salida: 2, 4, 6, 8… 498, 500.'''
def potenciadorEncontrar():
    print("Imprimiendo los potenciadores encontrados")
    for i in range(2, 501):
        if i % 2 == 0:
            print(f"Potenciador encontrado en la posición {i}")
            
# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)
'''Presta atención a la prioridad (si un punto es múltiplo de 10, también es de 5).
Decide qué se imprime primero.'''
def trampaEmoji():
    print("Recorriendo puntos para encontrar emojis")
    for i in range(1, 101):
        if i % 10 == 0:
            print(f"🍎 en el punto {i}")
        elif i % 5 == 0:
            print(f"🐍 en el punto {i}")

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)
def sumarBonus():
    print("Sumando puntos de bonificación de cada segundo par hasta el segundo 500000.")
    bonusXP = 0
    for i in range(0, 500001):
        if i % 2 == 0:
            bonusXP += i
    print(f"La recompensa final es de {bonusXP} puntos")

# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)
def viajeTemporal():
    print("Viajando al pasado hasta el año 0 o menos, partiendo desde 2024.")
    anioActual = 2024
    print(f"El año actual es {anioActual}")
    while anioActual > 0:
        anioActual -= 3
        print(f"El año actual es {anioActual}")

# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)
def contadorDinamico():
    inicio = int(input("Ingresa un número de inicio: "))
    fin = int(input("Ingresa un número final: "))
    salto = int(input("Ingresa un salto de intervalos: "))
    print("Realizando cálculo...")
    for i in range(inicio, fin + 1):
        if i % salto == 0:
            print(f"El nivel actual es {i}")
# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10

#Menú de navegación
continuar = True
while continuar:
    print("\n--- Ejercicios Core ---")
    print("--- Ejercicio 1 ---")
    print("--- Ejercicio 2 ---")
    print("--- Ejercicio 3 ---")
    print("--- Ejercicio 4 ---")
    print("--- Ejercicio 5 ---")
    print("--- Ejercicio 6 ---")
    opcion = input("\n --- Elige una opción: (1-6) (0 para salir): ")
    if opcion == "1":
        nivelesImprimir()
    elif opcion == "2":
        potenciadorEncontrar()
    elif opcion == "3":
        trampaEmoji()
    elif opcion == "4":
        sumarBonus()
    elif opcion == "5":
        viajeTemporal()
    elif opcion == "6":
        contadorDinamico()
    elif opcion == "0":
        break
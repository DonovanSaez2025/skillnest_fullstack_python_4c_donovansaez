#1. Generador de niveles:
#Imagina que estás diseñando un juego de plataformas donde cada nivel se numeran del 0 al 100.
#Utiliza un bucle for para imprimir todos los niveles desde el 0 hasta el 100 (incluyendo el 100).
def nivelesImprimir():
    print("Imprimiendo niveles del 0 al 100")
    for i in range(101):
        print(f"Nivel {i}")
    
#2. Potenciadores de energía (Múltiplos):
#En tu juego, cada 2 pasos se encuentra un potenciador de energía.
'''Imprime las posiciones de esos potenciadores, desde la posición 2 hasta la posición 500.
Ejemplo de salida: 2, 4, 6, 8… 498, 500.'''
def potenciadorEncontrar():
    print("Imprimiendo los potenciadores encontrados")
    for i in range(2, 501):
        if i % 2 == 0:
            print(f"Potenciador encontrado en la posición {i}")
            
#3. Trampa de emojis:
#Estás diseñando un sistema que muestra emojis cuando el personaje llega a ciertos puntos.
#Recorre los puntos del 1 al 100.
#Si un punto es divisible por 5, imprime un emoji bueno.
#Si un punto es divisible por 10, imprime un emoji malvado.
'''Presta atención a la prioridad (si un punto es múltiplo de 10, también es de 5).
Decide qué se imprime primero.'''
def trampaEmoji():
    print("Recorriendo puntos para encontrar emojis")
    for i in range(1, 101):
        if i % 10 == 0:
            print(f"🍎 en el punto {i}")
        elif i % 5 == 0:
            print(f"🐍 en el punto {i}")
#4. Suma colosal:
#Imagina que cada par de segundos en tu juego se acumula un bonus de experiencia.
'''Suma todos los bonus pares desde el segundo 0 hasta el segundo 500,000 (inclusive),
e imprime el total acumulado.'''
#Verás que el resultado es enorme, tal como las recompensas en un RPG masivo.
def sumarBonus():
    print("Sumando puntos de bonificación de cada segundo par hasta el segundo 500000.")
    bonusXP = 0
    for i in range(1, 500001):
        if i % 2 == 0:
            bonusXP += 1
    print(f"La recompensa final es de {bonusXP} puntos")

#5. Retroceso temporal:
'''Simula un viaje al pasado, comenzando en el año 2024 y
retrocediendo de 3 en 3 hasta llegar al año 0 o menos.'''
#Imprime cada año que visitas. Esto podría ser útil si imaginas un juego con viajes en el tiempo.
def viajeTemporal():
    print("Viajando al pasado hasta el año 0 o menos, partiendo desde 2024.")
    anioActual = 2024
    print(f"El año actual es {anioActual}")
    while anioActual > 0:
        anioActual -= 3
        print(f"El año actual es {anioActual}")

#6. Contador dinámico:
#Declara tres variables: inicio, fin y salto.
'''Piensa en inicio como el nivel de arranque, fin como el nivel final y salto como el tipo de avance
(o el intervalo de checkpoints).'''
#Imprime los niveles que son múltiplos de salto.
#Por ejemplo, si inicio = 3, fin = 10 y salto = 2, se imprimirán los niveles 4, 6, 8, 10.
def contadorDinamico():
    inicio = int(input("Ingresa un número de inicio: "))
    fin = int(input("Ingresa un número final: "))
    salto = int(input("Ingresa un salto de intervalos: "))
    print("Realizando cálculo...")
    for i in range(inicio, fin + 1):
        if i % salto == 0:
            print(f"El nivel actual es {i}")

#Menú de navegación
continuar = True
while continuar:
    print("\n--- Ejercicios Python ---")
    print("--- Interacci 1 ---")
    print("--- Ejercicio 2 ---")
    print("--- Ejercicio 3 ---")
    print("--- Ejercicio 4 ---")
    print("--- Ejercicio 5 ---")
    print("--- Ejercicio 6 ---")
    opcion = input("\n --- Elige una opción: (1-15) (0 para salir): ")
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
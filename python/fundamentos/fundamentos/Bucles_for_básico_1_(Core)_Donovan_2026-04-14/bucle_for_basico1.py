# Niveles del 0 al 100
def nivelesImprimir():
    for i in range(101):
        print(f"Nivel {i}")
    
# Encontrar potenciadores cada 2 pasos
def potenciadorEncontrar():
    for i in range(2, 501):
        if i % 2 == 0:
            print(f"Potenciador encontrado en la posición {i}")
            
# Trampa de emojis en pasos que sean divisibles por 10 o en 5
def trampaEmoji():
    for i in range(1, 101):
        if i % 10 == 0:
            print(f"Punto {i} maloso") #cambiar por emoji
        elif i % 5 == 0:
            print(f"Punto {i} Divertido") #cambiar por emoji

# Sumatoria de bonus XP en segundos pares hasta pasados 500000 segundos
def sumarBonus():
    bonusXP = 0
    for i in range(1, 500001):
        if i % 2 == 0:
            bonusXP += 1
    print(f"La recompensa final es de {bonusXP} puntos")

# Viajar en el tiempo al pasado hasta el año 0 o menos
def viajeTemporal():
    anioActual = 2024
    while anioActual > 0:
        anioActual -= 3
        print(f"El año actual es {anioActual}")

# Contador de niveles dinámico con intervalos de salto
def contadorDinamico():
    inicio = int(input("Ingresa un número de inicio: "))
    fin = int(input("Ingresa un número final: "))
    salto = int(input("Ingresa un salto de intervalos: "))
    for i in range(inicio, fin + 1):
        if i % salto == 0:
            print(f"El nivel actual es {i}")
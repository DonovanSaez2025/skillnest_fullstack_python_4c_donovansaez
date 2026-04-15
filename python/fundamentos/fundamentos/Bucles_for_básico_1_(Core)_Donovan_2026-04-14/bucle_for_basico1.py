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

#
bonusXP = 0
for i in range(1, 500001):
    if i % 2 == 0:
        bonusXP += i
print(f"La recompensa final es de {bonusXP} puntos")
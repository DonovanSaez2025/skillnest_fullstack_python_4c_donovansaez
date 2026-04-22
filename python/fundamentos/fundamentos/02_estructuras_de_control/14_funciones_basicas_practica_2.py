import os
# Funciones básicas práctica 2
# 1. Calcula experiencia
def multiplica_por_2(num):
    listaMultiplica = []
    for i in range(0, num*2+1):
        if i % 2 == 0:
            listaMultiplica.append(i)
    return listaMultiplica
# Debe retornar: [0, 2, 4, 6, 8, 10]


# 2, Analiza publicaciones
def suma_y_resta(numList):
    result1 = numList[0] + numList[1]
    result2 = numList[0] - numList[1]
    print(result1)
    return result2
# Imprime: 235 y retorna: 5

# 3. Puntaje ajustado
def sumatoria_menos_longitud(numList):
    total = sum(numList)
    longitud = len(numList)
    print(total)
    print(longitud)
    return total - longitud
# Suma total = 25, longitud = 4, debe retornar: 21


# 4. Ajusta visualizaciones
def valores_multiplicados_segundo(numList):
    longitud = len(numList)
    print(longitud)
    if longitud < 4:
        numList = []
    else:
        for i in range(0, longitud):
            numList[i] *= 3
            
    return numList
# Parte 1: Imprime: 4 y retorna: [300, 9, 150, 60]
# Parte 2: Imprime: 1 y retorna: []


# 5. Genera precio fijo
def valor_multiplicado_longitud(a, b):
    multList = []
    for i in range (0, b):
        multList.append(a * b)
    return multList
# Parte 1: Debe retornar: [10, 10]
# Parte 2: Debe retornar: [35, 35, 35, 35, 35]

def limpiarConsola():
    os.system('cls')

# Menú de navegación
Continue = True
while Continue:
    print("\n--- Ejercicios funciones 2 ---")
    print("Ejercicio 1")
    print("Ejercicio 2")
    print("Ejercicio 3")
    print("Ejercicio 4")
    print("Ejercicio 5")
    opcion = input("Escoge un ejercicio del 1 al 5: ")
    if opcion == "1":
        limpiarConsola()
        print("\nImprimiendo ejercicio 1:")
        print(multiplica_por_2(5))
    elif opcion == "2":
        limpiarConsola()
        print("\nImprimiendo ejercicio 2:")
        print(suma_y_resta([120, 115]))
    elif opcion == "3":
        limpiarConsola()
        print("\nImprimiendo ejercico 3:")
        print(sumatoria_menos_longitud([10, 5, 3, 7]))
    elif opcion == "4":
        limpiarConsola()
        print("\nImprimiendo ejercico 4 parte 1:")
        print(valores_multiplicados_segundo([100, 3, 50, 20]))
        
        print("\nImprimiendo ejercico 4 parte 2:")
        print(valores_multiplicados_segundo([100]))
    elif opcion == "5":
        limpiarConsola()
        print("\nImprimiendo ejercico 5 parte 1:")
        print(valor_multiplicado_longitud(5, 2))
        
        print("\nImprimiendo ejercico 5 parte 2:")
        print(valor_multiplicado_longitud(7, 5))
    elif opcion == "0":
        limpiarConsola()
    else:
        limpiarConsola()
        break
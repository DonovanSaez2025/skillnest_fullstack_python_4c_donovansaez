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
def ejercicio1():
    valor = multiplica_por_2(5)
    return valor

# 2, Analiza publicaciones
def suma_y_resta(numList):
    result1 = sum(numList)
    result2 = numList[0] - numList[1]
    print(result1)
    return result2
# Imprime: 235 y retorna: 5
def ejercicio2():
    valor = suma_y_resta([120, 115])
    return valor

# 3. Puntaje ajustado
def sumatoria_menos_longitud(numList):
    total = sum(numList)
    longitud = len(numList)
    print(total)
    print(longitud)
    return total - longitud
# Suma total = 25, longitud = 4, debe retornar: 21
def ejercicio3():
    valor = sumatoria_menos_longitud([10, 5, 3, 7])
    return valor

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
def ejercicio4_1():
    valor = valores_multiplicados_segundo([100, 3, 50, 20])
    return(valor)
# Parte 2: Imprime: 1 y retorna: []
def ejercicio4_2():
    valor = valores_multiplicados_segundo([100])
    return(valor)

# 5. Genera precio fijo
def valor_multiplicado_longitud(a, b):
    multList = []
    for i in range (0, b):
        multList.append(a * b)
    return multList
# Parte 1: Debe retornar: [10, 10]
def ejercicio5_1():
    valor = valor_multiplicado_longitud(5, 2)
    return valor
# Parte 2: Debe retornar: [35, 35, 35, 35, 35]
def ejercicio5_2():
    valor = valor_multiplicado_longitud(7, 5)
    return valor

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
        resultado = ejercicio1()
        print(resultado)
    elif opcion == "2":
        limpiarConsola()
        print("\nImprimiendo ejercicio 2:")
        resultado = ejercicio2()
        print(resultado)
    elif opcion == "3":
        limpiarConsola()
        print("\nImprimiendo ejercico 3:")
        resultado = ejercicio3()
        print(resultado)
    elif opcion == "4":
        limpiarConsola()
        print("\nImprimiendo ejercico 4 parte 1:")
        resultado1 = ejercicio4_1()
        print(resultado1)
        print("\nImprimiendo ejercico 4 parte 2:")
        resultado2 = ejercicio4_2()
        print(resultado2)
    elif opcion == "5":
        limpiarConsola()
        print("\nImprimiendo ejercico 5 parte 1:")
        result1 = ejercicio5_1()
        print(result1)
        print("\nImprimiendo ejercico 5 parte 2:")
        result2 = ejercicio5_2()
        print(result2)
    elif opcion == "0":
        limpiarConsola()
        break
    else:
        limpiarConsola()
# Funciones básicas práctica 2
# 1. Calcula experiencia
def multiplica_por_2(num):
    listaMultiplica = []
    for i in range(0, num*2+1):
        if i % 2 == 0:
            listaMultiplica.append(i)
    return listaMultiplica

result = multiplica_por_2(5)
print(result)
# Debe retornar: [0, 2, 4, 6, 8, 10]


# 2, Analiza publicaciones
def suma_y_resta(numList):
    result1 = numList[0] + numList[1]
    result2 = numList[0] - numList[1]
    print(result1)
    return result2

result = suma_y_resta([120, 115])
print(result)
# Imprime: 235 y retorna: 5


# 3. Puntaje ajustado
def sumatoria_menos_longitud(numList):
    total = sum(numList)
    longitud = len(numList)
    print(total)
    print(longitud)
    return total - longitud

result = sumatoria_menos_longitud([10, 5, 3, 7])
print(result)
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

result = valores_multiplicados_segundo([100, 3, 50, 20])
print(result)
# Imprime: 4 y retorna: [300, 9, 150, 60]

result = valores_multiplicados_segundo([100])
print(result)
# Imprime: 1 y retorna: []


# 5. Genera precio fijo
def valor_multiplicado_longitud(a, b):
    multList = []
    for i in range (0, b):
        multList.append(a * b)
    return multList

result = valor_multiplicado_longitud(5, 2)
print(result)
# Debe retornar: [10, 10]

result = valor_multiplicado_longitud(7, 5)
print(result)
# Debe retornar: [35, 35, 35, 35, 35]
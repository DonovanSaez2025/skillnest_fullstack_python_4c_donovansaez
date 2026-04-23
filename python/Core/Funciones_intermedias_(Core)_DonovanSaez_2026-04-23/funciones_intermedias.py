'''Aclaración: .items() rompe con el formato que nos pide skillnest para las salidas de datos,
así que solo fue usado en el bonus 3 ya que no nos daba formato que .items() rompía'''
# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]


# Lista de creadores de contenido en una plataforma de streaming
streamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]


# Eventos en distintas ciudades del mundo
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}


# Coordenadas de la sede de un torneo internacional
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]

# Ejercicios de modificación de datos
# 1. En puntajes, cambia el valor 300 por 600 (ajuste en los puntajes de la primera ronda).
puntajes[1][0] = 600
print(puntajes[1][0])

# 2. En streamers, cambia el nombre de ”GameNinjaPro” a ”EliteGamerX”.
streamers[0]["nombre"] = "EliteGamerX"
print(streamers[0]["nombre"])

# 3. En eventos, cambia la ciudad “Las Vegas” por “San Francisco”.
eventos["Estados Unidos"][2] = "San Francisco"
print(eventos["Estados Unidos"][2])

# 4. En ubicacion, cambia el valo de ”latitud” a 40.712776 (cambiando la sede del torneo a Nueva York).
ubicacion[0]["latitud"] = 40.712776
print(ubicacion[0]["latitud"])

# Ejercicios de recorrer datos
'''1. Crea la función iterar_diccionario(lista) que reciba una lista de diccionarios (como streamers)
y recorra cada uno, imprimiendo sus claves y valores.'''
def iterar_diccionario(lista):
    print("\nImprimiendo ejercicio 1:")
    for i in range(0, len(lista)):
        print(f"nombre - {lista[i]["nombre"]}, seguidores - {lista[i]["seguidores"]}")
iterar_diccionario(streamers)

'''2. Obtener valores de un diccionario creando la función obtener_valores(clave, lista) que reciba,
por una parte, una cadena con el nombre de una clave, por otra, una lista de diccionarios.
La función debe imprimir el valor asociado a esa clave en cada uno de los diccionarios.'''
def obtener_valores(clave, lista):
    print("\nImprimiendo ejercicio 2:")
    for i in range(0, len(lista)):
        print(streamers[i][clave])
    print("")
obtener_valores("nombre", streamers)
obtener_valores("seguidores", streamers)

'''3. Crea la función mostrar_informacion(diccionario), que reciba un diccionario en el que
los valores sean listas. La función debe, por una parte, imprimir el tamaño de la lista
y la clave en mayúsculas, por otra, imprimir cada elemento de la lista en líneas separadas.'''
def mostrar_informacion(diccionario):
    print("\nImprimiendo ejercicio 3:")
    print(f"{len(diccionario["Estados Unidos"])} CIUDADES_EVENTOS")
    for i in range(0, len(diccionario["Estados Unidos"])):
        print(diccionario["Estados Unidos"][i])
mostrar_informacion(eventos)

# Desafíos extras
datos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el puntaje de Pedro a 75
datos[2]["puntaje"] = 75
print(datos[2]["puntaje"])

# 2. Crear función que imprima: "Carlos obtuvo 80 puntos"
def puntajeObtenido(index, lista):
    print("\nImprimiendo ejercicio bonus 2:")
    print(f"{lista[index]["nombre"]} obtuvo {lista[index]["puntaje"]} puntos")
puntajeObtenido(0, datos)

# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores
def nombrePuntaje(lista):
    print("\nImprimiendo ejercicio bonus 3:")
    for i in range(0, len(lista)):
        for clave, valor in lista[i].items():
            print(f"{valor}")
nombrePuntaje(datos)
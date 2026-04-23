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

'''Crea la función iterar_diccionario(lista) que reciba una lista de diccionarios (como streamers)
y recorra cada uno, imprimiendo sus claves y valores.'''
def iterar_diccionario(listaStreamers):
    print("\nImprimiendo lista de streamers:")
    for i in range(0, len(listaStreamers)):
        print(f"nombre - {listaStreamers[i]["nombre"]}, seguidores - {listaStreamers[i]["seguidores"]}")
        
            
iterar_diccionario(streamers)
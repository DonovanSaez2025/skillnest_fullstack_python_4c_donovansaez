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
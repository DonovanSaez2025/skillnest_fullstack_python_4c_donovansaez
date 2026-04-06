'''
Datos primitivos
Estos son los elementos básicos de un lenguaje.
La mayoría de los lenguajes comparten estos en común.
'''

# Dato booleano: "True" o "False"
estaActivo = False
estaDespierto = True

# Datos numéricos: números enteros, decimal normal o flotante y números complejos
edad = 18
dinero = 20.55
pi = 3.1415
operatoria = dinero * pi

# Dato textual: String
nombre = "Ana"
apellido = "Ambár"
estado = 'bien'
frase = f"{nombre} {apellido} está {estado}"

# Datos compuestos: Array, tupla, diccionario
estudiantesPresentes = ["Don", "Cat", "Seb", "Mat", "Ran"] # Array
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre") # Tupla
personaCaract = { # Diccionario
    "nombre": "John",
    "edad": 18,
    "Altura": 1.90
}

# Imprimir datos
print((f"¿Está activo? Respuesta: {estaActivo}"))
print((f"¿Está despierto? Respuesta: {estaDespierto}"))
print((f"¿Edad? Respuesta: {edad}"))
print((f"¿Cuánto dinero tiene? Respuesta: {dinero}"))
print((f"¿Valor de PI? Respuesta: {pi}"))
print((f"Operatoria aleatoria: {operatoria}"))
print((f"¿Nombre? Respuesta: {nombre}"))
print((f"¿Apellido? Respuesta: {apellido}"))
print((f"¿Estado? Respuesta: {estado}"))
print((f"¿Frase? Respuesta: {frase}"))
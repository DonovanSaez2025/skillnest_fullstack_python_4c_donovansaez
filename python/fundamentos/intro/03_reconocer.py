"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random # Importa una librería para procesos aleatorios

nombre = "Frida Kahlo" # Se declara la variable tipo String llamada nombre
print(type(nombre)) # Se imprime en la consola el tipo de dato que es la variable nombre
print(len(nombre)) # Se imprime en la consola la longitud de la variable nombre

edad = 25 # Se declara la variable tipo INT llamada edad

if edad < 18: # Se establece condición IF comparando si edad es menor que 18
    print("Eres menor de edad.") # Imprime un mensaje
elif edad == 18: # Se establece subcondición ELIF comparando si edad es igual a 18
    print("Tienes 18 años.") # Imprime un mensaje
else: # Se establece subcondición ELSE
    print("Eres mayor de edad.") # Imprime un mensaje


frutas = ["manzana", "pera", "fresa"]
print(frutas[0])
frutas[0] = "banana"
frutas.append("uva")
frutas.remove("pera")


dimensiones = (200, 50)
print(dimensiones[0])


persona = {
   "nombre": "Carlos",
   "edad": 30
}
print(persona["nombre"])
persona["edad"] = 31
persona["ciudad"] = "Santiago"
del persona["ciudad"]


for i in range(5):
   if i == 2:
       continue
   if i == 4:
       break
   print(i)


contador = 0
while contador < 3:
   print(f"while contador es: {contador}")
   contador += 1


def saludar_usuario(nombre):
   return f"Hola, {nombre}"


print(saludar_usuario("Francisca"))
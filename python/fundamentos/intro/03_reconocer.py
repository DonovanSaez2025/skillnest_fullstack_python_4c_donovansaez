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

frutas = ["manzana", "pera", "fresa"] # Declara la variable tipo array llamada "frutas" con 3 items
print(frutas[0]) # Imprime el primer item de la variable frutas
frutas[0] = "banana" # Cambia el valor de la posición 0 de la variable frutas
frutas.append("uva") # Agrega un nuevo item tipo String de valor "uva" al final de la variable frutas
frutas.remove("pera") # Remueve la palabra "pera" del array

dimensiones = (200, 50) # Declara una variable tipo tupla (variable inmutable) llamada "dimensiones" con 2 items
print(dimensiones[0]) # Imprime el valor de la posición 0 de la variable dimensiones

persona = { # Declara una variable tipo diccionario (objeto) llamada persona con 2 items
    "nombre": "Carlos", # Se establece un item y se le asigna un valor
    "edad": 30 # Se establece un item y se le asigna un valor
} # Cierre del diccionario

print(persona["nombre"]) # Imprime en pantalla el valor del item "nombre" de la variable persona
persona["edad"] = 31 # Modifica el valor del item "edad" de la variable persona por el número 31
persona["ciudad"] = "Santiago" # Se añade el item "ciudad" a la variable "persona" y se le asigna un valor
del persona["ciudad"] # Se elimina el item completo

for i in range(5): # Se crea bucle con la variable i en rango desde 0 a 5
    
    if i == 2: # Se establece condición IF == 2
        continue # Ignora los procesos siguientes y continua
    if i == 4: # Se establece condición IF == 4
        break # Se rompe el bucle
    print(i) # Imprime el valor de la variable i

contador = 0 # Se declara la variable tipo INT llamada contador
while contador < 3: # Bucle while: mientras contador sea menor a 3 
    print(f"while contador es: {contador}") # Imprime el contador en un mensaje concatenado con fstring
    contador += 1 # Suma uno a la variable contador

def saludar_usuario(nombre): # Crea una función con un parámetro
    return f"Hola, {nombre}" # Retorna el paramétro concatenado con fstring

print(saludar_usuario("Francisca")) # Llama a la función saludar_usuario() enviandole el paramétro francisca e imprimiendo el valor retornado'''
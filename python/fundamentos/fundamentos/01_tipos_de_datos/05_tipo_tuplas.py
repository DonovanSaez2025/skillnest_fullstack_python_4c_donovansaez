#Tipos de tuplas
tupla_letras = ("a", "e", "i", "o", "u")
tupla_sin_parentesis = "a", "e", "i", "o", "u"

gato = ("Miau", 5, "persa", False)
print(gato[0]) #Imprime: Miau
#gato[0] = "Michi" ERROR: TypeError: 'tuple' object does not support item assignment

gato = gato + ("4.1",)
print(gato) #Imprime: ('Miu', 5, 'persa', False, '4.1')

def suma_multiplicacion(x, y):
    suma = x + y
    multiplicacion = x * y
    return (suma, multiplicacion)
print(suma_multiplicacion(2, 5))
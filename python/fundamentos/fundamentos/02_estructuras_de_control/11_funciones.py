def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
    resultado = num1 * num2     #instrucciones dentro de la función
    return resultado            #regresamos valor de resultado

resultado_multiplicacion = multiplicacion(5, 5) #Llamado a la función con argumentos 5 y 5
print(resultado_multiplicacion) #Se guarda en la variable el resultado que la función regresó. Imprime: 25

def buenos_dias(nombre):
    print("Buenos días " + nombre)
    
buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")

def buenos_dias(nombre):
    return "Buenos días "+nombre

#El valor de retorno de la función es "Buenos días Python",
# por lo que el valor de mi variable frase será ese

frase = buenos_dias("Python")
print(frase) #Imprime: Buenos días Python

def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

a = int(input("Ingresa un número: "))
b = int(input("Ingresa otro número: "))
print(multiplicacion(a, b))

def buenos_dias2(nombre):
    return "Buenos días " + nombre

frase = buenos_dias2("Python")
print(frase)

#Ejercicio de retorn ode valor.
#Crear una función que recibe una frase + un parámetro
#Devolver el valor de la frase completa e imprimir
def construirFrase(frase, palabra):
    return f"{frase} es el/la/los/las: {palabra}"
frase = input("Ingresa una frase que describa algo: ")
palabra = input("Ingresa qué es ese algo que has descrito: ")
print(construirFrase(frase, palabra))
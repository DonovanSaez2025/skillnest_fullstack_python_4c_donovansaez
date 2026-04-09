#Ejercicio 1: Números Pares Dinámicos
'''Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). 
El programa debe imprimir los primeros $n$ números pares positivos.'''
num = int(input("¿Cuántos números pares deseas ver? ")) #Pedir número al usuario
for i in range(num + 1):
    if i % 2 == 0:
        print(i)
        
#Ejercicio 2: Verificador de Edad y Acceso
'''Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+).
Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.'''
nacimiento = int(input("Ingresa tu año de nacimiento: "))
anioPresente = 2026
if nacimiento < 0:
    print("Ese no es un año válido")
else:
    edad = anioPresente - nacimiento
    if edad < 18 and edad >= 1:
        print(f"Tienes {edad} años, eres menor de edad, te faltan {18 - edad} años para ser adulto.")
    elif edad >= 18:
        print(f"Tienes {edad} años, ya eres mayor de edad.")
    
#Ejercicio 3: Calculadora de Descuentos
'''Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100,
aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final.'''
precio = float(input("Ingresa el precio del producto: "))
cantidad = int(input("Ingresa la cantidad del producto: "))
precioTotal = precio * cantidad
descuento = 0.15
if precioTotal > 100:
    subtotal = precioTotal - (precioTotal * descuento)
    #Los "$" son por signo dólar, no por confusión con JS
    print(f"Precio total: ${precioTotal}, se aplicó el descuento del 15% y se han descontado ${precioTotal * descuento}, el subtotal a pagar es ${subtotal}")
elif precioTotal <= 100:
    print(f"Precio a pagar: ${precioTotal}")

#Ejercicio 4: Clasificador de Números
'''Pide un número al usuario e indica si es: Positivo-Par,
Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.'''
num = int(input("Ingresa un número: "))
caract1 = ""
caract2 = ""

if num == 0:
    print("El número es 0")
elif num < 0:
    caract1 = "negativo"
    if num % 2 == 0:
        caract2 = "par"
    else:
        caract2 = "impar"
    print(f"El número {num} es {caract2} y {caract1}")
elif num > 0:
    caract1 = "positivo"
    if num % 2 == 0:
        caract2 = "par"
    else:
        caract2 = "impar"
    print(f"El número {num} es {caract2} y {caract1}")
        

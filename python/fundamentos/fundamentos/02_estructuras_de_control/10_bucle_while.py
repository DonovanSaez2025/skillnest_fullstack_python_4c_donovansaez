# while 3 < 5:
    #pass
    #Código que se ejecuta mientras la condición se cumpla

num = 0

while num < 4:
    print("bucle while -", num)
    num += 1
#Imprime: bucle while - 0, bucle while - 1, bucle while - 2, bucle while - 3

num = 0
while num < 4:
    print("bucle while -", num)
    num += 1
else:
    print("Acabamos de salir del bucle")

x = 1

while x > 2:
    print(x)
    x -= 1
    if x == 3:
        break
else: #Recuerda: Solo se ejecuta en una salida normal, NO en un break
    print("Sentencia final")

for i in range(10):
    print(i)
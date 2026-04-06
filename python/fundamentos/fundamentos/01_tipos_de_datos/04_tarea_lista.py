'''
Actividad: Gestor de inventario
'''

#1. Crear una lista llamada inventario con los siguientes articulos:
# "laptop", "ratón", "monitor", "cable hdmi"
inventario = ["laptop", "ratón", "monitor", "cable hdmi"]

#2. Agrega "impresora" y "teclado" al final de la lista con su método corresponiende.
inventario.append("impresora")
inventario.append("teclado")

#3. Usa la función integrada para mostrar cuantos elementos hay en la lista.
print(f"Cantidad de elementos en el inventario: {len(inventario)}")

#4. Modifica "teclado" por "teclado mecánico"
inventario[5] = "teclado mecánico"

#5. Crea la lista "promoción" que debe contener solo los 3 primeros elementos de la lista "inventario"
promocion = inventario[:3]

#6. Mostrar la lista de inventario ordenado alfabeticamente
print(sorted(inventario))

#7. Elimina el último elemento de la lista inventario y muestralo en pantalla
print(f"Elemento eliminado: {inventario.pop()}")
print(f"Inventario actual: {inventario}")
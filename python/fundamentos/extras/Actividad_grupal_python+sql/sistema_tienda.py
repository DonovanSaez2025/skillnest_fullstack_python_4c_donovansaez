import os
class Producto:
    tienda = "Porky's Big Shots"
    
    def __init__(self, nombre_producto, stock_producto, precio_producto):
        self.nombre_producto = nombre_producto
        self.stock_producto = stock_producto
        self.precio_producto = precio_producto
        
    def mostrar_producto(self):
        pass
    
    def actualizar_stock(self):
        pass

class Cliente:
    tienda = "Porky's Big Shots"
    banco = "Bancoestado"
    
    def __init__(self, nombre_cliente, direccion_cliente):
        self.nombre_cliente = nombre_cliente
        self.direccion_cliente = direccion_cliente
        self.saldo_prendiente = 0
    
    def realizar_compra(self, nombres_productos):
        pass
    
    def pagar_saldo(self, monto):
        pass
    
    def actualizar_direccion(self):
        pass
    
    def mostrar_cliente(self):
        pass

class Venta:
    tienda = "Porky's Big Shots"
    banco = "Bancoestado"
    
    def __init__(self, nombre_productos, nombre_cliente, fecha_venta, precio_total):
        self.nombre_productos = nombre_productos
        self.nombre_cliente = nombre_cliente
        self.fecha_venta = fecha_venta
        self.precio_total = precio_total
        
    def registrar_venta(self):
        pass
    
    def calcular_total(self):
        pass
    
# Crear instancias
#Productos
prod01 = Producto("Laptop", 10, 199.90)
prod02 = Producto("Mouse", 5, 15.99)
prod03 = Producto("Teclado", 20, 37.99)
prod04 = Producto("Parlantes", 50, 49.99)
prod05 = Producto("Disco duro externo 2tb", 100, 229.99)

#Clientes
clie01 = Cliente("Donovan", "Llo Lleó 1948, San Ramón")
clie02 = Cliente("MatildeX", "Doñihue 2945, San Ramón")
clie03 = Cliente("Matías", "Santa Rosa 1894, San Ramón")
clie04 = Cliente("Randy", "Américo Vespucio 2755, San Ramón")
clie05 = Cliente("Martín", "Doñihue 2815, San Ramón")

# Función para limpiar la consola
def limpiarConsola():
    os.system('cls')

# Menu while
while True:
    print("--- Actividad grupal sistema_tiendas ---")
    print("--- 1: mostrar producto ---")
    
    opcion = input("Ingresa una opción: ")
    
    if opcion == "1":
        limpiarConsola()
        
    if opcion == "0":
        limpiarConsola()
        break
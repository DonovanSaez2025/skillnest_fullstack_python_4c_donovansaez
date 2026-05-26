import os
class Producto:
    tienda = "Porky's Big Shots"
    listaProductos = []
    
    def __init__(self, nombre_producto, stock_producto, precio_producto):
        self.nombre_producto = nombre_producto
        self.stock_producto = stock_producto
        self.precio_producto = precio_producto
        Producto.listaProductos.append(nombre_producto)
        
    def mostrar_producto(self):
        print(f"\nMostrando información del producto '{self.nombre_producto}'")
        print(f"Nombre del producto: {self.nombre_producto}")
        print(f"Stock del producto: {self.stock_producto}")
        print(f"Precio unitario del producto: {self.precio_producto}\n")
    
    def actualizar_stock(self, cantidad):
        print("Actualizando stock del producto...")
        self.stock_producto += cantidad
        print(f"Nuevo stock de {self.nombre_producto}: {self.stock_producto}\n")

class Cliente:
    tienda = "Porky's Big Shots"
    banco = "Bancoestado"
    listaClientes = []
    
    def __init__(self, nombre_cliente, direccion_cliente):
        self.nombre_cliente = nombre_cliente
        self.direccion_cliente = direccion_cliente
        self.saldo_pendiente = 0
        Cliente.listaClientes.append(self.nombre_cliente)
    
    def realizar_compra(self, nombre_producto, cantidad):
        precio_final = 0.0
        if nombre_producto == "Laptop":
            print(f"\nComprando {cantidad} {nombre_producto}/s...")
            prod01.stock_producto -= cantidad
            precio_final += prod01.precio_producto * cantidad
            self.saldo_pendiente += precio_final
            print(f"Precio final: {precio_final}\nSaldo a pagar total: {self.saldo_pendiente}\n")
        elif nombre_producto == "Mouse":
            print(f"\nComprando {cantidad} {nombre_producto}/s...")
            prod02.stock_producto -= cantidad
            precio_final += prod02.precio_producto * cantidad
            self.saldo_pendiente += precio_final
            print(f"Precio final: {precio_final}\nSaldo a pagar total: {self.saldo_pendiente}\n")
        elif nombre_producto == "Disco duro externo 2tb":
            print(f"\nComprando {cantidad} {nombre_producto}/s...")
            prod03.stock_producto -= cantidad
            precio_final += prod03.precio_producto * cantidad
            self.saldo_pendiente += precio_final
            print(f"Precio final: {precio_final}\nSaldo a pagar total: {self.saldo_pendiente}\n")
        venta_hecha = Venta(nombre_producto, cantidad, self.nombre_cliente, "26/05/2026", precio_final)
        
    def pagar_saldo(self, monto):
        if monto > self.saldo_pendiente:
            print("Error: monto más alto que el saldo pendiente.")
        elif monto < self.saldo_pendiente:
            self.saldo_pendiente -= monto
            print(f"Parte del saldo pendiente pagado, pero aún quedan ${self.saldo_pendiente} por pagar.")
        elif monto == self.saldo_pendiente:
            self.saldo_pendiente -= monto
            print("Saldo totalmente pagado.")
    
    def actualizar_direccion(self, nueva_direccion):
        self.direccion_cliente = nueva_direccion
        print("Dirección actualizada.")
    
    def mostrar_cliente(self):
        print("Mostrando información del cliente...")
        print(f"Nombre: {self.nombre_cliente}")
        print(f"Dirección: {self.direccion_cliente}")

class Venta:
    tienda = "Porky's Big Shots"
    banco = "Bancoestado"
    
    def __init__(self, nombre_producto, cantidad, nombre_cliente, fecha_venta, precio_total):
        self.nombre_productos = nombre_producto
        self.cantidad = cantidad
        self.nombre_cliente = nombre_cliente
        self.fecha_venta = fecha_venta
        self.precio_total = precio_total
        
    def registrar_venta(self):
        pass
    
    def calcular_total(self):
        pass
    
# Crear instancias
#Productos
prod01 = Producto("Laptop", 10, 199.99)
prod02 = Producto("Mouse", 5, 15.99)
prod03 = Producto("Disco duro externo 2tb", 100, 229.99)

#Clientes
clie01 = Cliente("Donovan", "Llo Lleó 1948, San Ramón")
clie02 = Cliente("MatildeX", "Doñihue 2945, San Ramón")
clie03 = Cliente("Randy", "Américo Vespucio 2755, San Ramón")

# Función para limpiar la consola
def limpiarConsola():
    os.system('cls')

# Menu while
while True:
    print("--- Actividad grupal sistema_tiendas ---")
    print("--- 1: Mostrar producto ---")
    print("--- 2: Actualizar stock de un producto ---")
    print("--- 3: Comprar productos ---")
    
    opcion = input("Ingresa una opción: ")
    
    if opcion == "1":
        limpiarConsola()
        print(f"Productos:\n- {"\n- ".join(Producto.listaProductos)}")
        ins = input("\nIngresa el nombre exacto de un producto: ")
        
        if ins == "Laptop":
            prod01.mostrar_producto()
        elif ins == "Mouse":
            prod02.mostrar_producto()
        elif ins == "Disco duro externo 2tb":
            prod03.mostrar_producto()
        else:
            print("Producto inválido.\n")
    elif opcion == "2":
        limpiarConsola()
        print(f"Productos:\n- {"\n- ".join(Producto.listaProductos)}")
        ins = input("\nIngresa el nombre exacto de un producto: ")
        if ins == "Laptop":
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad > 0:
                prod01.actualizar_stock(cantidad)
            else:
                print("Inválido.\n")
        elif ins == "Mouse":
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad > 0:
                prod02.actualizar_stock(cantidad)
            else:
                print("Inválido.\n")
        elif ins == "Disco duro externo 2tb":
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad > 0:
                prod03.actualizar_stock(cantidad)
            else:
                print("Inválido.\n")
        else:
            print("Producto inválido.\n")
    elif opcion == "3":
        limpiarConsola()
        print(f"Clientes:\n- {"\n- ".join(Cliente.listaClientes)}")
        ins = input("Ingresa tu nombre: ")
        if ins == "Donovan":
            print("\nProductos:")
            print(f"{prod01.nombre_producto} - Stock: {prod01.stock_producto}")
            print(f"{prod02.nombre_producto} - Stock: {prod02.stock_producto}")
            print(f"{prod03.nombre_producto} - Stock: {prod03.stock_producto}")
            nombre_prod = input("Ingresa el nombre del producto: ")
            if nombre_prod in Producto.listaProductos:
                cantidad = int(input("Ingresa la cantidad que quieras de ese producto: "))
                if nombre_prod == "Laptop":
                    if prod01.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie01.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Mouse":
                    if prod02.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie01.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Disco duro externo 2tb":
                    if prod03.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie01.realizar_compra(nombre_prod, cantidad)
            else:
                print("Producto inválido.")
        elif ins == "MatildeX":
            print("\nProductos:")
            print(f"{prod01.nombre_producto} - Stock: {prod01.stock_producto}")
            print(f"{prod02.nombre_producto} - Stock: {prod02.stock_producto}")
            print(f"{prod03.nombre_producto} - Stock: {prod03.stock_producto}")
            nombre_prod = input("Ingresa el nombre del producto: ")
            if nombre_prod in Producto.listaProductos:
                cantidad = int(input("Ingresa la cantidad que quieras de ese producto: "))
                if nombre_prod == "Laptop":
                    if prod01.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie02.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Mouse":
                    if prod02.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie02.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Disco duro externo 2tb":
                    if prod03.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie02.realizar_compra(nombre_prod, cantidad)
            else:
                print("Producto inválido.")
        elif ins == "Randy":
            print("\nProductos:")
            print(f"{prod01.nombre_producto} - Stock: {prod01.stock_producto}")
            print(f"{prod02.nombre_producto} - Stock: {prod02.stock_producto}")
            print(f"{prod03.nombre_producto} - Stock: {prod03.stock_producto}")
            nombre_prod = input("Ingresa el nombre del producto: ")
            if nombre_prod in Producto.listaProductos:
                cantidad = int(input("Ingresa la cantidad que quieras de ese producto: "))
                if nombre_prod == "Laptop":
                    if prod01.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie03.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Mouse":
                    if prod02.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie03.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Disco duro externo 2tb":
                    if prod03.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie03.realizar_compra(nombre_prod, cantidad)
            else:
                print("Producto inválido.")
        else:
            print("Nombre inválido.")
    elif opcion == "0":
        limpiarConsola()
        break
    else:
        print("Opción inválida.\n")
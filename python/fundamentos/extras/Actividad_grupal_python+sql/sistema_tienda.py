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
        self.saldo_prendiente = 0
        Cliente.listaClientes.append(self.nombre_cliente)
    
    def realizar_compra(self, nombre_producto, cantidad):
        precio_final = 0.0
        if nombre_producto == "Laptop":
            print(f"\nComprando {cantidad} {nombre_producto}/s...")
            prod01.stock_producto -= cantidad
            precio_final += prod01.precio_producto * cantidad
            self.saldo_prendiente += precio_final
            print(f"Precio final: {precio_final}\nSaldo a pagar total: {self.saldo_prendiente}\n")
        elif nombre_producto == "Mouse":
            print(f"\nComprando {cantidad} {nombre_producto}/s...")
            prod02.stock_producto -= cantidad
            precio_final += prod02.precio_producto * cantidad
            self.saldo_prendiente += precio_final
            print(f"Precio final: {precio_final}\nSaldo a pagar total: {self.saldo_prendiente}\n")
        elif nombre_producto == "Teclado":
            print(f"\nComprando {cantidad} {nombre_producto}/s...")
            prod03.stock_producto -= cantidad
            precio_final += prod03.precio_producto * cantidad
            self.saldo_prendiente += precio_final
            print(f"Precio final: {precio_final}\nSaldo a pagar total: {self.saldo_prendiente}\n")
        elif nombre_producto == "Parlantes":
            print(f"\nComprando {cantidad} {nombre_producto}/s...")
            prod04.stock_producto -= cantidad
            precio_final += prod04.precio_producto * cantidad
            self.saldo_prendiente += precio_final
            print(f"Precio final: {precio_final}\nSaldo a pagar total: {self.saldo_prendiente}\n")
        elif nombre_producto == "Disco duro externo 2tb":
            print(f"\nComprando {cantidad} {nombre_producto}/s...")
            prod05.stock_producto -= cantidad
            precio_final += prod05.precio_producto * cantidad
            self.saldo_prendiente += precio_final
            print(f"Precio final: {precio_final}\nSaldo a pagar total: {self.saldo_prendiente}\n")
        venta_hecha = Venta(nombre_producto, cantidad, self.nombre_cliente, "25/05/2026", precio_final)
        
    def pagar_saldo(self, monto):
        pass
    
    def actualizar_direccion(self):
        pass
    
    def mostrar_cliente(self):
        pass

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
        elif ins == "Teclado":
            prod03.mostrar_producto()
        elif ins == "Parlantes":
            prod04.mostrar_producto()
        elif ins == "Disco duro externo 2tb":
            prod05.mostrar_producto()
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
                print("Inválido.")
        elif ins == "Mouse":
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad > 0:
                prod02.actualizar_stock(cantidad)
            else:
                print("Inválido.")
        elif ins == "Teclado":
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad > 0:
                prod03.actualizar_stock(cantidad)
            else:
                print("Inválido.")
        elif ins == "Parlantes":
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad > 0:
                prod04.actualizar_stock(cantidad)
            else:
                print("Inválido.")
        elif ins == "Disco duro externo 2tb":
            cantidad = int(input("Ingresa la cantidad de stock a sumar: "))
            if cantidad > 0:
                prod05.actualizar_stock(cantidad)
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
            print(f"{prod04.nombre_producto} - Stock: {prod04.stock_producto}")
            print(f"{prod05.nombre_producto} - Stock: {prod05.stock_producto}")
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
                elif nombre_prod == "Teclado":
                    if prod03.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie01.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Parlantes":
                    if prod04.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie01.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Disco duro externo 2tb":
                    if prod05.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie01.realizar_compra(nombre_prod, cantidad)
            else:
                print("Producto inválido.")
        if ins == "MatildeX":
            print("\nProductos:")
            print(f"{prod01.nombre_producto} - Stock: {prod01.stock_producto}")
            print(f"{prod02.nombre_producto} - Stock: {prod02.stock_producto}")
            print(f"{prod03.nombre_producto} - Stock: {prod03.stock_producto}")
            print(f"{prod04.nombre_producto} - Stock: {prod04.stock_producto}")
            print(f"{prod05.nombre_producto} - Stock: {prod05.stock_producto}")
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
                elif nombre_prod == "Teclado":
                    if prod03.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie02.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Parlantes":
                    if prod04.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie02.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Disco duro externo 2tb":
                    if prod05.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie02.realizar_compra(nombre_prod, cantidad)
            else:
                print("Producto inválido.")
        if ins == "Matías":
            print("\nProductos:")
            print(f"{prod01.nombre_producto} - Stock: {prod01.stock_producto}")
            print(f"{prod02.nombre_producto} - Stock: {prod02.stock_producto}")
            print(f"{prod03.nombre_producto} - Stock: {prod03.stock_producto}")
            print(f"{prod04.nombre_producto} - Stock: {prod04.stock_producto}")
            print(f"{prod05.nombre_producto} - Stock: {prod05.stock_producto}")
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
                elif nombre_prod == "Teclado":
                    if prod03.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie03.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Parlantes":
                    if prod04.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie03.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Disco duro externo 2tb":
                    if prod05.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie03.realizar_compra(nombre_prod, cantidad)
            else:
                print("Producto inválido.")
        if ins == "Randy":
            print("\nProductos:")
            print(f"{prod01.nombre_producto} - Stock: {prod01.stock_producto}")
            print(f"{prod02.nombre_producto} - Stock: {prod02.stock_producto}")
            print(f"{prod03.nombre_producto} - Stock: {prod03.stock_producto}")
            print(f"{prod04.nombre_producto} - Stock: {prod04.stock_producto}")
            print(f"{prod05.nombre_producto} - Stock: {prod05.stock_producto}")
            nombre_prod = input("Ingresa el nombre del producto: ")
            if nombre_prod in Producto.listaProductos:
                cantidad = int(input("Ingresa la cantidad que quieras de ese producto: "))
                if nombre_prod == "Laptop":
                    if prod01.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie04.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Mouse":
                    if prod02.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie04.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Teclado":
                    if prod03.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie04.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Parlantes":
                    if prod04.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie04.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Disco duro externo 2tb":
                    if prod05.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie05.realizar_compra(nombre_prod, cantidad)
            else:
                print("Producto inválido.")
        if ins == "Martín":
            print("\nProductos:")
            print(f"{prod01.nombre_producto} - Stock: {prod01.stock_producto}")
            print(f"{prod02.nombre_producto} - Stock: {prod02.stock_producto}")
            print(f"{prod03.nombre_producto} - Stock: {prod03.stock_producto}")
            print(f"{prod04.nombre_producto} - Stock: {prod04.stock_producto}")
            print(f"{prod05.nombre_producto} - Stock: {prod05.stock_producto}")
            nombre_prod = input("Ingresa el nombre del producto: ")
            if nombre_prod in Producto.listaProductos:
                cantidad = int(input("Ingresa la cantidad que quieras de ese producto: "))
                if nombre_prod == "Laptop":
                    if prod01.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie05.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Mouse":
                    if prod02.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie05.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Teclado":
                    if prod03.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie05.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Parlantes":
                    if prod04.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie05.realizar_compra(nombre_prod, cantidad)
                elif nombre_prod == "Disco duro externo 2tb":
                    if prod05.stock_producto < cantidad:
                        print("No hay suficiente stock.")
                    else:
                        clie05.realizar_compra(nombre_prod, cantidad)
            else:
                print("Producto inválido.")
    elif opcion == "0":
        limpiarConsola()
        break
    else:
        print("Opción inválida.\n")
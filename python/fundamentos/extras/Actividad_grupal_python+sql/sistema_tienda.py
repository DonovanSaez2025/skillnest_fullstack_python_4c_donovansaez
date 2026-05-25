class Producto:
    tienda = "Porky's Big Shots"
    
    def __innit__(self, nombre_producto, stock_producto, precio_producto):
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
    
    def __innit__(self, nombre_cliente, direccion_cliente):
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
    
    def __innit__(self, nombre_productos, nombre_cliente, fecha_venta, precio_total):
        self.nombre_productos = nombre_productos
        self.nombre_cliente = nombre_cliente
        self.fecha_venta = fecha_venta
        self.precio_total = precio_total
        
    def registrar_venta(self):
        pass
    
    def calcular_total(self):
        pass
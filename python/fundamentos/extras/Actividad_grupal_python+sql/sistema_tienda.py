class Producto:
    tienda = "Porky's Big Shots"
    
    def __innit__(self, nombre, stock, precio):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
        
    def mostrar_producto(self):
        pass
    
    def actualizar_stock(self):
        pass

class Cliente:
    tienda = "Porky's Big Shots"
    banco = "Bancoestado"
    
    def __innit__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.saldo_prendiente = 0
        pass

class Venta:
    def __innit__(self, nombre_producto, nombre_cliente, fecha_venta):
        self.nombre_producto = nombre_producto
        self.nombre_cliente = nombre_cliente
        self.fecha_venta = fecha_venta
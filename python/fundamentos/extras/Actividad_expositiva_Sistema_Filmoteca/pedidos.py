class Pedido:
    pedidos = []
    
    def __init__(self, ID, usuario_ID, pelicula_ID, cantidad, precio_total, fecha_venta):
        self.ID = ID
        self.usuario_ID = usuario_ID
        self.pelicula_ID = pelicula_ID
        self.cantidad = cantidad
        self.precio_total = precio_total
        self.fecha_venta = fecha_venta
        Pedido.listarPedido(self.ID, self.usuario_ID, self.pelicula_ID, self.cantidad, self.precio_total, self.fecha_venta)
    
    @classmethod
    def listarPedido(cls, ID, u_ID, p_ID, cant, prec_t, fecha):
        cls.pedidos.append({"ID": ID, "Usuario ID": u_ID, "Película ID": p_ID,
                            "Cantidad": cant, "Precio final": prec_t, "Fecha venta": fecha})
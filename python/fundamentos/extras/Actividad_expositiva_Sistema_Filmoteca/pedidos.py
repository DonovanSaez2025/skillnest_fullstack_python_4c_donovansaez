from conexion import Conexion
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
        # Contacto SQL
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """INSERT INTO pedidos(id_usuario, precio_total, created_by)
        VALUES(%s, %s, 1)"""
        valores = (u_ID, prec_t)
        cursor.execute(sql, valores)
        sql = """INSERT INTO detalles_pedidos(id_pedido, id_pelicula, cantidad)
        VALUES(%s, %s, %s)"""
        valores = (ID, p_ID, cant)
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
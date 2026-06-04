class Usuario:
    usuarios = []
    tipo_usuario = ["Administrador", "Usuario"]
    
    def __init__(self, ID, username, email, password, tipo_usuario_ID):
        self.ID = ID
        self.username = username
        self.email = email
        self.password_hash = password
        self.tipo_usuario = tipo_usuario_ID
        self.saldo_pendiente = 0
        Usuario.usuarios.append(self.username)
        
    def realizar_pedido(self, pelicula, cantidad, precio):
        print("Comprando película...")
        
    def pagar_saldo(self, monto):
        if monto > self.saldo_pendiente:
            print("Error: monto más alto que el saldo a pagar.")
        else:
            print("Pagando saldo...")
            self.saldo_pendiente -= monto
            if self.saldo_pendiente > 0:
                print("Saldo totalmente pagado.")
            else:
                print(f"Parte del saldo pagado, pero aún quedan ${self.saldo_pendiente} por pagar")
    
    def cambiar_contrasena(self, nueva_contrasena):
        print("Actualizando contraseña...")
        self.password_hash = nueva_contrasena
        print("Contraseña actualizada.")
    
    def mostrar_usuarios(self):
        print("Imprimiendo información del usuario...")
        print(f"Nombre de usuario: {self.username}")
        print(f"Email: {self.username}")
        print(f"Tipo de usuario: {self.tipo_usuario}")
        print(f"Saldo pendiente: {self.saldo_pendiente}")
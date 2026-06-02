class Usuario:
    usuarios = []
    
    def __init__(self, username, email, password, tipo_usuario):
        self.username = username
        self.email = email
        self.password_hash = password
        self.tipo_usuario = tipo_usuario
        self.saldo_pendiente = 0
        Usuario.usuarios.append(self.username)
        
    def realizar_pedido(self, pelicula, cantidad):
        pass
    
    def pagar_saldo(self, monto):
        pass
    
    def cambiar_contrasena(self, nueva_contrasena):
        pass
    
    def mostrar_usuarios(self):
        print("Imprimiendo información del usuario...")
        print(f"Nombre de usuario: {self.username}")
        print(f"Email: {self.username}")
        print(f"Tipo de usuario: {self.tipo_usuario}")
        print(f"Saldo pendiente: {self.saldo_pendiente}")
        
# Crear instancias
user1 = Usuario("SuperDONO17", "donovansaez@liceovvh.cl", "JAOSF)=/JF", "Administrador")
user2 = Usuario("IncrediJavi", "javierazapata@liceovvh.cl", "nsKSJ=(/!/%", "Usuario")
user3 = Usuario("MegaDav", "davidtobar@liceovvh.cl", "NAu9!)47", "Usuario")
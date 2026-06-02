class Usuario:
    usuarios = []
    
    def __init__(self, username, email, password, tipo_usuario):
        self.username = username
        self.email = email
        self.password_hash = password
        self.tipo_usuario = tipo_usuario
        Usuario.usuarios.append(self.username)
    
    def mostrar_usuarios():
        print("Imprimiendo información del usuario...")
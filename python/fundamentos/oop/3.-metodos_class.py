class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
        return self
    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto
        return self
    def mostrar_saldo_usuario(self):
        print(self.saldo_pagar)
    def aumentar_credito(self, monto):
        self.limite_credito += monto
    def cambiar_email(self, nuevoemail):
        self.email = nuevoemail

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")
donovan = Usuario("Donovan", "Sáez", "donovansaez@liceovvh.cl")
    
miyagi.hacer_compra(150).hacer_compra(300).pagar_tarjeta(50).mostrar_saldo_usuario()
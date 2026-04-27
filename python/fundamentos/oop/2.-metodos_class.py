class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
    def aumentar_credito(self, monto):
        self.limite_credito += monto
    def cambiar_email(self, nuevoemail):
        self.email = nuevoemail

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")
donovan = Usuario("Donovan", "Sáez", "donovansaez@liceovvh.cl")

# Compras miyagi
print("Compras de Miyagi ")
primeracompra = 2000
miyagi.hacer_compra(primeracompra)
print(f"Primera compra de {miyagi.nombre}: ${primeracompra}")
segundacompra = 300
miyagi.hacer_compra(segundacompra)
print(f"Segunda compra de {miyagi.nombre}: ${segundacompra}")
# Imprimir cuanto crédito le queda
print(f"Crédito disponible de {miyagi.nombre}: #{miyagi.limite_credito - miyagi.saldo_pagar}")

# Compras daniel
print("Compras de Daniel")
daniel.hacer_compra(45)
print(daniel.saldo_pagar)

#Tarea
'''
1. - Crear un nuevo método que permita aumentar el límite de crédito.
- imprimir el nuevo limite.
2. - Crear método que permita cambiar el correo.
- Mostrar el nuevo correo.
'''
# 1. aumentar limite del crédito
instancia = input("Selecciona una instancia (miyagi, daniel): ")
if instancia == "miyagi": 
    monto = int(input("Ingresa un monto de dinero: "))
    miyagi.aumentar_credito(monto)
    print(f"Nuevo límite de crédito para {miyagi.nombre}: ${miyagi.limite_credito}")
elif instancia == "daniel":
    monto = int(input("Ingresa un monto de dinero: "))
    daniel.aumentar_credito(monto)
    print(f"Nuevo límite de crédito para {daniel.nombre}: ${daniel.limite_credito}")
    
# 2. cambiar el correo
instancia = input("Selecciona una instancia(miyagi, daniel): ")
if instancia == "miyagi": 
    nuevocorreo = input("Ingresa un nuevo correo electrónico: ")
    miyagi.cambiar_email(nuevocorreo)
    print(f"Nuevo correo electrónico para {miyagi.nombre}: {miyagi.email}")
elif instancia == "daniel":
    nuevocorreo = input("Ingresa un nuevo correo electrónico: ")
    daniel.cambiar_email(nuevocorreo)
    print(f"Nuevo correo electrónico para {daniel.nombre}: {daniel.email}")
    
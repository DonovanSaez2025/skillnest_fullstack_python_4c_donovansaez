#Creación de la clase usuario - Entidad
class Usuario:
    def __init__(self): #Constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

#Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
donovan = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre)
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

#Nuevos valores asignaros a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000

print(daniel.nombre)
print(daniel.apellido)
print(daniel.email)
print(daniel.limite_credito)
print(daniel.saldo_pagar)

#Valores a nueva instancia
donovan.nombre = "Donovan"
donovan.apellido = "Sáez"
donovan.email = "donovansaez@liceovvh.cl"
donovan.limite_credito = 90000000
donovan.saldo_pagar = 10000

#Imprimir nombre de cada instancia
print(miyagi.nombre)
print(daniel.nombre)
print(donovan.nombre)
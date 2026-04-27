class Usuario:
    def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar

#Creación de las instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 30000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 100000, 300000)
donovan = Usuario("Donovan", "Sáez", "donovan@liceovvh.cl", 90000000, 10000)

#Imprimir valores
print(miyagi.nombre)
print(daniel.nombre)
print(miyagi.limite_credito)
print(daniel.limite_credito)

#-------------------------------------
#--- Tarea rápid
'''
- Crear una clase estudiante y asignarle los siguientes atributos: 
    (rut, nombre, apellido, especialidad, fecha_nacimiento)
- Crear 3 instancias para la clase con distintos estudiantes
- Imprimir el nombre y apellido concatenado y su especialidad
'''
#Crear clase
class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nacimiento):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nacimiento = fecha_nacimiento

#Crear instancias
matias = Estudiante("22847947-4", "Matias", "Rios", "programación", "02/05/2008")
julio = Estudiante("22857978-4", "Julio", "Cesar", "logistica", "08/04/2008")
tania = Estudiante("22851886-4", "Tania", "Ramirez", "contabilidad", "25/12/2007")

#Imprimir
print(f"Estudiante 1: {matias.nombre} {matias.apellido} de la especialidad de {matias.especialidad}.")
print(f"Estudiante 2: {julio.nombre} {julio.apellido} de la especialidad de {julio.especialidad}.")
print(f"Estudiante 3: {tania.nombre} {tania.apellido} de la especialidad de {tania.especialidad}.")
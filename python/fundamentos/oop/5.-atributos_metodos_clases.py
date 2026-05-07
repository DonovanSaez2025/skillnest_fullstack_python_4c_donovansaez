#Atributos, métodos de clase, métodos estáticos

#Definir clase
class Estudiante:
    #Atributo de clase
    colegio = "Liveo Vate Vicente Huidrobro"
    #Lista de estudiante
    estudianteLista = []
    
    #Método constructor
    def __init__(self, nombre, nota):
        #Atributos de instancia
        self.nombre = nombre
        self.nota = nota
        
        #Agregar elementos a la lista de estudiantes
        Estudiante.estudianteLista.append(self)
        
    #Método de instancia
    def mostrar_info(self):
            print(f"\nNombre: {self.nombre}\nNota: {self.nota}")
            
    #Método de clase: Usa "cls" porque trabaja con la información de la clase
    @classmethod #Cambiar nombre del colegio
    def cambiarColegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre
    
    @classmethod #Contar la cantidad de estudiantes existentes
    def cantidadEstudiantes(cls):
        return len(cls.estudianteLista)

    #Método estático: no usa CLS ni self, solo parámetros
    @staticmethod #Válidar nota
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False
    
#Creación de objetos (instancias)
e1 = Estudiante("Donovan", 4.0)
e2 = Estudiante("Randy", 7.0)
e3 = Estudiante("Martín", 3.9)

#Uso de métodos de instancia
print("\n== MÉTODO DE INSTANCIA ==")
#Mostrar datos de estudiantes
e1.mostrar_info()
e2.mostrar_info()
e3.mostrar_info()

#Usar atributos de clase
print("\n== ATRIBUTO DE CLASE ==")
print(e1.colegio)
print(e2.colegio)
print(e3.colegio)

#Uso de método de clase
print("\n== Método de clase ==")
Estudiante.cambiarColegio("Purkuyen") #Cambia a todas las instancias
e2.colegio = "VVH" #Cambia directamente al estudiante 1
print(e1.colegio)
print(e2.colegio)
print(e3.colegio)

#Contar estudiantes
print("\n== Contar estudiantes ==")
print(f"Total de estudiantes: {Estudiante.cantidadEstudiantes()}")

#Método estático
print("\n== Método Estático ==")
print(f"¿{e1.nombre} aprueba?")
print(Estudiante.aprobar(e1.nota))
print(f"¿{e2.nombre} aprueba?")
print(Estudiante.aprobar(e2.nota))
print(f"¿{e3.nombre} aprueba?")
print(Estudiante.aprobar(e3.nota))

#Función repaso.
#Crear una función que válide usuario y contraseña.
def validador(user, password):
    if user == "matias123" and password == "fabianinmortal":
        print(f"Bienvenido {user}!")
        return True
    else:
        print("Acceso denegado.")
        return False
    
def enviarDatos():
    username = input("Ingresa tu usuario: ").strip()
    password = input("Ingresa tu contraseña: ").strip()
    validador(username, password)
enviarDatos()
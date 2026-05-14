class CafeteriaCliente:
    membresias_validas = ["Bronce", "Plata", "Oro"]
    
    total_clientes = 0
    def __init__(self, nombre, puntos_acumulados=0, saldo_pendiente=0, tipo_membresia="Bronce"):

        self.nombre = nombre

        # Todo:
        self.puntos_acumulados = puntos_acumulados
        self.saldo_pendiente = saldo_pendiente
        self.tipo_membresia = tipo_membresia
        # Crear los atributos faltantes
        
        CafeteriaCliente.total_clientes += 1
    
    def realizar_compra(self, monto):
        
        # Todo:
        self.saldo_pendiente += monto
        # Aumentar saldo pendiente

        # Todo:
        i = monto // 1000
        while i > 0:
            self.puntos_acumulados += 10
            i-=1
        # Aumentar puntos

        print(f"{self.nombre} realizó una compra.")
        return self
        
    def pagar_saldo(self, monto):

        # Todo:
        if self.saldo_pendiente == 0:
            print("No tienes un saldo por pagar.")
        elif monto > self.saldo_pendiente:
            print("Error: se está pagando una cantidad mayor al saldo pendiente, no se puede completar el pago.")
        elif monto <= self.saldo_pendiente:
            self.saldo_pendiente -= monto
        
        if self.saldo_pendiente > 0:
            print(f"Aún queda ${self.saldo_pendiente} por pagar.")
        else:
            print("Saldo totalmente pagado.")
        # Validar el pago
        return self
    
    @classmethod
    def mostrar_total_clientes(cls):

        # Todo
        print(f"Total de clientes: {cls.total_clientes}")
    
    @staticmethod
    def validar_membresia(tipo):

        # Todo
        if tipo in CafeteriaCliente.membresias_validas:
            print(f"{tipo} es una membresía válida.")
            return True
        else:
            print(f"{tipo} es una membresía inválida.")
            return False
        
    def mostrar_informacion(self):
        print(f"\nMostrando información de {self.nombre}: ")
        print(f"Nombre: {self.nombre}")
        print(f"Puntos acumulados: {self.puntos_acumulados}")
        print(f"Saldo pendiente: ${self.saldo_pendiente}")
        print(f"Tipo de membresía: {self.tipo_membresia}")

donovan = CafeteriaCliente("Donovan", 0, 0, "Bronce")
sebastian = CafeteriaCliente("Sebastián", 0, 0, "Plata")
randy = CafeteriaCliente("Randy", 0, 0, "Oro")

donovan.realizar_compra(3520).pagar_saldo(2000)
sebastian.realizar_compra(4000).pagar_saldo(5000)
randy.mostrar_total_clientes()

donovan.validar_membresia("Bronce")
sebastian.validar_membresia("Diamante")
randy.mostrar_informacion()
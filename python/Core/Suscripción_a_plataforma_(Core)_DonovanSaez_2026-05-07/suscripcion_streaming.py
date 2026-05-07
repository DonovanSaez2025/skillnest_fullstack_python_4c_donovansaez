class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}
    
    def __init__(self, usuario, saldo_pendiente, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = SuscripcionStreaming.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = saldo_pendiente

    def realizar_pago(self, monto):
        #Reduce el saldo pendiente según el monto pagado.
        print("Realizando pago...")
        self.saldo_pendiente -= monto
        if self.saldo_pendiente > 0:
            print(f"Aún faltan ${self.saldo_pendiente} por pagar.")
        elif self.saldo_pendiente == 0:
            print("Saldo completamente pagado.")
        elif self.saldo_pendiente < 0:
            vuelto = self.saldo_pendiente * -1
            print(f"Saldo completamente pagado, y se han devuelto ${vuelto} sobrantes")
        return self

    def cambiar_suscripcion(self, nuevo_tipo):
        #Cambia el tipo de suscripción y actualiza el costo mensual.
        if nuevo_tipo == "Gratis" or nuevo_tipo == "Estándar" or nuevo_tipo == "Premium":
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = SuscripcionStreaming.costos_suscripcion[nuevo_tipo]
            self.saldo_pendiente += self.costo_mensual
            print(f"Nueva suscripción: {nuevo_tipo}")
            print(f"Monto a pagar: {self.saldo_pendiente}")
            return self
        else:
            print("Nueva suscripción inválida.")
            return self

    def ver_contenido_exclusivo(self):
        #Permite ver contenido exclusivo según el tipo de suscripción.
        if self.tipo_suscripcion == "Gratis":
            print("Contenido exclusivo bloqueado, debes ser rango Estándar o mayor.")
        elif self.tipo_suscripcion == "Estándar" or self.tipo_suscripcion == "Premium":
            print("Viendo contenido exclusivo.")
        return self

    def mostrar_info_suscripcion(self):
        #Muestra la información de la suscripción del usuario.
        print(f"Tipo de suscripción de {self.usuario}: {self.tipo_suscripcion}")
        print(f"Costo mensual: ${self.costo_mensual}")
        return self
        
#Crea 3 usuarios con diferentes tipos de suscripción.
user1 = SuscripcionStreaming("Matías", 0)
user2 = SuscripcionStreaming("Arael", 5.99, "Estándar")
user3 = SuscripcionStreaming("MatildeX", 10.99, "Premium")

'''Haz que el primer usuario intente ver contenido
exclusivo mejore su suscripción y pague su saldo.'''
print("== Actividad usuario 1 ==")
user1.ver_contenido_exclusivo().cambiar_suscripcion("Estándar").realizar_pago(5.99).ver_contenido_exclusivo()

'''Haz que el segundo usuario vea contenido exclusivo,
cambie su suscripción a Premium y pague dos veces.'''
print("\n== Actividad usuario 2 ==")
user2.ver_contenido_exclusivo().cambiar_suscripcion("Premium").realizar_pago(5.99).realizar_pago(10.99)

'''Haz que el tercer usuario intente pagar una cantidad
menor a su saldo pendiente y vea contenido exclusivo.'''
print("\n== Actividad usuario 3 ==")
user3.realizar_pago(2.43).ver_contenido_exclusivo()
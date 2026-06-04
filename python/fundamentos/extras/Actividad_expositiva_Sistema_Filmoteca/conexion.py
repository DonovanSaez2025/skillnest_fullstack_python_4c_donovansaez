# Importamos el conector MySQL
import mysql.connector


class Conexion:

    @staticmethod
    def conectar():

        """
        Este método crea y retorna una conexión
        a la base de datos.
        """

        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="colegio"
        )

        return conexion
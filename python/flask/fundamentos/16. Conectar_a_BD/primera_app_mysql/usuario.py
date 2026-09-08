from mysqlconnection import connectToMySQL

# Clase Usuario
class Usuario:
    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y transforma sus datos en atributos del objeto.
        """
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Obtener todos los usuarios
    @classmethod
    def get_all(cls):
        """
        Consulta todos los usuarios almacenados
        en la base de datos.
        Retorna una lista de objetos Usuario.
        """
        # Consulta SQL
        query = """
            SELECT * FROM usuarios;
        """
        # Ejecutar consulta
        resultados = connectToMySQL("primera_flask").query_db(query)

        # Crear lista de objetos
        usuarios = []

        # Convertir cada diccionario en Usuario
        for usuario in resultados:
            usuarios.append(cls(usuario))

        # Retornar resultado
        return usuarios
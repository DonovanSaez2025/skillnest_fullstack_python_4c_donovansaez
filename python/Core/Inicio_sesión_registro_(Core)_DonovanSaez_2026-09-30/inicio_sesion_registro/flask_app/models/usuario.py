# Importaciones
import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

# Filtro de caracteres en los email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password_hash = data["password_hash"]
        self.animal_favorito = data["animal_favorito"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validar_usuario(datos):
        es_valido = True
        
        if not datos["nombre"].strip():
            flash("El nombre es obligatorio.", "nombre")
            es_valido = False
        elif len(datos["nombre"].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "nombre")
            es_valido = False
            
        if not datos["apellido"].strip():
            flash("El apellido es obligatorio.", "apellido")
            es_valido = False
        elif len(datos["apellido"].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "apellido")
            es_valido = False
            
        if not datos["email"].strip():
            flash("El email es obligatorio.", "email")
            es_valido = False
        elif not EMAIL_REGEX.match(datos["email"].strip()):
            flash("El email no tiene un formato válido.", "email")
            es_valido = False
            
        # Validación de contraseña base
        if not datos["password_hash"]:
            flash("La contraseña es obligatoria.", "password_hash")
            es_valido = False
        elif len(datos["password_hash"]) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "password_hash")
            es_valido = False
            
        # NUEVA VALIDACIÓN: Confirmación de contraseña
        if datos["password_hash"] != datos["conf_password"]:
            flash("Las contraseñas no coinciden.", "password_hash")
            es_valido = False
            
        if not datos["animal_favorito"]:
            flash("Debes elegir un animal favorito.", "animal_favorito")
            es_valido = False
        elif len(datos["animal_favorito"]) < 2:
            flash("El animal debe tener al menos 2 caracteres.", "animal_favorito")
            es_valido = False
            
        # CORRECCIÓN DE BUG: Ahora sí bloquea si no ingresan la edad
        if not datos["edad"]:
            flash("Debes ingresar tu edad.", "edad")
            es_valido = False
            
        return es_valido

    @classmethod
    def guardar(cls, datos):
        query = """
            INSERT INTO usuarios(nombre, apellido, email, password_hash, animal_favorito, edad)
            VALUES(%(nombre)s, %(apellido)s, %(email)s, %(password_hash)s, %(animal_favorito)s, %(edad)s);
        """
        return connectToMySQL("inicio_sesion_registro").query_db(query, datos)
    
    @classmethod
    def existe_email(cls, datos):
        query = """
            SELECT id FROM usuarios WHERE email = %(email)s;
        """
        resultados = connectToMySQL("inicio_sesion_registro").query_db(query, datos)
        return len(resultados) > 0
    
    @classmethod
    def buscar_por_email(cls, datos):
        query = """
            SELECT * FROM usuarios WHERE email = %(email)s;
        """
        resultados = connectToMySQL("inicio_sesion_registro").query_db(query, datos)
        # CORRECCIÓN: Agregamos [0] para pasar el diccionario del usuario individual, no la lista entera
        if resultados and len(resultados) == 1:
            return cls(resultados[0]) 
        return False
        
    @classmethod
    def buscar_por_id(cls, datos):
        query = """
            SELECT * FROM usuarios WHERE id = %(id)s;
        """    
        resultados = connectToMySQL("inicio_sesion_registro").query_db(query, datos)
        # CORRECCIÓN: Agregamos [0] para pasar el diccionario del usuario individual, no la lista entera
        if resultados and len(resultados) == 1:
            return cls(resultados[0]) 
        return False
    
    @classmethod
    def passwords(cls, datos):
        if datos["password_1"] != datos["password_2"]:
            return cls
        return False

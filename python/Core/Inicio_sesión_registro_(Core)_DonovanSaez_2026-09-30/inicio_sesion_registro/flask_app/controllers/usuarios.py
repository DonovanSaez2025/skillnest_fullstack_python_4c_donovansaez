# Importaciones
from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario

# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para registar un usuario
@app.route("/registrar", methods=["POST"])
def registrar():
    datos = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip().lower(),
        "password_hash": request.form["password_hash"].strip(),
        "conf_password": request.form["conf_password"].strip(),
        "animal_favorito": request.form["animal_favorito"].strip(),
        "edad": request.form["edad"]}
    
    # Ejecutar el método validar_usuario de la clase Usuario
    if not Usuario.validar_usuario(datos):
        return redirect("/")
    
    # Verificar que el email no esté en uso
    if Usuario.existe_email({"email": datos["email"]}):
        flash("El email ya está registrado.", "email")
        return redirect("/")

    # Cifrar la contraseña después de las validaciones anteriores
    password_hash = bcrypt.generate_password_hash(datos["password_hash"]).decode("utf-8")
    datos["password_hash"] = password_hash
    
    usuario_id = Usuario.guardar(datos)
    if not usuario_id:
        flash("No fue posible registrar el usuario.", "general")
        return redirect("/")

    session["usuario_id"] = usuario_id
    return redirect("/usuario")

# Ruta para iniciar sesión
@app.route("/login", methods=["POST"])
def login():
    # Datos necesarios para el inicio de sesión
    datos = {
        "email": request.form["email"].strip().lower(),
        "password_hash": request.form["password_hash"]}

    # Verificar que el email exista
    usuario = Usuario.buscar_por_email({"email": datos["email"]})
    if not usuario:
        flash("Email o contraseña incorrectos.", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(usuario.password_hash, datos["password_hash"]):
        flash("Email o contraseña incorrectos.", "login")
        return redirect("/")
    
    # Redireccionar a la ruta de usuario luego de las validaciones
    session["usuario_id"] = usuario.id
    return redirect("/usuario")

# Ruta de usuario
@app.route("/usuario")
def usuario_mostrar():
    # Al llegar a la ruta de usuario sin tener una sesión iniciada
    if "usuario_id" not in session:
        flash("Debes iniciar sesión.", "login")
        return redirect("/")
    
    # Buscar el id del usuario
    usuario = Usuario.buscar_por_id({"id": session["usuario_id"]})
    return render_template("usuario.html", usuario=usuario)

# Ruta para cerrar sesión
@app.route("/logout")
def logout():
    # Limpiar la sesión
    session.clear()
    return redirect("/")
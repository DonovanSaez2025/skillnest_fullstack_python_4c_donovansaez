from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    datos = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip().lower(),
        "password_hash": request.form["password_hash"].strip(),
        "conf_password": request.form["conf_password"].strip(),
        "animal_favorito": request.form["animal_favorito"].strip(),
        "edad": request.form["edad"]
    }
    
    # 1. Ejecuta todas las validaciones (Maneja vacíos, largos y coincidencia de claves)
    if not Usuario.validar_usuario(datos):
        return redirect("/")
    
    # 2. Verifica que el correo no esté tomado
    if Usuario.existe_email({"email": datos["email"]}):
        flash("El email ya está registrado.", "email")
        return redirect("/")

    # 3. Cifra la contraseña únicamente tras pasar las validaciones con éxito
    password_hash = bcrypt.generate_password_hash(datos["password_hash"]).decode("utf-8")
    datos["password_hash"] = password_hash
    
    usuario_id = Usuario.guardar(datos)
    if not usuario_id:
        flash("No fue posible registrar el usuario.", "general")
        return redirect("/")

    session["usuario_id"] = usuario_id
    return redirect("/usuario")


@app.route("/login", methods=["POST"])
def login():
    datos = {
        "email": request.form["email"].strip().lower(),
        "password_hash": request.form["password_hash"]}

    usuario = Usuario.buscar_por_email({"email": datos["email"]})
    if not usuario:
        flash("Email o contraseña incorrectos.", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(usuario.password_hash, datos["password_hash"]):
        flash("Email o contraseña incorrectos.", "login")
        return redirect("/")
    
    session["usuario_id"] = usuario.id
    return redirect("/usuario")

@app.route("/usuario")
def usuario_mostrar():
    if "usuario_id" not in session:
        flash("Debes iniciar sesión.", "login")
        return redirect("/")
    
    usuario = Usuario.buscar_por_id({"id": session["usuario_id"]})
    return render_template("usuario.html", usuario=usuario)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
# Importaciones
from flask_app import app
from flask import render_template, request, redirect, url_for
from flask_app.models.usuario import Usuario

# Ruta principal
@app.route("/usuarios")
def usuarios():
    lista_usuarios = Usuario.get_all()
    return render_template("index.html", usuarios=lista_usuarios)

# Ruta para crear un usuario
@app.route("/usuarios/nuevo")
def nuevo():
    return render_template("nuevo.html")

# Ruta para guardar los valores del usuario creado
@app.route("/usuarios/crear", methods=["POST"])
def crear():
    data = {
        "nombre_usuario": request.form["nombre_usuario"].strip(),
        "apellido_usuario": request.form["apellido_usuario"].strip(),
        "email_usuario": request.form["email_usuario"].strip()}
    if not data["nombre_usuario"] or not data["apellido_usuario"] or not data["email_usuario"]:
        return render_template( "nuevo.html", error="Todos los campos son obligatorios.", datos=data)
    
    resultado = Usuario.save(data)
    if resultado is False:
        return render_template("nuevo.html",  error="No se pudo crear el usuario.", datos=data)
    
    return redirect(url_for("usuarios"))

# Ruta para ver un usuario según el ID
@app.route("/usuarios/<int:id>")
def detalle(id):
    usuario = Usuario.get_by_id(id)
    if usuario is None:
        return "Usuario no encontrado", 404

    return render_template("detalle.html", usuario=usuario)

# Ruta para editar un usuario
@app.route("/usuarios/editar/<int:id>")
def editar(id):
    usuario = Usuario.get_by_id(id)
    if usuario is None:
        return "Usuario no encontrado", 404
    
    return render_template("editar.html", usuario=usuario)

# Ruta para guardar los datos de un usuario editado
@app.route("/usuarios/<int:id>/actualizar", methods=["POST"])
def actualizar(id):
    data = {
        "id": id,
        "nombre_usuario": request.form["nombre_usuario"].strip(),
        "apellido_usuario": request.form["apellido_usuario"].strip(),
        "email_usuario": request.form["email_usuario"].strip()}

    if not data["nombre_usuario"] or not data["apellido_usuario"] or not data["email_usuario"]:
        usuario = Usuario.get_by_id(id)
        return render_template("editar.html", usuario=usuario, error="Todos los campos son obligatorios.")
        
    resultado = Usuario.update(data)
    if resultado is False:
        usuario = Usuario.get_by_id(id)
        return render_template("editar.html", usuario=usuario, error="No se pudo actualizar el usuario.")
    
    return redirect(url_for("usuarios"))

# Ruta para borrar un usuario
@app.route("/usuarios/borrar/<int:id>")
def borrar(id):
    data = {"id": id}
    resultado = Usuario.delete(data)
    if resultado is False:
        return "No se pudo borrar el usuario.", 500
    
    return redirect(url_for("usuarios"))
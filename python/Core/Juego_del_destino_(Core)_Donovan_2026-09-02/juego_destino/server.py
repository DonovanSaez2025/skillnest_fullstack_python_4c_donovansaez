from flask import Flask, render_template, request, session, redirect, url_for
import random
app = Flask(__name__)

# Lista respuestas
respuestas = [
    # Respuestas
    ["", "", "", "", "", "", "", "", "", ""]
    # Respuestas al color
    ["", "", "", "", "", "", "", "", "", ""]
    # Respuestas al animal
    ["", "", "", "", "", "", "", "", "", ""]
    ]
respuestasEdad = [
    # 1-10 años
    ["", "", "", "", "", "", "", "", "", ""]
    # 11-17 años
    ["", "", "", "", "", "", "", "", "", ""]
    # 18-25
    ["", "", "", "", "", "", "", "", "", ""]
    # 26+
    ["", "", "", "", "", "", "", "", "", ""]
]

# Clave para manejar sesiones en Flask
app.secret_key = "clave_secreta"

# Ruta principal que muestra el formulario para ingresar datos
@app.route("/")
def main():
    return render_template("index.html")

# Ruta para procesar los datos del formulario y almacenarlos en sesión
@app.route("/enviar", methods=["POST"])
def procesar():
    session["nombre"] = request.form["nombre"].strip()
    session["edad"] = request.form["edad"]
    session["color"] = request.form["color"]
    session["animal"] = request.form["animal"]
    return redirect(url_for("prediccion"))

# Ruta para mostrar la predicción del futuro basada en los datos ingresados
@app.route("/futuro", methods=["GET"])
def prediccion():
    nombre = session["nombre"]
    edad = session["edad"]
    color = session["color"]
    animal = session["animal"]
    return render_template("futuro.html", nombre=nombre, edad=edad, color=color, animal=animal)

# Debug
if __name__ == "__main__":
    app.run(debug=True)
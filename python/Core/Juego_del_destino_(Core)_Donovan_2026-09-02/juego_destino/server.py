from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)

# Clave para manejar sesiones en Flask
app.secret_key = "clave_secreta"

# Ruta principal que muestra el formulario para ingresar datos
@app.route("/")
def main():
    return render_template("index.html")

# Ruta para procesar los datos del formulario y almacenarlos en sesión
@app.route("/enviar", methods=["POST"])
def procesar():
    session["nombre"] = ""
    return redirect(url_for("prediccion"))

# Ruta para mostrar la predicción del futuro basada en los datos ingresados
@app.route("/futuro", methods=["GET"])
def prediccion():
    return render_template("futuro.html")

# Debug
if __name__ == "__main__":
    app.run(debug=True)
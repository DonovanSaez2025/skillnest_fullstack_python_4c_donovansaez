from flask import Flask, render_template, request, session, redirect, url_for
import random
app = Flask(__name__)

# Lista respuestas
respuestas = [
    # Respuestas
    {"respuestas": ["Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
                    "Grandes momentos de alegría se acercan a tu vida. Tu mente hallará paz en estas semanas.",
                    "Enfrentarás el mayor desafío del año uno de estos días. Preparate para sufrir una pérdida.",
                    "La buena suerte va a estar de tu lado por este mes. Aún así no te confíes en las apuestas.",
                    "Cuida tus objetos mañana, una visita inesperada traerá miedo a tu vida. Prepara una defensa crítica.",
                    "Recibirás una visita agradable hoy mismo. Será mejor que tengas lista una buena ofrenda de paz.",
                    "Un evento misterioso sucederá este año que te dejará con la duda creciente. Cuida tu curiosidad"],
        "colores": ["#ff00bf", "#0000FF", "#FF0000", "#00ff00", "#ffe600", "#ffbb00", "#9c4df7"]},
    # Respuestas al color
    ["el misterio y descubrimiento", "la amabilidad y cariño", "la ansiedad y miedo",
    "la investigación y atracción", "la física y lógica", "la buena vibra y positividad",
    "la naturaleza y vida"],
    # Respuestas al animal
    ["feróz y sigilosa", "tranquila y desapercibida", "tonta e ilógica",
    "social y colectiva", "calculadora y capáz", "inteligente y sabia", "aportadora y eficiente"]]
respuestasEdad = [
    # 1-12 años
    ["explorar la creatividad", "hacer nuevos amigos", "leer más libros", "dibujar para entrenar la mente"],
    # 13-17 años
    ["conocer el mundo exterior", "manejar mejor tus amistades", "empezar a ver tu futuro", "elegir una meta de vida"],
    # 18-25
    ["obtener un buen empleo", "pensar a largo plazo", "estudiar para seguir tus metas", "un momento favorable para aprovechar nuevas oportunidades"]]

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
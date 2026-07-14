from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/variable")
def varible():
    return render_template("variable.html", nombre="Donovan", curso="4C", ciudad="Santiago", anio="2026", profesor=False, tecnologias=["Python", "Flask", "HTML", "CSS"])

@app.route("/jugador")
def jugador():
    return render_template("jugador.html", jugador="TheDono", puntaje="6769", lider=False)

if __name__ == "__main__":

    app.run(debug=True)
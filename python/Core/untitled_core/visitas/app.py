from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = "llave"

# Ruta principal
@app.route("/")
def mainRoot():
    if "contador" not in session:
        session["contador"] = 0
    session["contador"] += 1
    return render_template("index.html", counter=session["contador"])

# Suma dos al conteo
@app.route('/sumar-dos', methods=["POST"])
def sumar_dos():
    if "contador" not in session:
        session["contador"] = 0
    session["contador"] += 1 
    return redirect(url_for("mainRoot"))

# Reinicia el conteo
@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    session.pop("contador", None)
    return redirect(url_for("mainRoot"))

# Debug
if __name__ == "__main__":
    app.run(debug=True)
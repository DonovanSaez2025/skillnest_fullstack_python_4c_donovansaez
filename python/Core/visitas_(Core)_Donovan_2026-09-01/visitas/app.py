from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = "llave"

# Ruta principal
@app.route("/")
def mainRoot():
    if "contador" not in session:
        session["contador"] = 0
        
    if "contadorRes" not in session:
            session["contadorRes"] = 0
            
    session["contador"] += 1
    return render_template("index.html", counter=session["contador"], counterRes=session["contadorRes"])

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
    if "contadorRes" not in session:
                session["contadorRes"] = 0
    session["contadorRes"] += 1
    
    session.pop("contador", None)
    return redirect(url_for("mainRoot"))

# Suma personalizada
@app.route('/sumar-custom', methods=['POST'])
def sumar_personalizado():
    if "cantidad" not in session:
        session["cantidad"] = 0
    cantidad = request.form.get("cantidad", 0)
    
    if cantidad:
        session["contador"] += int(cantidad)-1
    return redirect(url_for("mainRoot"))

# Debug
if __name__ == "__main__":
    app.run(debug=True)
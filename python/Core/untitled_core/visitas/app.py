from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "llave"

@app.route("/")
def mainRoot():
    if "contador" not in session:
        session["contador"] = 0
        
    session["contador"] += 1
    
    return render_template("index.html", counter=session["contador"])

if __name__ == "__main__":
    app.run(debug=True)
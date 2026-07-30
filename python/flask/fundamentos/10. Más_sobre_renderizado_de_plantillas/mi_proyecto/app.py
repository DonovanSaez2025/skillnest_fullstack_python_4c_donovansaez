from flask import Flask, render_template

app = Flask(__name__)

@app.route("/listas")
def renderizar_listas():
    # Lista de números
    numeros = [7, 15, 22]

    # Lista de diccionarios
    listado_estudiantes = [{"nombre":"Florencia", "edad":25},
                            {"nombre":"Valentina", "edad":30},
                            {"nombre":"José","edad":27},
                            {"nombre":"Patricio", "edad":21}]
    
    return render_template("listas.html", numeros=numeros, estudiantes=listado_estudiantes)
    
@app.route("/videojuegos")
def videojuegos():
    # Lista de videojuegos
    listado_videojuegos = [{"titulo": "Shadow of the Colossus", "plataforma": "Play Station 2", "anio": 2005},
                            {"titulo": "Cuphead", "plataforma": "PC", "anio": 2017},
                            {"titulo": "Super Mario Bros", "plataforma": "NES", "anio": 1985},
                            {"titulo": "Angry Birds", "plataforma": "Celular", "anio": 2009},
                            {"titulo": "Roblox", "plataforma": "PC", "anio": 2006},
                            {"titulo": "Crash Bandicoot", "plataforma": "Play Station 1", "anio": 1994}]
    return render_template("videojuegos.html", videojuegos=listado_videojuegos)
    
if __name__ == "__main__":
    app.run(debug=True)
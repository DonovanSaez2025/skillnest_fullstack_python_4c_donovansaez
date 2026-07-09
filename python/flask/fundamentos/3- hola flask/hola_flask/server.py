from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "My Little Duckaroo" #Insertar ruta HTML

@app.route("/nosotros")
def nosotros():
    return "Conócenos un poco más!"

@app.route("/peliculas")
def peliculas():
    return "Conoce todas nuestras películas y su modo de obtención: "

@app.route("/creditos")
def creditos():
    return "Creado por Donovan Sáez\nAgradecimientos al Profe Dany por enseñarnos."

if __name__ == "__main__":
    app.run(debug=True)
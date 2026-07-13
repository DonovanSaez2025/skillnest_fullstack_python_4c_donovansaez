from flask import Flask
app = Flask(__name__)

# Ruta raíz - Página de inicio
@app.route("/")
def inicio():
    return "<h1>Inicio</h1><p>Bienvenido a la página de inicio</p>"

# Ruta genérica para explorar enrutamiento
@app.route("/explorar")
def explorar():
    return "<h1>Explorar</h1><p>¿Vas a explorar algunos temas?</p>"

@app.route("/lista_peliculas")
def lista_peliculas():
    return "<h1>Lista de películas</h1><p>A continuación se mostrará una lista de películas disponibles</p><br><span>cargando...<span>"
# Rutas dinámicas para personalización
@app.route("/perfil/@<username>")
def perfil(username):
    return f"<h1>{username}</h1><p>Bienvenido a tu perfil {username}."

@app.route("/pelicula/<titulo>")
def pelicula(titulo):
    return f"<h1>{titulo}</h1><p>{titulo} es una película."

# Ruta que repite un mensaje varias veces
@app.route("/repetir/<mensaje>/<int:veces>")
def repetir(mensaje, veces):
    return f"{f"{mensaje} " * veces}"

# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente
@app.errorhandler(404)
def error(código=404):
    return f"Error: página no encontrada. Código: {código}"

# Ejecuta el servidor
if __name__ == "__main__":
    app.run(debug=True)
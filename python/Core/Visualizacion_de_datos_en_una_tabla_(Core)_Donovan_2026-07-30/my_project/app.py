from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de plataformas digitales
datos = [
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia", "imagen": "spotify.png"},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU.", "imagen": "netflix.png"},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU.", "imagen": "youtube.png"},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU.", "imagen": "twitch.png"},
    {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China", "imagen": "tiktok.png"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU.", "imagen": "instagram.png"},
    {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU.", "imagen": "discord.png"}]

# Ruta para mostrar la tabla con datos
@app.route("/tabla")
def plataformas():
    return render_template("index.html", datos=datos)

if __name__ == "__main__":
    app.run(debug = True)
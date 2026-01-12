from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def registrar_visita(pagina):
    conn = sqlite3.connect("reciconciencia.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pagina TEXT
        )
    """)
    cursor.execute("INSERT INTO visitas (pagina) VALUES (?)", (pagina,))
    conn.commit()
    conn.close()


@app.route("/")
def inicio():
    registrar_visita("inicio")
    return render_template("index.html")

@app.route("/informacion")
def informacion():
    registrar_visita("informacion")
    return render_template("info.html")

@app.route("/tips")
def tips():
    registrar_visita("tips")
    return render_template("tips.html")

@app.route("/contenedores")
def contenedores():
    registrar_visita("contenedores")
    return render_template("contenedores.html")

@app.route("/dinamicas")
def dinamicas():
    registrar_visita("dinamicas")
    return render_template("dinamicas.html")

if __name__ == "__main__":
    app.run(debug=True)

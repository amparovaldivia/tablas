from asignacion import app
from asignacion.modelo.usuarios import usuarios
from flask import render_template

@app.route('/')
def mostrar_tabla():
    return render_template('tabla.html',usuarios=usuarios)


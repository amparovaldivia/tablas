from flask import Flask, render_template, request, redirect


from asignacion import app
from asignacion.controllers import controlador


if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, redirect, render_template, request, session, url_for
from autenticacion import GestorAutenticacion
from util import GestorSesion

autenticacion_bp = Blueprint(
    'autenticacion',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@autenticacion_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        return GestorAutenticacion.usuarioValido(username, password)

    else: # request.method == "GET"
        if GestorSesion.usuarioLogeado():
            return redirect(url_for('curriculums.home'))
        return render_template('login.html')

@autenticacion_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        return GestorAutenticacion.agregarUsuario(username, password, confirm_password, email)
        # return "Registrar post"
    else:
        if GestorSesion.usuarioLogeado():
            return redirect(url_for('curriculums.home'))
        return render_template('registrar.html')

@autenticacion_bp.route("/cerrar_sesion")
def cerrarSesion():
    if GestorSesion.usuarioLogeado():
        GestorAutenticacion.cerrarSesion()
    return redirect(url_for('principal.index'))
    
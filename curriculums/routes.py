from flask import Blueprint, redirect, render_template, request, session, url_for
from curriculums import GestorCurriculums
from util import GestorSesion
from markupsafe import escape

curriculums_bp = Blueprint(
    'curriculums',
    __name__,
    template_folder="templates",
    static_folder="static"
)

@curriculums_bp.route("/home")
def home():
    if not GestorSesion.usuarioLogeado():    
        return redirect(url_for('principal.index'))
    id_usuario = GestorSesion.getIdUsuario()
    curriculums = GestorCurriculums.consultarCVS(id_usuario)
    return render_template("home.html", cvs=curriculums)

@curriculums_bp.route("/crear", methods=['GET', 'POST'])
def crear():
    if not GestorSesion.usuarioLogeado():
        return redirect(url_for('principal.index'))
    if request.method == "POST":
        titulo = request.form['titulo']
        id_plantilla = int(request.form['pt'])
        return GestorCurriculums.crearCV(titulo, id_plantilla)
    return render_template('crearCV.html')

@curriculums_bp.route("/editar/<id_curriculum>", methods=['GET', 'POST'])
def editar(id_curriculum):
    if not GestorSesion.usuarioLogeado():
        return redirect(url_for('principal.index'))
    id = escape(id_curriculum)
    if request.method == 'GET':
        # Obtener la informacion de curriculum y pasarla al render para completar el html
        cv = GestorCurriculums.obtenerCV(id)
        return render_template('edicion.html', id=id)
    # editar/id methods == "post"
    datos = None
    estado = GestorCurriculums.actualizarCV(id, datos)
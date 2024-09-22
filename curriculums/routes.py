from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for
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
        # Obtener la información del currículum y pasarla al render para completar el HTML
        cv = GestorCurriculums.obtenerCV(id)
        return render_template('edicion.html', id=id, cv=cv)

    if request.method == 'POST':
            # Extraer datos JSON del cuerpo de la solicitud
        datos = request.get_json()
        # GUardar los cambios en la BD
        return GestorCurriculums.actualizarCV(id_curriculum, datos)

@curriculums_bp.route("/eliminar/<id_curriculum>", methods=['GET', 'POST'])
def eliminar(id_curriculum):
    if not GestorSesion.usuarioLogeado():
        return redirect(url_for('principal.index'))
    
    if request.method == 'POST':
        id = escape(id_curriculum)
        return GestorCurriculums.eliminarCV(id)
    return redirect(url_for('curriculums.home'))

@curriculums_bp.route("/previsualizar/<id_curriculum>")
def previsualizar(id_curriculum):
    if not GestorSesion.usuarioLogeado():
        return redirect(url_for('principal.index'))

    estado, respuesta = GestorCurriculums.exportar(id_curriculum, "pdf")
    if estado:
        return respuesta # Devuelve el archivo
    else:
        return render_template('notificacion.html', mensaje=respuesta)
    
    
    
@curriculums_bp.route("/exportar/<id_curriculum>", methods=['GET', 'POST'])
def exportar(id_curriculum):
    if not GestorSesion.usuarioLogeado():
        return redirect(url_for('principal.index'))
    
    if request.method == 'POST':
        formato = request.form['fmt']
        estado, respuesta = GestorCurriculums.exportar(id_curriculum, formato)
        if estado:
            return respuesta # Devuelve el archivo
        else:
            return render_template('notificacion.html', mensaje=respuesta)
            

    return render_template('exportar.html', id_cum=id_curriculum)
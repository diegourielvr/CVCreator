from flask import jsonify
from curriculums.Curriculum import Curriculum
from service import ConectorDBCurriculums
from util import GestorSesion

def consultarCVS(id_usuario):
    cvs = ConectorDBCurriculums.consultarCVS(id_usuario)
    if not cvs:
        return False
    curriculums = []
    for cv in cvs:
        curriculums.append(Curriculum(
            cv[0], cv[1], cv[2], cv[3], cv[4], cv[5]
        ))
    return curriculums

def crearCV(titulo, id_plantilla):
    if not titulo:
        return jsonify({
            'status': 'error',
            'message': '¡Debes ingresar un titulo! ⚠'
        })
    if not id_plantilla:
        return jsonify({
            'status': 'error',
            'message': '¡Debes seleccionar una plantilla! ⚠'
        })
    # TODO: Validar que el titulo no se repita
    id_usuario = GestorSesion.getIdUsuario() # Recupera id id_usuario
    if ConectorDBCurriculums.crearCV(id_usuario, id_plantilla, titulo):
        return jsonify({
            'status': 'success',
            'message': '¡Curriculum creado correctamente! ✅'
        })
    
def obtenerCV(id_curriculum):
    cv = ConectorDBCurriculums.obtenerCV(id_curriculum)
    # TODO
    return

def actualizarCV(id_curriculum, file):
    # TODO: El GEstor debe convertir los datos a JSON
    
    estado = ConectorDBCurriculums.actualizarCV(id_curriculum, file)
    return

def eliminarCV(id_curriculum):
    estado = ConectorDBCurriculums.eliminarCV(id_curriculum)
    # TODO: Aqui hacer las validacinoes necesarias
    return
    
         
from io import BytesIO
import json
from flask import jsonify, render_template, send_file
from curriculums.Curriculum import Curriculum
from curriculums import Exportacion
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
    id_usuario = GestorSesion.getIdUsuario() # Recupera id_usuario

    if ConectorDBCurriculums.existeTitulo(titulo, id_usuario):
        return jsonify({
            'status': 'error',
            'message': f'Ya existe un archivo con el mismo titulo ({titulo}) ⚠'
        })
    
    if ConectorDBCurriculums.crearCV(id_usuario, id_plantilla, titulo):
        return jsonify({
            'status': 'success',
            'message': '¡Curriculum creado correctamente! ✅',
        })
    
def obtenerCV(id_curriculum):

    id_usuario = GestorSesion.getIdUsuario()
    if not ConectorDBCurriculums.existeCurriculum(id_curriculum, id_usuario):
        estado = False
        mensaje = "No existe el curriculum ❌"
        return estado, mensaje 

    cv = ConectorDBCurriculums.obtenerDatosJson(id_curriculum)
    estado = True
    return estado, cv

def actualizarCV(id_curriculum, datos):
    # Convertir los datos a una cadena JSON
    json_data = json.dumps(datos)

    # Llamar al método de actualización en ConectorDBCurriculums
    estado = ConectorDBCurriculums.actualizarCV(id_curriculum, json_data)
    if estado:
        return jsonify({
            'status': 'success',
            'message': '¡Curriculum actualizado correctamente! ✅'
        })
    else:
        return jsonify({
                'status': 'error',
                'message': 'No haz realizado cambios. ⚠'
                # 'message': 'Error al actualizar el currículum. ⚠'
        })

def eliminarCV(id_curriculum):
    # Validar si existe el cv antes de eliminar y si le pertenece al usuario actual
    id_usuario = GestorSesion.getIdUsuario()
    if ConectorDBCurriculums.existeCurriculum(id_curriculum, id_usuario):
        estado = ConectorDBCurriculums.eliminarCV(id_curriculum)
        if estado:
            return jsonify({
                'status': 'success',
                'message': '¡Curriculum eliminado correctamente! ✅'
            })
        else:
            return jsonify({
                    'status': 'error',
                    'message': 'Error al eliminar el currículum. ⚠'
            })
    return jsonify({
            'status': 'error',
            'message': 'No existe el curriculum ❌'
    })

def previsualilzar(id_curriculum):
    id_usuario = GestorSesion.getIdUsuario()
    if not ConectorDBCurriculums.existeCurriculum(id_curriculum, id_usuario):
        estado = False
        mensaje = "No existe el curriculum ❌"
        return estado, mensaje 
        
    # obtener ifnormación de la BD
    cv = ConectorDBCurriculums.obtenerCV(id_curriculum)
    
    id_plantilla = str(cv[1])
    nombre_cv = cv[2]
    datos = {} # Siempre pasar un diccionario (aunque este vacio)
    if cv[5]:
        datos = json.loads(cv[5])
    else:
        datos = getJsonEjemplo()

    estado = True
    return estado, Exportacion.exportar("preview", id_plantilla, nombre_cv, datos)

def exportar(id_curriculum, formato):
    id_usuario = GestorSesion.getIdUsuario()
    if not ConectorDBCurriculums.existeCurriculum(id_curriculum, id_usuario):
        estado = False
        mensaje = "No existe el curriculum ❌"
        return estado, mensaje 
        
    # obtener ifnormación de la BD
    cv = ConectorDBCurriculums.obtenerCV(id_curriculum)
    
    id_plantilla = str(cv[1])
    nombre_cv = cv[2]
    datos = {} # Siempre pasar un diccionario (aunque este vacio)
    if cv[5]:
        datos = json.loads(cv[5])
    else:
        datos = getJsonEjemplo()

    estado = True
    return estado, Exportacion.exportar(formato, id_plantilla, nombre_cv, datos)
    
def getJsonEjemplo():
    return {
        "datos_personales": {
            "nombre": "Diego uriel",
            "apellidos": "Vazquez Ramirez",
            "fecha_nacimiento": "02/09/00",
            "telefono": "0011226644",
            "ocupacion": "Estudiante",
            "email": "diego@gmail.com"
        },
        "links": [
            {
                "nombre": "Github",
                "link": "https://github.com/diegourielvr"
            },
            {
                "nombre": "LinkedIn",
                "link": "https://mx.linkedin.com/in/diego_uriel"
            }
        ],
        "lenguajes": [
            {
                "idioma": "Español",
                "nivel": "Nativo"    
            },
            {
                "idioma": "Ingles",
                "nivel": "B2"   
            }
        ],
        "habilidades": [
            {
                "nombre": "Base de datos",
                "resumen": "mysql"
            },
            {
                "nombre": "Lenguajes de programación",
                "resumen": "hola"
            },
        ],
        "experiencia_laboral": [
            {
                "compania": "Uam Cuajimalpa",
                "puesto": "Estudiante",
                "fecha_inicio": "04/12/19",
                "fecha_fin": "20/08/25",
                "resumen": "Mucho aprendizaje"
            },
            {
                "compania": "Taqueria carlitos",
                "puesto": "Mesero",
                "fecha_inicio": "04/12/19",
                "fecha_fin": "20/08/25",
                "resumen": "Mucho aprendizaje"
            },
        ],
        "educacion": [
            {
                "institucion": "Cetis 50",
                "grado": "Ingenieria en computacion",
                "fecha_inicio": "04/12/15",
                "fecha_fin": "20/08/18",
                "resumen": "Programacion web y manejo de base de datos"
            },
            {
                "institucion": "Prepa 7",
                "grado": "Ingenieria en mecatronica",
                "fecha_inicio": "04/12/15",
                "fecha_fin": "20/08/18",
                "resumen": "Programacion web y manejo de base de datos"
            },
        ]
    }
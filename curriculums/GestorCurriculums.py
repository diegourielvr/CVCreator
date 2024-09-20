from io import BytesIO
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

def exportar(id_curriculum, formato):
    # Validar que existe el id_curriculum
    # Validar que el id_curriculum pertenexca al usuario con sesion actual
    # Exportar unicamente despues de haber guardado los cambios
    # obtener ifnormación de la BD

    datos = {
        "datos_personales": {
            "nombre": "Diego Uriel",
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
                "subhabilidades": [
                    "Mysql",
                    "Postgresql",
                    "MongoDB"
                ]
            },
            {
                "nombre": "Lenguajes de programación",
                "subhabilidades": [
                    "Python",
                    "C",
                    "Java"
                ]
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
    id_plantilla = str(3) # Obtener de la base de datos
    nombre_cv = "Mi primer CV"
    return Exportacion.exportar(formato, id_plantilla, nombre_cv, datos)
    
         
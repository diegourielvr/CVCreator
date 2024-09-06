from click import confirm
from flask import jsonify
from service import ConectorDBAutenticacion
from autenticacion.Usuario import Usuario
from util import GestorSesion

def usuarioValido(username, password):
    user = ConectorDBAutenticacion.usuarioValido(username, password)
    if user:
        usuario = Usuario(user[0], user[1], user[3])
        # Guardar la sesion del usuario
        GestorSesion.guardarSesion(usuario)
        return jsonify({
            'status': 'success',
            'message': '¡Inicio de sesión exitoso! ✅'
        })
    return jsonify({
        'status': 'error',
        'message': '¡El nombre de usuario o contraseña es incorrecto! ❌'
    })
    
def agregarUsuario(username, password, confirm_password, email):
    if password == confirm_password:
        if ConectorDBAutenticacion.existeUsername(username):
            return jsonify({
                'status': 'error',
                'message': '¡El nombre de usuario ya estaba registrado! ❌'
            })
        if ConectorDBAutenticacion.existeEmail(email):
            return jsonify({
                'status': 'error',
                'message': '¡El email ya estaba registrado! ❌'
            })
            
        registrado = ConectorDBAutenticacion.agregarUsuario(username, password, email)
        if registrado:
            return jsonify({
                'status': 'success',
                'message': '¡Te has registrado correctamente! ✅'
            })
    
    return jsonify({
        'status': 'error',
        'message': '¡Las contraseñas no coinciden! ❌'
    })

def cerrarSesion():
    if GestorSesion.eliminarSesion():
        return True
    return False
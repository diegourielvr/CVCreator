from flask import session
from autenticacion.Usuario import Usuario

def guardarSesion(usuario: Usuario):
    session['id_usuario'] = usuario.getIdUsuario()
    session['username'] = usuario.getUsername()
    session['email'] = usuario.getEmail()
    session['conectado'] = True

def eliminarSesion():
    if 'conectado' in session:
        session.pop('id_usuario', None)
        session.pop('username', None)
        session.pop('email', None)
        session.pop('conectado', None)
        # session.clear()
        return True
    return False
    
def usuarioLogeado():
    return 'conectado' in session

def getIdUsuario():
    return session['id_usuario']
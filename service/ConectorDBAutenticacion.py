import mysql.connector

conexion = mysql.connector.connect(
    user="root",
    password="daik",
    host="localhost",
    database="cvcreator"
)
cursor = conexion.cursor()

# Devuelve toda la información de un usuario
def usuarioValido(username, password):
    sql = """
    SELECT id_usuario, username, password, email from usuarios
    WHERE username = %s
    """
    values = (username,)
    try:
        cursor.execute(sql, values)
        user = cursor.fetchone()
        # No existe el usuario o su conrtaseña es incorrecta
        if not user or password != user[2]:
            return False
        return user
    except mysql.connector.Error as err:
        return False

def agregarUsuario(username, password, email):
    sql = """
    INSERT INTO usuarios(username, password, email)
    VALUES (%s, %s, %s)
    """
    values = (username, password, email)
    try:
        cursor.execute(sql, values)
        conexion.commit()
        if cursor.rowcount: # filas afectadas
            return True
        else:
            return False
    except mysql.connector.Error as err:
        return False
    
def existeUsername(username):
    sql = """
    SELECT * FROM usuarios
    WHERE username = %s 
    """
    values = (username,)
    try:
        cursor.execute(sql, values)
        resultado = cursor.fetchone()
        if resultado:
            return True
        return False
    except mysql.connector.Error as err:
        return False
    
def existeEmail(email):
    sql = """
    SELECT * FROM usuarios
    WHERE email = %s 
    """
    values = (email,)
    try:
        cursor.execute(sql, values)
        resultado = cursor.fetchone()  # fetchall devuelve una lista de tuplas
        if resultado:
            return True
        return False
    except mysql.connector.Error as err:
        return False
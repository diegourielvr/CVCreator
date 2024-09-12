import mysql.connector

conexion = mysql.connector.connect(
    user="root",
    password="daik",
    host="localhost",
    database="cvcreator"
)
cursor = conexion.cursor()

def consultarCVS(id_usuario):
    sql = """
    SELECT id_curriculum, id_usuario, id_plantilla, titulo, fecha_creacion, fecha_ultima_modificacion from curriculums
    WHERE id_usuario = %s
    """
    values = (id_usuario,)
    try:
        cursor.execute(sql, values)
        cvs = cursor.fetchall()
        if cvs:
            return cvs
        return False
    except mysql.connector.Error as err:
        return False

def crearCV(id_usuario, id_plantilla, titulo):
    sql = """
    INSERT INTO curriculums(id_usuario, id_plantilla, titulo)
    VALUES (%s, %s, %s)
    """
    values = (id_usuario, id_plantilla, titulo)
    try:
        cursor.execute(sql, values)
        conexion.commit()
        if cursor.rowcount: # filas afectadas
            return True
        else:
            return False
    except mysql.connector.Error as err:
        return False

def obtenerCV(id_curriculum):
    # TODO
    return

def actualizarCV(id_curriculum, file):
    #TODO
    return

def eliminarCV(id_curriculum):
    try:
        # Eliminar el CV de la tabla 'curriculums'
        sql = "DELETE FROM curriculums WHERE id_curriculum = %s"
        cursor.execute(sql, (id_curriculum,))
        conexion.commit()
        print(f"CV con id {id_curriculum} eliminado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al eliminar el CV: {err}")
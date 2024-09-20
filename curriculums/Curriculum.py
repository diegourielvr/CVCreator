class Curriculum:
    def __init__(self, id_curriculum, id_usuario, id_plantilla, titulo, fecha_creacion, fecha_modificacion):
        self.id_curriculum = id_curriculum
        self.id_usuario = id_usuario
        self.id_plantilla = id_plantilla
        self.titulo = titulo
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion
    
    def getIdCurriculum(self):
        return self.id_curriculum
    
    def getTitulo(self):
        return self.titulo
        
    def getFechaModificacion(self):
        return self.fecha_modificacion

    def getIdPlantilla(self):
        return str(self.id_plantilla)
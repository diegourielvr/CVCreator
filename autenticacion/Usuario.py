class Usuario:
    def __init__(self, id_usuario, username, email):
        self.id_usuario = id_usuario
        self.username= username
        self.email = email 

    def getIdUsuario(self):
        return self.id_usuario

    def getUsername(self):
        return self.username
        
    def getEmail(self):
        return self.email
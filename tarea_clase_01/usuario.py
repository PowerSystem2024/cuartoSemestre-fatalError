class Usuario:
    """Clase que representa un usuario de la base de datos"""
    
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario    # ID del usuario (PK en BD)
        self._username = username        # Nombre de usuario
        self._password = password        # Contraseña

    def __str__(self):
        """Representación en texto del objeto"""
        return f"Usuario: {self._id_usuario}, {self._username}, {self._password}"

    # Getter y Setter para id_usuario
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    # Getter y Setter para username
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    # Getter y Setter para password
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

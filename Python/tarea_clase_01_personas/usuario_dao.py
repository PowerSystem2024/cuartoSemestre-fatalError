from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import log

class UsuarioDao:
    """Data Access Object para la tabla usuario"""
    
    # Sentencias SQL
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        """Obtiene todos los usuarios de la base de datos"""
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)        # Ejecuta la consulta
            registros = cursor.fetchall()           # Obtiene todos los resultados
            usuarios = [Usuario(registro[0], registro[1], registro[2]) for registro in registros]  # Convierte a objetos Usuario
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        """Inserta un nuevo usuario"""
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)  # Valores para el INSERT
            cursor.execute(cls._INSERTAR, valores)          # Ejecuta el INSERT
            log.debug(f"Usuario insertado: {usuario}")
            return cursor.rowcount                          # Devuelve cantidad de filas afectadas

    @classmethod
    def actualizar(cls, usuario):
        """Actualiza un usuario existente"""
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Usuario actualizado: {usuario}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        """Elimina un usuario"""
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Usuario eliminado: {usuario}")
            return cursor.rowcount

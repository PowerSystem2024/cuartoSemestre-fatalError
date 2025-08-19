from conexion import Conexion     # Usamos la clase Conexion para obtener conexiones
from logger_base import log       # Logger para registrar eventos

class CursorDelPool:
    """Clase que administra la conexión y el cursor usando 'with'"""
    
    def __init__(self):
        self._conexion = None     # Guardará la conexión activa
        self._cursor = None       # Guardará el cursor activo

    def __enter__(self):
        """Se ejecuta al entrar al bloque 'with'"""
        self._conexion = Conexion.obtenerConexion()  # Obtenemos una conexión del pool
        self._cursor = self._conexion.cursor()       # Creamos un cursor para ejecutar SQL
        return self._cursor                          # Retornamos el cursor para usarlo

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_error):
        """Se ejecuta al salir del bloque 'with'"""
        if valor_excepcion:
            # Si hubo un error, hacemos rollback
            self._conexion.rollback()
            log.error(f"Error: {valor_excepcion} - rollback ejecutado")
        else:
            # Si todo va bien, confirmamos cambios (commit)
            self._conexion.commit()
            log.debug("Commit de la transacción")
        self._cursor.close()                         # Cerramos el cursor
        Conexion.liberarConexion(self._conexion)     # Liberamos la conexión al pool

import psycopg2                  # Librería para conectarse a PostgreSQL
from psycopg2 import pool        # Módulo para manejar pool de conexiones
import sys                       # Para salir del programa en caso de error
from logger_base import log      # Logger para registrar eventos

class Conexion:
    # Datos de configuración de la base de datos
    _DATABASE =         # Nombre de la base de datos
    _USERNAME =        # Usuario de PostgreSQL
    _PASSWORD =           # Contraseña del usuario
    _DB_PORT = '5432'            # Puerto de PostgreSQL
    _HOST = 'localhost'          # Dirección del servidor
    _MIN_CON = 1                  # Mínimo de conexiones en el pool
    _MAX_CON = 5                  # Máximo de conexiones en el pool
    _pool = None                  # Variable para almacenar el pool de conexiones

    @classmethod
    def obtenerPool(cls):
        """Crea y devuelve el pool de conexiones si no existe"""
        if cls._pool is None:
            try:
                # Crea el pool de conexiones
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f"Creación del pool exitosa: {cls._pool}")
                return cls._pool
            except Exception as e:
                # Si hay error, se muestra y se cierra el programa
                log.error(f"Error al crear el pool de conexiones: {e}")
                sys.exit()
        else:
            # Si el pool ya existe, lo devuelve
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        """Obtiene una conexión del pool"""
        conexion = cls.obtenerPool().getconn()
        log.debug(f"Conexión obtenida del pool: {conexion}")
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        """Devuelve una conexión al pool"""
        cls.obtenerPool().putconn(conexion)
        log.debug(f"Conexión devuelta al pool: {conexion}")

    @classmethod
    def cerrarConexiones(cls):
        """Cierra todas las conexiones del pool"""
        cls.obtenerPool().closeall()
        log.debug("Conexiones cerradas")

import logging as log

# Configuración básica del logger
log.basicConfig(
    level=log.DEBUG,                              # Nivel mínimo de mensajes
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt='%I:%M:%S %p'
)

import os

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

# Rutas
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "assets")
IMAGES_PATH = os.path.join(ASSETS_PATH, "images")
SOUNDS_PATH = os.path.join(ASSETS_PATH, "sounds")

# Configuración del jugador
PLAYER_SPEED = 5
LASER_SPEED = 10

# Configuración de enemigos
ENEMY_SPEED = 2
ENEMY_SPAWN_RATE = 60  # frames entre aparición de enemigos
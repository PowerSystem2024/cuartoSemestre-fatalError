import pygame
import sys
import os
import random
from constantes import *

# Inicialización de Pygame
pygame.init()

# Configuración de audio
try:
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)
    audio_available = True
except:
    print("Advertencia: No se pudo inicializar el sistema de audio")
    audio_available = False

# Configuración de volumen
VOLUMEN_MUSICA = 0.5
VOLUMEN_SONIDOS = 0.7

# Configuración de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Naves")
clock = pygame.time.Clock()

# Crear carpetas necesarias
os.makedirs(IMAGES_PATH, exist_ok=True)
os.makedirs(SOUNDS_PATH, exist_ok=True)

# Función para cargar sonidos
def load_sound(filename, volume=0.5):
    if not audio_available:
        return None
        
    try:
        sound_path = os.path.join(SOUNDS_PATH, filename)
        if not os.path.exists(sound_path):
            print(f"Archivo de sonido no encontrado: {sound_path}")
            return None
            
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(volume * VOLUMEN_SONIDOS)
        return sound
    except Exception as e:
        print(f"Error al cargar el sonido {filename}: {e}")
        return None

# Función para reproducir música
def play_music(filename, volume=0.5):
    if not audio_available:
        return
        
    try:
        music_path = os.path.join(SOUNDS_PATH, filename)
        if not os.path.exists(music_path):
            print(f"Archivo de música no encontrado: {music_path}")
            return
            
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(volume * VOLUMEN_MUSICA)
        pygame.mixer.music.play(-1)  # -1 para reproducir en bucle
    except Exception as e:
        print(f"Error al cargar la música {filename}: {e}")

# Cargar efectos de sonido
sounds = {}

# Intentar cargar los sonidos si están disponibles
if audio_available:
    sounds['laser'] = load_sound('Disparo.wav', 0.7)
    sounds['explosion'] = load_sound('LogTrue.wav', 0.7)  # Sonido de explosión
    # Reproducir música de fondo si está disponible
    play_music('Level2 OST.mp3', 0.5)

# Cargar y preparar imágenes
try:
    # Cargar la imagen de fondo
    try:
        background_img = pygame.image.load("assets/images/Whisk_cd0ee91237ba1d4970f40760b3d63a22dr.jpeg").convert()
        background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except Exception as e:
        print(f"No se pudo cargar la imagen de fondo: {e}")
        background_img = None
    
    # Cargar la imagen base
    base_img = pygame.image.load("assets/images/topSprite.png").convert_alpha()
    
    # Imagen del enemigo (apuntando hacia abajo)
    enemy_img = pygame.transform.scale(base_img, (40, 40))
    
    # Imagen del jugador (rotada 180 grados y de color azul)
    player_img = pygame.transform.rotate(base_img, 180)  # Rotar 180 grados
    player_img = pygame.transform.scale(player_img, (40, 40))
    
    # Cambiar el color de la nave del jugador a azul
    player_img = player_img.copy()
    w, h = player_img.get_size()
    for x in range(w):
        for y in range(h):
            r, g, b, a = player_img.get_at((x, y))
            if a > 0:  # Si el píxel no es transparente
                # Cambiar a tonos de azul
                player_img.set_at((x, y), (r//3, g//3, 255, a))
    
    # Crear imagen del láser
    laser_img = pygame.Surface((4, 15), pygame.SRCALPHA)
    pygame.draw.rect(laser_img, AMARILLO, (0, 0, 4, 15))
    
except Exception as e:
    print(f"Error al cargar imágenes: {e}")
    print("Usando figuras geométricas en su lugar...")
    
    # Crear superficies de respaldo
    player_img = pygame.Surface((50, 40), pygame.SRCALPHA)
    pygame.draw.polygon(player_img, AZUL, [(25,0), (0,40), (50,40)])  # Triángulo azul
    
    enemy_img = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.polygon(enemy_img, ROJO, [(20,0), (0,40), (40,40)])  # Triángulo rojo
    
    laser_img = pygame.Surface((4, 15), pygame.SRCALPHA)
    pygame.draw.rect(laser_img, AMARILLO, (0, 0, 4, 15))  # Rectángulo amarillo

# Inicializar jugador
player_img_rect = player_img.get_rect()
player = pygame.Rect(
    SCREEN_WIDTH // 2 - player_img_rect.width // 2,
    SCREEN_HEIGHT - 100,
    player_img_rect.width,
    player_img_rect.height
)

# Ajustar el tamaño de la hitbox del jugador (hacerla un poco más pequeña que la imagen)
player_hitbox = player.inflate(-10, -10)  # Reducir el tamaño de la hitbox
player_speed = PLAYER_SPEED

# Listas para guardar proyectiles y enemigos
lasers = []
enemies = []

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Disparar
                if sounds.get('laser'):
                    sounds['laser'].play()
                laser_rect = laser_img.get_rect()
                laser = {
                    'rect': pygame.Rect(
                        player.centerx - laser_rect.width // 2,
                        player.top - laser_rect.height,
                        laser_rect.width,
                        laser_rect.height
                    ),
                    'image': laser_img
                }
                lasers.append(laser)
    
    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
        player.x += player_speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < SCREEN_HEIGHT:
        player.y += player_speed
    
    # Generar enemigos
    if random.random() < 0.02:  # 2% de probabilidad por frame
        enemy = pygame.Rect(
            random.randint(0, SCREEN_WIDTH - 40),
            -40,
            40,
            40
        )
        enemies.append(enemy)
    
    # Actualizar posición de los láseres
    for laser in lasers[:]:
        laser['rect'].y -= 15
        if laser['rect'].bottom < 0:
            lasers.remove(laser)
    
    # Actualizar posición de los enemigos
    for enemy in enemies[:]:
        enemy.y += ENEMY_SPEED
        if enemy.top > SCREEN_HEIGHT:
            enemies.remove(enemy)
        
        # Detección de colisión con jugador (usando hitbox)
        if player_hitbox.colliderect(enemy):
            if sounds.get('game_over'):
                sounds['game_over'].play()
            running = False
        
        # Detección de colisión con láseres
        for laser in lasers[:]:
            if enemy.colliderect(laser['rect']):
                if laser in lasers:
                    lasers.remove(laser)
                if enemy in enemies:
                    enemies.remove(enemy)
                    if sounds['explosion']:
                        sounds['explosion'].play()
                score += 10
                break
    
    # Dibujar fondo
    if background_img:
        screen.blit(background_img, (0, 0))
    else:
        screen.fill(NEGRO)
    
    # Dibujar jugador
    screen.blit(player_img, player.topleft)
    
    # Dibujar hitbox (solo para depuración)
    # pygame.draw.rect(screen, VERDE, player_hitbox, 1)
    
    # Dibujar láseres
    for laser in lasers:
        screen.blit(laser['image'], laser['rect'])
    
    # Dibujar enemigos
    for enemy in enemies:
        screen.blit(enemy_img, enemy.topleft)
    
    # Mostrar puntuación
    score_text = font.render(f'Puntuación: {score}', True, BLANCO)
    screen.blit(score_text, (10, 10))
    
    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(FPS)

# Pantalla de Game Over
game_over = True
game_over_font = pygame.font.Font(None, 72)
small_font = pygame.font.Font(None, 36)

game_over_text = game_over_font.render('GAME OVER', True, ROJO)
final_score_text = font.render(f'Puntuación final: {score}', True, BLANCO)
restart_text = small_font.render('Presiona R para reiniciar o ESC para salir', True, BLANCO)

# Efecto de fade out
fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
fade.fill(NEGRO)
for alpha in range(0, 200, 5):
    fade.set_alpha(alpha)
    screen.blit(fade, (0, 0))
    pygame.display.flip()
    pygame.time.delay(30)

# Bucle de game over
waiting = True
while waiting and game_over:
    screen.fill(NEGRO)
    
    # Dibujar textos
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//2 - 100))
    screen.blit(final_score_text, (SCREEN_WIDTH//2 - final_score_text.get_width()//2, SCREEN_HEIGHT//2))
    screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, SCREEN_HEIGHT//2 + 100))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                waiting = False
            if event.key == pygame.K_r:
                # Reiniciar juego
                game_over = False
                waiting = False
                
                # Restablecer variables del juego
                player.x = SCREEN_WIDTH // 2 - player_img_rect.width // 2
                player.y = SCREEN_HEIGHT - 100
                lasers = []
                enemies = []
                score = 0
                
                # Volver a reproducir música de fondo
                play_music('background.wav')
                
                # Continuar con el juego
                running = True
                while running:
                    # Manejo de eventos
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                # Disparar
                                if sounds.get('laser'):
                                    sounds['laser'].play()
                                laser_rect = laser_img.get_rect()
                                laser = {
                                    'rect': pygame.Rect(
                                        player.centerx - laser_rect.width // 2,
                                        player.top - laser_rect.height,
                                        laser_rect.width,
                                        laser_rect.height
                                    ),
                                    'image': laser_img
                                }
                                lasers.append(laser)
                    
                    # Movimiento del jugador
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT] and player.left > 0:
                        player.x -= player_speed
                    if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
                        player.x += player_speed
                    if keys[pygame.K_UP] and player.top > 0:
                        player.y -= player_speed
                    if keys[pygame.K_DOWN] and player.bottom < SCREEN_HEIGHT:
                        player.y += player_speed
                    
                    # Generar enemigos
                    if random.random() < 0.02:  # 2% de probabilidad por frame
                        enemy = pygame.Rect(
                            random.randint(0, SCREEN_WIDTH - 40),
                            -40,
                            40,
                            40
                        )
                        enemies.append(enemy)
                    
                    # Actualizar posición de los láseres
                    for laser in lasers[:]:
                        laser['rect'].y -= 15
                        if laser['rect'].bottom < 0:
                            lasers.remove(laser)
                    
                    # Actualizar posición de los enemigos
                    for enemy in enemies[:]:
                        enemy.y += ENEMY_SPEED
                        if enemy.top > SCREEN_HEIGHT:
                            enemies.remove(enemy)
                        
                        # Detección de colisión con jugador (usando hitbox)
                        if player_hitbox.colliderect(enemy):
                            if sounds.get('game_over'):
                                sounds['game_over'].play()
                            running = False
                            game_over = True
                            waiting = True
                            break
                        
                        # Detección de colisión con láseres
                        for laser in lasers[:]:
                            if enemy.colliderect(laser['rect']):
                                if laser in lasers:
                                    lasers.remove(laser)
                                if enemy in enemies:
                                    enemies.remove(enemy)
                                    if sounds.get('explosion'):
                                        sounds['explosion'].play()
                                score += 10
                                break
                    
                    # Si el juego terminó, salir del bucle
                    if not running:
                        break
                    
                    # Dibujar fondo
                    if background_img:
                        screen.blit(background_img, (0, 0))
                    else:
                        screen.fill(NEGRO)
                    
                    # Dibujar jugador
                    screen.blit(player_img, player.topleft)
                    
                    # Dibujar láseres
                    for laser in lasers:
                        screen.blit(laser['image'], laser['rect'])
                    
                    # Dibujar enemigos
                    for enemy in enemies:
                        screen.blit(enemy_img, enemy.topleft)
                    
                    # Mostrar puntuación
                    score_text = font.render(f'Puntuación: {score}', True, BLANCO)
                    screen.blit(score_text, (10, 10))
                    
                    # Actualizar pantalla
                    pygame.display.flip()
                    clock.tick(FPS)
                    
                    # Si el juego terminó, salir del bucle
                    if game_over:
                        break

# Salir del juego
pygame.quit()
sys.exit()

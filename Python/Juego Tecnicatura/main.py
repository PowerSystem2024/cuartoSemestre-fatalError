import pygame
import sys
import random
import os
from random import random
from personaje import Personaje, Enemigo, Explocion
from constantes import ASSETS_PATH, SCREEN_WIDTH, SCREEN_HEIGHT

# Inicializa el juego
def mostrar_imagen_inicial(screen, imagen_path, duracion):
    imagen = pygame.image.load(imagen_path).convert()
    imagen = pygame.transform.scale(imagen, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Bucle para mostrar la imagen principal con una opacidad
    alpha = 255  # transparencia inicial completa
    clock = pygame.time.Clock()

    tiempo_inicial = pygame.time.get_ticks()
    tiempo_total = duracion  # Duración en milisegundos (8000 ms para 8 segundos)

    while pygame.time.get_ticks() - tiempo_inicial < tiempo_total:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Aquí puedes agregar el código para renderizar la imagen con opacidad si lo deseas
        screen.blit(imagen, (0, 0))
        pygame.display.flip()
        
        clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fondo1 = pygame.image.load(FONDO1_PATH)
fondo1 = pygame.transform.scale(fondo1, (SCREEN_WIDTH, SCREEN_HEIGHT))

estrella = pygame.image.load(ESTRELLA_PATH)
estrella = pygame.transform.scale(estrella, (SCREEN_WIDTH, SCREEN_HEIGHT))

sonido_laser = pygame.mixer.Sound(f'{ASSETS_PATH}/sound/explosion.mp3')

personaje = Personaje(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
enemigos = []
explosiones = []
puntos = 0
nivel = 1

clock = pygame.time.Clock()
running = True

# Inicializar el fondo actual con el fondo original
fondo_actual = fondo1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:   # tecla hacia la derecha
        dx = -5
    if keys[pygame.K_RIGHT]:  # tecla hacia la izquierda
        dx = 5
    if keys[pygame.K_UP]:     # tecla hacia arriba
        dy = -5
    if keys[pygame.K_DOWN]:   # tecla hacia abajo
        dy = 5
        
        personaje.mover(dx, dy)
        
        if keys[pygame.K_SPACE]:
            if personaje.disparar():
                personaje.lanzar_laser()
                sonido_laser.play()
                
                
    for enemigo in enemigos:
        enemigo.mover()
        if enemigo.shape.top > SCREEN_HEIGHT:
            enemigos.remove(enemigo)
    for laser in personaje.lasers:import pygame
import sys
import random
import os
from personaje import Personaje, Enemigo, Explocion
from constantes import ASSETS_PATH, SCREEN_WIDTH, SCREEN_HEIGHT

# Inicializa el juego
def mostrar_imagen_inicial(screen, imagen_path, duracion):
    imagen = pygame.image.load(imagen_path).convert()
    imagen = pygame.transform.scale(imagen, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Bucle para mostrar la imagen principal con una opacidad
    alpha = 255  # transparencia inicial completa
    clock = pygame.time.Clock()

    tiempo_inicial = pygame.time.get_ticks()
    tiempo_total = duracion  # Duración en milisegundos (8000 ms para 8 segundos)

    while pygame.time.get_ticks() - tiempo_inicial < tiempo_total:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Aquí puedes agregar el código para renderizar la imagen con opacidad si lo deseas
        screen.blit(imagen, (0, 0))
        pygame.display.flip()
        
        clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fondo1 = pygame.image.load(FONDO1_PATH)
fondo1 = pygame.transform.scale(fondo1, (SCREEN_WIDTH, SCREEN_HEIGHT))

estrella = pygame.image.load(ESTRELLA_PATH)
estrella = pygame.transform.scale(estrella, (SCREEN_WIDTH, SCREEN_HEIGHT))

sonido_laser = pygame.mixer.Sound(f'{ASSETS_PATH}/sound/explosion.mp3')

personaje = Personaje(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
enemigos = []
explosiones = []
puntos = 0
nivel = 1

clock = pygame.time.Clock()
running = True

# Inicializar el fondo actual con el fondo original
fondo_actual = fondo1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:   # tecla hacia la derecha
        dx = -5
    if keys[pygame.K_RIGHT]:  # tecla hacia la izquierda
        dx = 5
    if keys[pygame.K_UP]:     # tecla hacia arriba
        dy = -5
    if keys[pygame.K_DOWN]:   # tecla hacia abajo
        dy = 5
        
        personaje.mover(dx, dy)
        
        if keys[pygame.K_SPACE]:
            if personaje.disparar():
                personaje.lanzar_laser()
                sonido_laser.play()
                
                
    for enemigo in enemigos:
        enemigo.mover()
        if enemigo.shape.top > SCREEN_HEIGHT:
            enemigos.remove(enemigo)
    for laser in personaje.lasers:import pygame
import sys
import random
import os
from personaje import Personaje, Enemigo, Explocion
from constantes import ASSETS_PATH, SCREEN_WIDTH, SCREEN_HEIGHT

# Inicializa el juego
def mostrar_imagen_inicial(screen, imagen_path, duracion):
    imagen = pygame.image.load(imagen_path).convert()
    imagen = pygame.transform.scale(imagen, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Bucle para mostrar la imagen principal con una opacidad
    alpha = 255  # transparencia inicial completa
    clock = pygame.time.Clock()

    tiempo_inicial = pygame.time.get_ticks()
    tiempo_total = duracion  # Duración en milisegundos (8000 ms para 8 segundos)

    while pygame.time.get_ticks() - tiempo_inicial < tiempo_total:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Aquí puedes agregar el código para renderizar la imagen con opacidad si lo deseas
        screen.blit(imagen, (0, 0))
        pygame.display.flip()
        
        clock.tick(60)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fondo1 = pygame.image.load(FONDO1_PATH)
fondo1 = pygame.transform.scale(fondo1, (SCREEN_WIDTH, SCREEN_HEIGHT))

estrella = pygame.image.load(ESTRELLA_PATH)
estrella = pygame.transform.scale(estrella, (SCREEN_WIDTH, SCREEN_HEIGHT))

sonido_laser = pygame.mixer.Sound(f'{ASSETS_PATH}/sound/explosion.mp3')

personaje = Personaje(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
enemigos = []
explosiones = []
puntos = 0
nivel = 1

clock = pygame.time.Clock()
running = True

# Inicializar el fondo actual con el fondo original
fondo_actual = fondo1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:   # tecla hacia la derecha
        dx = -5
    if keys[pygame.K_RIGHT]:  # tecla hacia la izquierda
        dx = 5
    if keys[pygame.K_UP]:     # tecla hacia arriba
        dy = -5
    if keys[pygame.K_DOWN]:   # tecla hacia abajo
        dy = 5
        
        personaje.mover(dx, dy)
        
        if keys[pygame.K_SPACE]:
            if personaje.disparar():
                personaje.lanzar_laser()
                sonido_laser.play()
                
                
    for enemigo in enemigos:
        enemigo.mover()
        if enemigo.shape.top > SCREEN_HEIGHT:
            enemigos.remove(enemigo)
    for laser in personaje.lasers:
        if enemigo.rect.colliderect(laser.rect):
            explosiones.append(Explocion(enemigo.rect.centerx, enemigo.rect.centery))
            enemigo.remover(enemigo)
            personaje.lasers.remove(laser)
            sonido_laser.play()
            puntos += 10
            break
    if enemigo.rect.colliderect(personaje.shape):
        if not personaje.recibir_dano():
            running = False
            
    if random.Random() <0.02:
        x = random.randint(0, SCREEN_WIDTH - 50)
        enemigo = enemigo(x, 0)
        enemigos.append(enemigo)
        
explosiones = [explosion for explosion in explosiones if explosion.actualizar()]

if puntos >= nivel * 250:
    if fondo_actual == fondo:
        fondo_actual = estrella
    else:
        fondo_actual = fondo1
        puntos = 0
        nivel += 1
    
    
    screen.blit(fondo_actual, (0, 0))
    personaje.dibujar(screen)
    for enemigo in enemigos:
        enemigo.dibujar(screen)
    for explosion in explosiones:
        explosion.dibujar(screen)
        
    font = pygame.font.Font(None, 36)
    texto_puntos = font.render(f'Puntos: {puntos}', True, (255, 255, 255))
    texto:nivel = font.render(f'Nivel: {nivel}', True, (255, 255, 255))
    screen.blit(texto_puntos, (10, 50))
    screen.blit(texto_nivel, (10, 90))
    
    
    pygame.display.flip()
    clock.tick(60)
    
    screen.fill((0, 0, 0))
    texto_game_over = font.render(f'GAME OVER! Puntos: {puntos}', True, (255, 0, 0))
    texto_mensaje_final = font.render('QUE LA FUERZA TE ACOMPAÑE', True, (255, 255, 255))
    
    screen.bilt ( texto_game_over, (SCREEN_WIDTH //2 -texto_game_over.get.width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    
    pygame.quit()
    sys.exit()
if _name_ == "_main_":
    main()
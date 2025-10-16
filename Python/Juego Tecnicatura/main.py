import pygame
import sys
import random
import os
from personaje import Personaje,Enemigo,Explocion
from constantes import assets_path 

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

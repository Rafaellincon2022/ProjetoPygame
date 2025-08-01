#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import ENTITY_SPEED, WINDOW_HEIGHT, WINDOW_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        # Variável para armazenar a tecla pressionada
        pressed_key = pygame.key.get_pressed()
        # Verifica se a tecla é seta cima e se o retângulo da nave está no topo
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        # Verifica se a tecla é seta baixo e se o retângulo da nave está na parte mais baixa da tela
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        # Verifica se a tecla é seta esquerda e se o retângulo da nave está colada no lado esquerdo
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        # Verifica se a tecla é seta direita e se o retângulo da nave está na parte final à direita
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WINDOW_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

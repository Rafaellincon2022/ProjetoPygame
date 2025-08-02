#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.PlayerShot import PlayerShot
from code.const import ENTITY_SPEED, WINDOW_HEIGHT, WINDOW_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Aqui gerenciamos o delay entre um tiro e outro
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

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

    # Definição dos tiros
    def Shoot(self):
        # O tiro terá um delay de ele mesmo - 1
        self.shot_delay -= 1
        # Até chegar em zero e aqui, verificamos:
        if self.shot_delay == 0:
            # A variável recebe a quantidade original
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            # Variável da tecla pressionada
            pressed_key = pygame.key.get_pressed()
            # Se a tecla estiver pressionada
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                # Retorna a imagem do tiro na posição central da nave
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

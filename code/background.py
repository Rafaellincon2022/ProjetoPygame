#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WINDOW_WIDTH, ENTITY_SPEED
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        # O centerx seria o controle de velocidade
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # Se o canto direito da imagem chegar na posição 0
        if self.rect.right <= 0:
            # A imagem retorna para a posição mais à esquerda da tela
            self.rect.left = WINDOW_WIDTH
        pass

#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        # Carregamos as imagens genéricas, porque podemos carregar imagens para o fundo, inimigos ou a nave
        self.surf = pygame.image.load('./assets/' + name + '.png')
        # Desenhamos o retângulo nas posições informadas
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass

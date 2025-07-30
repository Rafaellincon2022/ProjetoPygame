#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import trunc

import pygame.display

from code.entity import Entity
from code.entity_Factory import Entity_Factory

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode

        # Criamos uma lista vazia
        self.entity_list: list[Entity] = []
        # Instanciamos a lista com todos os objetos inseridos na fábrica
        self.entity_list.extend(Entity_Factory.get_entity('Level1Bg'))

    def run(self):
        while True:
            # Pegamos imagem por imagem da lista e jogamos em tela
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            pygame.display.flip()
        pass


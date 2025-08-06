#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.EnemyShot import EnemyShot
from code.const import ENTITY_SPEED, WINDOW_WIDTH, ENTITY_SHOT_DELAY
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        # A nave chega no final apenas - será destruída pelo mediator
        self.rect.centerx -= ENTITY_SPEED[self.name]

    # Definição dos tiros
    def Shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
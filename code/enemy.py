#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED, WINDOW_WIDTH
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        # A nave chega no final apenas - será destruída pelo mediator
        self.rect.centerx -= ENTITY_SPEED[self.name]

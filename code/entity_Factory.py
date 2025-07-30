#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WINDOW_WIDTH


class Entity_Factory:

    # Definimos que esse método é estático
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    # Precisamos inserir 7 imagens inicialmente
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    # Inserimos + 7 totalizando 14. Dessa forma, as 7 primeiras acabam e inicia as próximas 7
                    list_bg.append(Background(f'Level1Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
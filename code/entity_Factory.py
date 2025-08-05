#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.enemy import Enemy
from code.player import Player


class Entity_Factory:

    # Definimos que esse método é estático
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                # Laço referente às 7 imagens do level 1
                for i in range(7):
                    # Precisamos inserir 7 imagens inicialmente
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    # Inserimos + 7 totalizando 14. Dessa forma, as 7 primeiras acabam e inicia as próximas 7
                    list_bg.append(Background(f'Level1Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                # Laço referente às 5 imagens do level 2
                for i in range(5):
                    # Precisamos inserir 5 imagens inicialmente do level 2
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    # Inserimos + 5 totalizando 10. Dessa forma, as 5 primeiras acabam e inicia as próximas 5
                    list_bg.append(Background(f'Level2Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg

            # Implementação do jogador 1 e a posição inicial no jogo
            case 'Player1':
                return Player('Player1', (10, WINDOW_HEIGHT / 2 - 30))

            # Implementação do jogador 2 e a posição inicial no jogo
            case 'Player2':
                return Player('Player2', (10, WINDOW_HEIGHT / 2 + 30))

            # Implementação do inimigo 1 e a posição inicial dele em tela
            case 'Enemy1':
                return Enemy('Enemy1', (WINDOW_WIDTH + 10, random.randint(20, WINDOW_HEIGHT - 20)))

            # Implementação do inimigo 2 e a posição inicial dele em tela
            case 'Enemy2':
                return Enemy('Enemy2', (WINDOW_WIDTH + 10, random.randint(20, WINDOW_HEIGHT - 20)))
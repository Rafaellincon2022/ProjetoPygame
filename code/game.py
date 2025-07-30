#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importando a biblioteca PyGame
import pygame

from code.level import Level
from code.menu import Menu
from code.const import WINDOW_HEIGHT, WINDOW_WIDTH, MENU_OPTION


class Game:
    def __init__(self):
        # Instanciando nosso objeto
        pygame.init()

        # Criando a janela onde acontecerá nosso jogo - passamos em pixels
        # Iremos criar uma tela pequena inicialmente - 600 x 480
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        # Loop para manter capturar os eventos do nosso jogo
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            # Se as opções de menu forem uma das jogáveis, executa o LEVEL.RUN()
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()

            else:
                pass

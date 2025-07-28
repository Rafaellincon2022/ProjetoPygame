#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importando a biblioteca PyGame
import pygame
from code.menu import Menu
from code.const import WINDOW_HEIGHT, WINDOW_WIDTH

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
            menu.run()
            pass


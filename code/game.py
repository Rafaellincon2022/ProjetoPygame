#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importando a biblioteca PyGame
import pygame
from code.menu import Menu

class Game:
    def __init__(self):
        # Instanciando nosso objeto
        pygame.init();

        # Criando a janela onde acontecerá nosso jogo - passamos em pixels
        # Iremos criar uma tela pequena inicialmente - 600 x 480
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        # Loop para manter capturar os eventos do nosso jogo
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # EVENT.GET() é o método que captura os eventos
            for event in pygame.event.get():
                # Se o evento for do tipo QUIT sai do jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # Finaliza o jogo e fecha a tela
                    quit()


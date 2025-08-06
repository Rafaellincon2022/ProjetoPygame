#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importando a biblioteca PyGame
import pygame

from code.level import Level
from code.menu import Menu
from code.const import WINDOW_HEIGHT, WINDOW_WIDTH, MENU_OPTION
from code.score import Score


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
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            # Se as opções de menu forem uma das jogáveis, executa o LEVEL.RUN()
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                # Criamos uma variável que irá armazenar a pontuação dos jogadores
                player_score = [0, 0]
                # Chama o Level 1 em tela
                level = Level(self.window, 'Level1', menu_return, player_score)
                # Armamzena o retorno do level
                level_return = level.run(player_score)

                # Se o retorno for True
                if level_return:
                    # Chamamos o Level 2 em tela
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    # Armamzena o retorno do level
                    level_return = level.run(player_score)

                    # Se o jogador passou pela fase nível 2 até o fim
                    if menu_return:
                        # Passa para a função o parâmetro de qual foi o jogador (P1 ou P2) e a pontuação do jogador
                        score.save_score(menu_return, player_score)

            # Se a opção for para mostrar o SCORE atual dos jogadores
            elif menu_return == MENU_OPTION[3]:
                score.show_score()

            # Se a opção for para SAIR do jogo
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()

            else:
                pass
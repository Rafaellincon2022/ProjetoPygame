#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WINDOW_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        # Carregamos uma imagem
        self.surf = pygame.image.load("./assets/MenuBg.png")
        # Criamos um retângulo
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        # Inserindo música em nosso menu
        pygame.mixer_music.load("./assets/Menu.mp3")
        # O parâmetro -1 indica que é pra tocar indefinidamente
        pygame.mixer_music.play(-1)

        while True:
            # Colocamos nossa imagem dentro do retângulo
            self.window.blit(source=self.surf, dest=self.rect)

            # Inserindo os textos do nosso menu
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WINDOW_WIDTH / 2), 120))

            # Mostrando o MENU com as opções ao usuário
            for i in range(len(MENU_OPTION)):
                self.menu_text(20,MENU_OPTION[i], COLOR_WHITE, ((WINDOW_WIDTH / 2), 200 + 25 * i))

            # Método para mostrar o objeto em tela
            pygame.display.flip()
            #pass

            # EVENT.GET() é o método que captura os eventos
            for event in pygame.event.get():
                # Se o evento for do tipo QUIT sai do jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # Finaliza o jogo e fecha a tela
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font
from code.const import COLOR_WHITE, WINDOW_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIMER
from code.entity import Entity
from code.entity_Factory import Entity_Factory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode

        # Criamos uma lista vazia
        self.entity_list: list[Entity] = []
        # Instanciamos a lista com todos os objetos inseridos na fábrica
        self.entity_list.extend(Entity_Factory.get_entity('Level1Bg'))
        # Instanciamos tudo o que irá ser carregado junto com nosso level - nave do jogador
        self.entity_list.append(Entity_Factory.get_entity('Player1'))

        # Verificamos o MODO DE JOGO para criarmos as naves do jogador 2
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(Entity_Factory.get_entity('Player2'))

        # Definindo que os inimigos irão aparecer em tela a cada 2 segundos
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIMER)

    def run(self):
        # Carregamos uma música para o level 1
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        # A música será tocada indefinidamente -1
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            # Definimos o FPS em 60 - Quanto maior o FPS, mais rápido será o jogo
            clock.tick(60)
            # Pegamos imagem por imagem da lista e jogamos em tela
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()

            # Evento para finalizarmos o jogo mesmo com ele em execução
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Evento para acionarmos o EVENT_ENEMY e de fato criarmos os inimigos
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(Entity_Factory.get_entity(choice))

            # Mostra o tempo de duração da fase
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            # Mostra o FPS em tela
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WINDOW_HEIGHT - 35))
            # Mostra a quantidade de objetos criados em tela (fundos, inimigos, jogador)
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WINDOW_HEIGHT - 20))

            pygame.display.flip()

    # Definição do método para configurar as fontes em tela
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font
from code.const import COLOR_WHITE, WINDOW_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIMER, COLOR_GREEN, COLOR_CYAN, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.enemy import Enemy
from code.entity import Entity
from code.entity_Factory import Entity_Factory
from code.entity_mediator import Entity_Mediator
from code.player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode

        # Criamos uma lista vazia
        self.entity_list: list[Entity] = []
        # Instanciamos a lista com todos os objetos inseridos na fábrica
        self.entity_list.extend(Entity_Factory.get_entity(self.name + 'Bg'))
        # Instanciamos tudo o que irá ser carregado junto com nosso level - nave do jogador
        # self.entity_list.append(Entity_Factory.get_entity('Player1'))

        # Criamos uma variável para armazenar o jogador 1
        player = Entity_Factory.get_entity('Player1')
        # A variável utiliza o método score para receber a pontuação do jogador 1 (posição 0)
        player.score = player_score[0]
        # Agora nós fazemos o append da lista
        self.entity_list.append(player)

        # Verificamos o MODO DE JOGO para criarmos as naves do jogador 2
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            # self.entity_list.append(Entity_Factory.get_entity('Player2'))

            # Criamos uma variável para armazenar o jogador 1
            player = Entity_Factory.get_entity('Player2')
            # A variável utiliza o método score para receber a pontuação do jogador 2 (posição 1)
            player.score = player_score[1]
            # Agora nós fazemos o append da lista
            self.entity_list.append(player)

        # Definindo que os inimigos irão aparecer em tela a cada 2 segundos
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIMER)

        # Evento para identificar a vitória do jogador e finalização do level
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
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

                # Instanciamos os tiros, seja do inimigo, seja do jogador na lista de entidades
                if isinstance(entity, (Player, Enemy)):
                    # Variável para receber o retorno dos tiros
                    shoot = entity.Shoot()
                    # Verifica se o retorno não é vazio
                    if shoot is not None:
                        # Se existir retorno, adiciona na lista de entidades
                        self.entity_list.append(shoot)

                # Mostra a saúde do Player 1
                if entity.name == 'Player1':
                    self.level_text(14, f'Player 1 - Health: {entity.health} | Score: {entity.score}', COLOR_GREEN, (10, 25))

                # Mostra a saúde do Player 2
                if entity.name == 'Player2':
                    self.level_text(14, f'Player 2 - Health: {entity.health} | Score: {entity.score}', COLOR_CYAN, (10, 45))

            # Evento para finalizarmos o jogo mesmo com ele em execução
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Evento para acionarmos o EVENT_ENEMY e de fato criarmos os inimigos
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(Entity_Factory.get_entity(choice))

                # Evento para checar se é do tipo TIMEOUT
                if event.type == EVENT_TIMEOUT:
                    # Retira a quantidade (STEP) do timeout definido
                    self.timeout -= TIMEOUT_STEP
                    # Quando o timeout chega em 0, retorna TRUE
                    if self.timeout == 0:
                        # Aqui nós varremos as entidades da lista
                        for entity in self.entity_list:
                            # Se existir o P1, atualizamos o score
                            if isinstance(entity, Player) and entity.name == 'Player1':
                                player_score[0] = entity.score
                            # Se existir o P2, atualizamos o score
                            if isinstance(entity, Player) and entity.name == 'Player2':
                                player_score[1] = entity.score
                        return True

                # Busca jogador
                found_player = False
                # Verifica se o player existe
                for entity in self.entity_list:
                    # Se existe uma instância de Player (pode ser P1 ou P2)
                    if isinstance(entity, Player):
                        found_player = True

                # Se o jogador não for encontrado, retorna False
                if not found_player:
                    return False

            # Mostra o tempo de duração da fase
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            # Mostra o FPS em tela
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WINDOW_HEIGHT - 35))
            # Mostra a quantidade de objetos criados em tela (fundos, inimigos, jogador)
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WINDOW_HEIGHT - 20))

            pygame.display.flip()

            # Chamada do método para gerenciar as colisões
            Entity_Mediator.verify_collision(entity_list=self.entity_list)
            # Chamada do método para remover as entidades sem vida
            Entity_Mediator.verify_health(entity_list=self.entity_list)

    # Definição do método para configurar as fontes em tela
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
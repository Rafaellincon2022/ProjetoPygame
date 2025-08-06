import sys
from datetime import datetime

import pygame.image
from pygame import Surface, Rect, K_BACKSPACE, KEYDOWN, K_RETURN, K_ESCAPE
from pygame.font import Font

from code.const import COLOR_YELLOW, SCORE_POSITION, MENU_OPTION, COLOR_WHITE
from code.dbproxy import DBProxy


# Definição da classe
class Score:

    def __init__(self, window):
        # Definimos a janela
        self.window = window
        # Carregamos a imagem
        self.surf = pygame.image.load('./assets/ScoreBg.png').convert_alpha()
        # Criamos o retângulo
        self.rect = self.surf.get_rect(left=0, top=0)

    # Função para salvar a pontuação
    def save_score(self, game_mode: str, player_score: list[int]):
        # Carregamos a música
        pygame.mixer_music.load('./assets/Score.mp3')
        pygame.mixer_music.play(-1)

        # Conectando ao banco de dados
        db_proxy = DBProxy('DBScore')

        # Variável para salvar o nome do jogador
        name = ''

        while True:
            # Desenhamos a imagem dentro do retângulo
            self.window.blit(source=self.surf, dest=self.rect)

            # Chamamos a função para gravar o texto em tela
            self.text_score(48, 'YOU WIN', COLOR_YELLOW, SCORE_POSITION['Title'])

            # Variável que armazena a string para solicitar o nome do jogar
            text = 'Enter Team Name (4 characters): '
            # Variável que armazena a string para solicitar o nome do jogar
            score = player_score[0]

            # Se o modo de jogo for 1 jogador
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]

            # Se o modo de jogo for COLABORATIVO, pega o total dos jogadores e divide por 2
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2

            # Se o modo de jogo for COMPETITIVO, Verifica qual dos dois jogadores teve maior placar
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters): '

            # Escreve o nome do jogador vencedor em tela
            self.text_score(20, text, COLOR_WHITE, SCORE_POSITION['EnterName'])

            # Permite fechar a janela de Score
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Se usuário pressionou tecla
                elif event.type == KEYDOWN:
                    # Se a tecla for ENTER
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})

                        # Mostra a tela de SCORE após salvar
                        self.show_score()
                        return

                    # Se a tecla for BACKSPACE
                    elif event.key == K_BACKSPACE:
                        # Apaga o último caractere digitado
                        name = name[:-1]

                    # Se for qualquer outra tecla
                    else:
                        if len(name) < 4:
                            name += event.unicode

            # Mostra o texto digitado em tela
            self.text_score(20, name, COLOR_WHITE, SCORE_POSITION['Name'])

            # Mostramos a imagem em tela
            pygame.display.flip()

    # Função para mostrar a pontuação
    def show_score(self):
        # Carregamos a música
        pygame.mixer_music.load('./assets/Score.mp3')
        pygame.mixer_music.play(-1)
        # Desenhamos a imagem dentro do retângulo
        self.window.blit(source=self.surf, dest=self.rect)

        # Escrevemos o texto
        self.text_score(48, 'TOP 10 SCORE', COLOR_YELLOW, SCORE_POSITION['Title'])
        self.text_score(20, 'NAME     SCORE           DATE      ', COLOR_YELLOW, SCORE_POSITION['Label'])

        # Fazemos a conexão ao banco de dados
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.text_score(20, f'{name}     {score:05d}     {date}', COLOR_YELLOW, SCORE_POSITION[list_score.index(player_score)])

        while True:
            # Permite fechar a janela de Score
            for event in pygame.event.get():
                # Evento para fechar a janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Evento para a tecla ESC - Retorna ao MENU
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            # Mostramos a imagem em tela
            pygame.display.flip()

    # Função para escrever texto em tela
    def text_score(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

# Função para mostrarmos a data e hora atual
def get_formatted_date():
    # Pega a data e hora atual do computador
    current_datetime = datetime.now()
    # Converte o tempo em Horas e Minutos
    current_time = current_datetime.strftime('%H:%M')
    # Converte a data em DIA/MÊS/ANO
    current_date = current_datetime.strftime('%d/%m/%y')
    # Retorna formatado
    return f'{current_time} - {current_date}'
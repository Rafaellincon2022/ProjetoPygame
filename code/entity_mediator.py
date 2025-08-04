from code import entity
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.const import WINDOW_WIDTH
from code.enemy import Enemy
from code.entity import Entity
from code.player import Player


class Entity_Mediator:

    @staticmethod
    # Essa função irá verificar se as naves inimigas atingiram o limite da tela para destruí-los
    def __verify_collision_window(ent: Entity):
        # Verifica se a instância criada é de inimigos apenas
        if isinstance(ent, Enemy):
            # Verificar se ela está fora da tela
            if ent.rect.right <= 0:
                # Recebe 0 de vida - mas ainda não é destruída
                ent.health = 0

        # Precisamos destruir também os tiros do jogador que estão saindo da tela
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WINDOW_WIDTH:
                ent.health = 0

        # Precisamos destruir também os tiros do inimigo que estão saindo da tela
        if isinstance(ent, EnemyShot):
            # Se os tiros saindo da direita para a esquerda forem <= 0
            if ent.rect.right <= 0:
                # A vida recebe 0
                ent.health = 0

    @staticmethod
    # Essa função irá verificar se as naves colidiram entre si
    def __verify_collision_entity(entity1, entity2):
        valid_interaction = False

        # Verifica se é um inimigo e um tiro do jogador
        if isinstance(entity1, Enemy) and isinstance(entity2, PlayerShot):
            valid_interaction = True
        # # Verifica se é um tiro do jogador e um inimigo
        elif isinstance(entity1, PlayerShot) and isinstance(entity2, Enemy):
            valid_interaction = True
        # Verifica se é um jogador e um tiro do inimigo
        elif isinstance(entity1, Player) and isinstance(entity2, EnemyShot):
            valid_interaction = True
        # Verifica se é um tiro do inimigo e um jogador
        elif isinstance(entity1, EnemyShot) and isinstance(entity2, Player):
            valid_interaction = True

        # Houve interação. Agora verifica se a interação foi dentro desses critérios com a colisão
        if valid_interaction:
            if (entity1.rect.right >= entity2.rect.left and entity1.rect.left <= entity2.rect.right and
               entity1.rect.bottom >= entity2.rect.top and  entity1.rect.top <= entity2.rect.bottom
            ):
                # Ambas as entidades sofrem dano
                entity1.health -= entity2.damage
                entity2.health -= entity1.damage

                # Variáveis para controlarmos o score de quem deu o último dano
                entity1.last_dmg = entity2.name
                entity2.last_dmg = entity1.name

    @staticmethod
    # Esse método irá gerenciar o score do jogador
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        # Verifica quem deu o último dano
        if enemy.last_dmg == 'Player1Shot':
            # Varre a lista de entidades
            for ent in entity_list:
                # Localiza o P1
                if ent.name == 'Player1':
                    # Adiciona aos pontos do P1
                    ent.score += enemy.score

        # Verifica quem deu o último dano
        if enemy.last_dmg == 'Player2Shot':
            # Varre a lista de entidades
            for ent in entity_list:
                # Localiza o P2
                if ent.name == 'Player2':
                    # Adiciona aos pontos do P2
                    ent.score += enemy.score

    @staticmethod
    # Essa função irá gerenciar as colisões entre naves
    def verify_collision(entity_list: list[Entity]):
        # Percorremos cada entidade da lista, uma por uma
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            # Para cada entidade chamamos outra função
            Entity_Mediator.__verify_collision_window(entity1)

            # Aqui iremos comparar cada com as outras que virão depois dela
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                # Chamamos outra função que verifica as colisões entre si, passando ambas entidades como parâmetro
                Entity_Mediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    # Essa função verificar o nível de vida das entidades
    def verify_health(entity_list: list[Entity]):
        # Para cada entidade dentro da lista
        for ent in entity_list:
            # Se a entidade estiver com vida menor ou igual a 0
            if ent.health <= 0:
                # Iremos verificar se a entidade destruída é um inimigo para pontuar ao jogador
                if isinstance(ent, Enemy):
                    # Verifica quem realizou o abate (P1 ou P2) e quem ele abateu
                    Entity_Mediator.__give_score(ent, entity_list)
                # Aqui ela será destruída
                entity_list.remove(ent)


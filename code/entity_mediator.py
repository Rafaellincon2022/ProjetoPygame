from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.const import WINDOW_WIDTH
from code.enemy import Enemy
from code.entity import Entity


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
    # Essa função irá gerenciar as colisões entre naves
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity = entity_list[i]
            Entity_Mediator.__verify_collision_window(entity)

    @staticmethod
    # Essa função verificar o nível de vida das entidades
    def verify_health(entity_list: list[Entity]):
        # Para cada entidade dentro da lista
        for ent in entity_list:
            # Se a entidade estiver com vida menor ou igual a 0
            if ent.health <= 0:
                # Aqui ela será destruída
                entity_list.remove(ent)


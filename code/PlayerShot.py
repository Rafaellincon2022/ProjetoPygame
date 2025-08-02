from code.const import ENTITY_SPEED
from code.entity import Entity

# Definição da classe de tiro do jogador
class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # O tiro irá se mover em linha reta sempre para a direita
    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]

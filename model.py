import random
import creatures
import entities


class Model:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.entities = {}

    def add_entity(self, new_entity, is_randomly=False):
        # if (not is_randomly and
        #         0 <= new_entity.position.x < self.width and
        #         0 <= new_entity.position.y < self.height and
        #         self.get_entity(new_entity.position) is None):
        #     self.entities[new_entity.position] = new_entity
        #     if issubclass(new_entity.__class__, creatures.Creature):
        #         new_entity.field = self
        #     return True
        if is_randomly:
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            random_position = entities.Position(x, y)
            if self.get_entity(random_position) is None:
                new_entity.set_position(random_position)
                self.entities[random_position] = new_entity
                if issubclass(new_entity.__class__, creatures.Creature):
                    new_entity.set_model(self)
                return True
            return False

    def get_entity(self, position: entities.Position):
        for point in self.entities.keys():
            if point.x == position.x and point.y == position.y:
                return self.entities[point]
        return None

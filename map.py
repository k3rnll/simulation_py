import random

import creatures


class Map:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.entities = {}

    def add_entity(self, new_entity, is_randomly=False):
        if (not is_randomly and
                0 <= new_entity.position.x < self.width and
                0 <= new_entity.position.y < self.height and
                self.get_entity(new_entity.position) is None):
            self.entities[new_entity.position] = new_entity
            if new_entity is creatures.Creature:
                new_entity.field = self
            return True
        elif is_randomly:
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            new_entity.position.x = x
            new_entity.position.y = y
            if self.get_entity(new_entity.position) is None:
                self.entities[new_entity.position] = new_entity
                if new_entity is creatures.Creature:
                    new_entity.field = self
                return True
            return False

    def get_entity(self, position):
        for point in self.entities.keys():
            if point.x == position.x and point.y == position.y:
                return self.entities[point]
        return None

    def delete_entity(self, position):
        for point in self.entities.keys():
            if point.x == position.x and point.y == position.y:
                del self.entities[point]
                return True

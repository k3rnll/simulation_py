import random
import creatures
import entities


class Model:
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        self.__entities = {}

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def entities_on_grid(self):
        return self.__entities

    def __is_point_correct(self, point: entities.Position):
        return 0 <= point.x < self.__width and 0 <= point.y < self.height

    def __put_entity_on_grid(self, new_entity, position_to: entities.Position):
        new_entity.set_position(position_to)
        self.__entities[position_to] = new_entity
        if issubclass(new_entity.__class__, creatures.Creature):
            new_entity.set_model(self)

    def add_entity_manually(self, new_entity, position_to: entities.Position):
        if self.__is_point_correct(position_to) and self.get_entity(position_to) is None:
            self.__put_entity_on_grid(new_entity, position_to)
            return True
        return False

    def add_entity_randomly(self, new_entity):
        random_x = random.randrange(0, self.__width)
        random_y = random.randrange(0, self.height)
        random_position = entities.Position(random_x, random_y)
        if self.get_entity(random_position) is None:
            self.__put_entity_on_grid(new_entity, random_position)
            return True
        return False

    def get_entity(self, position: entities.Position):
        for point in self.__entities.keys():
            if point.x == position.x and point.y == position.y:
                return self.__entities[point]
        return None

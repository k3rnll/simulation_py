import random
import creatures
import entities
from entities import Position


class Cell:
    def __init__(self):
        self.__items = set()

    def add_item(self, item: entities.Entity):
        if item:
            self.items.add(item)

    def clear_items(self):
        self.__items.clear()

    @property
    def items(self):
        return self.__items


class Grid:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__cells = [Cell() for _ in range(width * height)]

    def __is_point_in_grid_range(self, x, y):
        return (x in range(0, self.__width) and
                y in range(0, self.__height))

    def get_cell_on(self, x: int, y: int):
        if self.__is_point_in_grid_range(x, y):
            return self.__cells[self.__width * y + x]
        return None

    @property
    def cells(self):
        return self.__cells

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


class Model:
    def __init__(self, height: int, width: int):
        self.__grid = Grid(width, height)
        self.__height = height
        self.__width = width
        self.__entities = {}

    @property
    def grid(self):
        return self.__grid

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def entities_dict(self):
        return self.__entities

    def entities_on_grid(self, spec_type=entities.Entity):
        entities_list = []
        for obj in self.__entities.values():
            if isinstance(obj, spec_type):
                entities_list.append(obj)
        return entities_list

    def is_valid_point(self, point: entities.Position):
        return 0 <= point.x < self.__width and 0 <= point.y < self.height

    @classmethod
    def __update_entity_position(cls, entity: entities.Entity, new_point: entities.Position):
        entity.position.x = new_point.x
        entity.position.y = new_point.y

    def __put_entity_on_grid(self, new_entity, position_to: entities.Position):
        self.__update_entity_position(new_entity, position_to)
        self.__entities[new_entity.position] = new_entity
        if issubclass(new_entity.__class__, creatures.Creature):
            new_entity.set_model(self)

    def add_entity_manually(self, entity, position_to: Position):
        cell = self.__grid.get_cell_on(position_to.x, position_to.y)
        if cell:
            cell.add_item(entity)

    def add_entity_randomly(self, entity):
        random_x = random.randrange(0, self.grid.width)
        random_y = random.randrange(0, self.grid.height)
        self.add_entity_manually(entity, Position(random_x, random_y))

    def get_entity(self, position: entities.Position):
        for point in self.__entities.keys():
            if point.x == position.x and point.y == position.y:
                return self.__entities[point]
        return None

    def is_able_to_stand_point(self, point: entities.Position):
        obj = self.get_entity(point)
        if (self.is_valid_point(point) and obj is None or
                isinstance(obj, entities.Grass)):
            return True
        return False

    def update_entity_position(self, entity: entities.Entity, new_point: entities.Position):
        if (entity in self.__entities.values() and
                self.is_able_to_stand_point(new_point)):
            entity.position.x = new_point.x
            entity.position.y = new_point.y
            return True
        return False

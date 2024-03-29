import random
from creatures import Creature, Herbivore, Predator
from entities import Position, Entity, Rock, Tree, Grass


class Cell:
    def __init__(self):
        self.__items = list()

    def add_item(self, item: Entity):
        if item:
            self.items.append(item)

    def remove_item(self, item: Entity):
        if item in self.__items:
            self.__items.remove(item)

    def clear_items(self):
        self.__items.clear()

    @property
    def items(self) -> list[Entity]:
        return self.__items


class Grid:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__cells = [Cell() for _ in range(width * height)]

    def __is_point_in_grid_range(self, x, y):
        return (x in range(0, self.__width) and
                y in range(0, self.__height))

    def get_cell_on(self, x: int, y: int) -> Cell | None:
        if self.__is_point_in_grid_range(x, y):
            return self.__cells[self.__width * y + x]
        return None

    @property
    def cells(self) -> list[Cell]:
        return self.__cells

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height


class CreaturesHandler:
    def __init__(self, grid: Grid):
        self.__grid = grid
        self.__creatures_list = list()

    @property
    def alive_creatures_amount(self) -> int:
        amount = 0
        for creature in self.__creatures_list:
            if not creature.is_dead:
                amount += 1
        return amount

    def __update_creatures_list(self):
        self.__creatures_list.clear()
        for cell in self.__grid.cells:
            for obj in cell.items:
                if isinstance(obj, Creature):
                    self.__creatures_list.append(obj)

    def move_all_creatures(self):
        self.__update_creatures_list()
        for creature in self.__creatures_list:
            creature.move()

    def hit_creatures_by_hunger(self):
        self.__update_creatures_list()
        for creature in self.__creatures_list:
            creature.hit_by_hunger()

    def ask_all_to_eat(self):
        self.__update_creatures_list()
        for creature in self.__creatures_list:
            creature.eat()


class CellContentRules:
    def __init__(self, grid: Grid):
        self.__grid = grid
        self.__can_stand_on_types = Grass
        self.__cant_stand_on_types = (
            Rock,
            Tree,
            Herbivore,
            Predator,
        )

    @staticmethod
    def is_cell_have_obj_type(cell: Cell, obj_type: type | tuple[type, ...]) -> bool:
        for obj in cell.items:
            if isinstance(obj, obj_type):
                return True
        return False

    def is_cell_have_grass(self, cell: Cell) -> bool:
        return self.is_cell_have_obj_type(cell, Grass)

    def is_cell_standable(self, cell: Cell) -> bool:
        return not self.is_cell_have_obj_type(cell, self.__cant_stand_on_types)


class Model:
    def __init__(self, width: int, height: int):
        self.__grid = Grid(width, height)
        self.__creatures_handler = CreaturesHandler(self.__grid)
        self.__cell_content_rules = CellContentRules(self.__grid)

    @property
    def grid(self) -> Grid:
        return self.__grid

    @property
    def creatures_handler(self) -> CreaturesHandler:
        return self.__creatures_handler

    def add_entity_manually(self, entity, position_to: Position) -> bool:
        cell = self.__grid.get_cell_on(position_to.x, position_to.y)
        if not cell:
            return False
        if self.__cell_content_rules.is_cell_have_obj_type(cell, entity.__class__):
            return False
        if self.__cell_content_rules.is_cell_standable(cell):
            cell.add_item(entity)
            entity.position.x = position_to.x
            entity.position.y = position_to.y
            if isinstance(entity, Creature):
                entity.set_model(self)
            return True
        return False

    def add_entity_randomly(self, entity):
        random_x = random.randrange(0, self.grid.width)
        random_y = random.randrange(0, self.grid.height)
        self.add_entity_manually(entity, Position(random_x, random_y))

    def remove_entity(self, entity: Entity, position: Position):
        cell = self.__grid.get_cell_on(position.x, position.y)
        if cell:
            cell.remove_item(entity)

    def change_entity_position(self, entity: Entity, new_position: Position) -> bool:
        old_position = Position(entity.position.x, entity.position.y)
        if self.add_entity_manually(entity, new_position):
            self.remove_entity(entity, old_position)
            return True
        return False

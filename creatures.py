from abc import ABCMeta, abstractmethod
from entities import Entity, Position, Grass, Rock, Tree
from params import SimulationParams
import random
import coord


class IMovable(metaclass=ABCMeta):
    @abstractmethod
    def move_up(self):
        pass

    @abstractmethod
    def move_down(self):
        pass

    @abstractmethod
    def move_left(self):
        pass

    @abstractmethod
    def move_right(self):
        pass

    @abstractmethod
    def move_up_left(self):
        pass

    @abstractmethod
    def move_up_right(self):
        pass

    @abstractmethod
    def move_down_left(self):
        pass

    @abstractmethod
    def move_down_right(self):
        pass


class Creature(Entity):
    def __init__(self, icon: str):
        super().__init__(icon)
        self._hp = 100
        self.__model = None
        self.__vision = Vision(self)
        self.__movement = MovementHandle(self)

    @abstractmethod
    def eat(self):
        pass

    @property
    def model(self):
        return self.__model

    def set_model(self, to_model):
        self.__model = to_model

    @property
    def icon(self) -> str:
        return super().icon if self._hp > 0 else 'X'

    @property
    def is_dead(self) -> bool:
        return self._hp <= 0

    @property
    def entities_in_sight(self) -> set:
        return self.__vision.entities_in_sight

    def make_random_move(self):
        x = random.randrange(0, 8)
        match x:
            case 0: self.__movement.move_up()
            case 1: self.__movement.move_down()
            case 2: self.__movement.move_left()
            case 3: self.__movement.move_right()
            case 4: self.__movement.move_up_left()
            case 5: self.__movement.move_up_right()
            case 6: self.__movement.move_down_left()
            case 7: self.__movement.move_down_right()

    def change_hp_by(self, amount: int):
        if 0 < self._hp <= 100:
            self._hp += amount
            self._hp = 100 if self._hp > 100 else self._hp
            self._hp = 0 if self._hp < 0 else self._hp

    def _get_next_point_to_target(self, target: Entity) -> Position:
        return coord.get_points_of_vector(self.position, target.position)[0]

    def _move_to_target(self, target: Entity) -> bool:
        next_point = self._get_next_point_to_target(target)
        return self.model.change_entity_position(self, next_point)


class MovementHandle(IMovable):
    def __init__(self, owner: Creature):
        self.__owner = owner

    def move_up(self):
        if self.__owner.model:
            new_point = Position(self.__owner.position.x, self.__owner.position.y - 1)
            self.__owner.model.change_entity_position(self.__owner, new_point)

    def move_down(self):
        if self.__owner.model:
            new_point = Position(self.__owner.position.x, self.__owner.position.y + 1)
            self.__owner.model.change_entity_position(self.__owner, new_point)

    def move_left(self):
        if self.__owner.model:
            new_point = Position(self.__owner.position.x - 1, self.__owner.position.y)
            self.__owner.model.change_entity_position(self.__owner, new_point)

    def move_right(self):
        if self.__owner.model:
            new_point = Position(self.__owner.position.x + 1, self.__owner.position.y)
            self.__owner.model.change_entity_position(self.__owner, new_point)

    def move_up_right(self):
        self.move_up()
        self.move_right()

    def move_up_left(self):
        self.move_up()
        self.move_left()

    def move_down_right(self):
        self.move_down()
        self.move_right()

    def move_down_left(self):
        self.move_down()
        self.move_left()


class Vision:
    def __init__(self, owner: Creature):
        self.__owner = owner
        self.__distance = SimulationParams.creatures_default_vision_distance
        if isinstance(owner, Herbivore):
            self.__distance = SimulationParams.herbivore_vision_distance
        if isinstance(owner, Predator):
            self.__distance = SimulationParams.predator_vision_distance
        self.__solid_obj_types = (Rock, Tree, Creature)
        self.__entities_in_sight = set()

    @property
    def entities_in_sight(self) -> set:
        if self.__owner.model:
            self.__look_around()
        return self.__entities_in_sight

    def __look_around(self):
        self.__entities_in_sight.clear()
        vision_border_points_list = coord.get_points_list_of_borderline(self.__owner.position, self.__distance)
        for point in vision_border_points_list:
            vision_vector = coord.get_points_of_vector(self.__owner.position, point)
            objs_on_vector = self.__get_objs_on_view_vector(vision_vector)
            self.__entities_in_sight = self.__entities_in_sight.union(objs_on_vector)

    def __get_objs_on_view_vector(self, vector):
        seen_objs = set()
        for point in vector:
            cell = self.__owner.model.grid.get_cell_on(point.x, point.y)
            if cell:
                for obj in cell.items:
                    seen_objs.add(obj)
                    if isinstance(obj, self.__solid_obj_types):
                        return seen_objs
        return seen_objs


class Predator(Creature):
    def __init__(self):
        super().__init__('\033[31m█\033[0m')
        self.__hunger_hp = SimulationParams.predator_hunger_hp
        self.__eat_hp = SimulationParams.predator_eat_hp

    def eat(self):
        points_around = coord.get_points_list_of_borderline(self.position, 1)
        for point in points_around:
            cell = self.model.grid.get_cell_on(point.x, point.y)
            if cell:
                for obj in cell.items:
                    if isinstance(obj, Herbivore) and not obj.is_dead:
                        self.change_hp_by(self.__eat_hp)
                        obj.hit_by_bite(self.__eat_hp)
                        break

    def __choose_nearest_target(self):
        min_distance = self.model.grid.height + self.model.grid.width
        chosen_entity = None
        entities_set = self.entities_in_sight
        for entity in entities_set:
            if isinstance(entity, Herbivore) and not entity.is_dead:
                cur_dist = coord.calc_distance_to_point(self.position, entity.position)
                if cur_dist < min_distance:
                    min_distance = cur_dist
                    chosen_entity = entity
        return chosen_entity

    def move(self):
        if self._hp <= 0:
            return
        if chosen := self.__choose_nearest_target():
            self._move_to_target(chosen)
        else:
            self.make_random_move()

    def hit_by_hunger(self):
        self.change_hp_by(self.__hunger_hp * -1)


class Herbivore(Creature):
    def __init__(self):
        super().__init__('\033[34m█\033[0m')
        self.__hunger_hp = SimulationParams.herbivore_hunger_hp
        self.__grass_hp = SimulationParams.herbivore_eat_hp

    def eat(self):
        cell = self.model.grid.get_cell_on(self.position.x, self.position.y)
        for obj in cell.items:
            if isinstance(obj, Grass):
                cell.remove_item(obj)
                self.change_hp_by(self.__grass_hp)
                break

    def __choose_nearest_target(self):
        min_distance = self.model.grid.height + self.model.grid.width
        chosen_entity = None
        entities_set = self.entities_in_sight
        for entity in entities_set:
            if isinstance(entity, Grass):
                cur_dist = coord.calc_distance_to_point(self.position, entity.position)
                if cur_dist < min_distance:
                    min_distance = cur_dist
                    chosen_entity = entity
        return chosen_entity

    def move(self):
        if self._hp <= 0:
            return
        if chosen := self.__choose_nearest_target():
            self._move_to_target(chosen)
        else:
            self.make_random_move()

    def hit_by_hunger(self):
        self.change_hp_by(self.__hunger_hp * -1)

    def hit_by_bite(self, amount: int):
        self.change_hp_by(amount * -1)

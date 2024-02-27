from abc import ABCMeta, abstractmethod

import entities
from entities import Tree, Grass, Rock, Position, Entity
import random
import coord


class IMovable(metaclass=ABCMeta):
    @abstractmethod
    def _move_up(self):
        pass

    @abstractmethod
    def _move_down(self):
        pass

    @abstractmethod
    def _move_left(self):
        pass

    @abstractmethod
    def _move_right(self):
        pass

    @abstractmethod
    def _move_up_left(self):
        pass

    @abstractmethod
    def _move_up_right(self):
        pass

    @abstractmethod
    def _move_down_left(self):
        pass

    @abstractmethod
    def _move_down_right(self):
        pass


# class Vision:
#     def __init__(self, owner: Creature, distance=5):
#         self.__owner = owner
#         self.__model = owner.model
#         self.__distance = distance
#         self.__looking_for_obj_types = can_see_objs
#         self.__can_see_through_obj_types = (Grass,)
#         self.__entities_in_sight = []
#
#     @property
#     def entities_in_sight(self):
#         self.__look_around()
#         return self.__entities_in_sight
#
#     def __look_around(self):
#         self.__entities_in_sight.clear()
#         view_border_points = coord.get_points_list_of_borderline(self.__creature.get_position(), self.__distance)
#         for point in view_border_points:
#             entity = self.__look_by_vector(point)
#             if entity:
#                 self.__entities_in_sight.append(entity)
#
#     def __look_by_vector(self, to_point: Position):
#         vector_points = coord.get_points_of_vector(self.__creature.get_position(), to_point)
#         for point in vector_points:
#             entity = self.__creature.get_model().get_entity(point)
#             if isinstance(entity, self.__looking_for_obj_types) and entity not in self.__entities_in_sight:
#                 return self.__creature.get_model().get_entity(point)
#             elif not entity or isinstance(entity, self.__can_see_through_obj_types):
#                 continue
#             else:
#                 break
#         return None


class Creature(Entity, IMovable):
    def __init__(self, position=None, icon=None):
        super().__init__(position, icon)
        self._hp = 100
        self._model = None
        self.vision = Vision(self)

    @property
    def model(self):
        return self._model

    def set_model(self, to_model):
        self._model = to_model

    def get_model(self):
        return self._model

    def _move_up(self):
        if self._position.y > 0:
            self._position.y -= 1

    def _move_down(self):
        if self._position.y < self._model.height - 1:
            self._position.y += 1

    def _move_left(self):
        if self._position.x > 0:
            self._position.x -= 1

    def _move_right(self):
        if self._position.x < self._model.width - 1:
            self._position.x += 1

    def _move_up_right(self):
        self._move_up()
        self._move_right()

    def _move_up_left(self):
        self._move_up()
        self._move_left()

    def _move_down_right(self):
        self._move_down()
        self._move_right()

    def _move_down_left(self):
        self._move_down()
        self._move_left()

    def make_move(self, direction):
        # left top corner is x=0, y=0
        if direction == "up":
            self._move_up()
        elif direction == "down":
            self._move_down()
        elif direction == "left":
            self._move_left()
        elif direction == "right":
            self._move_right()
        elif direction == "up_right" or direction == "right_up":
            self._move_up_right()
        elif direction == "up_left" or direction == "up_left":
            self._move_up_left()
        elif direction == "down_right" or direction == "right_down":
            self._move_down_right()
        elif direction == "down_left" or direction == "left_down":
            self._move_down_left()

    def make_random_move(self):
        commands = ["up", "down", "left", "right", "up_right", "up_left", "down_right", "down_left"]
        x = random.randrange(0, len(commands))
        self.make_move(commands[x])

    def get_nearest_target(self, target: type):
        entities_in_sight = self.vision.entities_in_sight
        closest_target = None
        if entities_in_sight:
            distance = 10000
            for ent in entities_in_sight:
                if isinstance(ent, target):
                    cur_dist = coord.calc_distance_to_point(self.get_position(), ent.get_position())
                    if cur_dist < distance:
                        distance = cur_dist
                        closest_target = ent
        return closest_target

    def get_step_to_target(self, target: Entity):
        vector_points = coord.get_points_of_vector(self.get_position(), target.get_position())
        return vector_points[0]

    def make_move_to_nearest_target(self, target: type):
        closest_target = self.get_nearest_target(target)
        if closest_target:
            point_to_step = self.get_step_to_target(closest_target)
            if self._model.get_entity(point_to_step) is None:
                self.get_position().x = point_to_step.x
                self.get_position().y = point_to_step.y
        else:
            self.make_random_move()


class Vision:
    def __init__(self, owner: Creature, distance=5):
        self.__owner = owner
        self.__distance = distance
        self.__solid_obj_types = entities.Entity
        self.__entities_in_sight = set()

    @property
    def entities_in_sight(self):
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
            obj = self.__owner.model.get_entity(point)
            if obj:
                seen_objs.add(obj)
            if isinstance(obj, self.__solid_obj_types):
                return seen_objs
        return seen_objs


class Predator(Creature):
    def __init__(self, position=None):
        super().__init__(position, 'P')


class Herbivore(Creature):
    def __init__(self, position=None):
        super().__init__(position, 'H')

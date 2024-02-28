from abc import ABCMeta, abstractmethod
import entities
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


class Creature(entities.Entity, IMovable):
    def __init__(self, position=None, icon=None):
        super().__init__(position, icon)
        self._hp = 100
        self.__model = None
        self.vision = Vision(self)

    @property
    def model(self):
        return self.__model

    def set_model(self, to_model):
        self.__model = to_model

    @classmethod
    def is_creature(cls, obj):
        return isinstance(obj, Creature)

    def _move_up(self):
        if self.model:
            new_point = entities.Position(self.position.x, self.position.y - 1)
            self.model.change_entity_position(self, new_point)

    def _move_down(self):
        if self.model:
            new_point = entities.Position(self.position.x, self.position.y + 1)
            self.model.change_entity_position(self, new_point)

    def _move_left(self):
        if self.model:
            new_point = entities.Position(self.position.x - 1, self.position.y)
            self.model.change_entity_position(self, new_point)

    def _move_right(self):
        if self.model:
            new_point = entities.Position(self.position.x + 1, self.position.y)
            self.model.change_entity_position(self, new_point)

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
                    cur_dist = coord.calc_distance_to_point(self.position, ent.position)
                    if cur_dist < distance:
                        distance = cur_dist
                        closest_target = ent
        return closest_target

    def get_step_to_target(self, target: entities.Entity):
        vector_points = coord.get_points_of_vector(self.position, target.position)
        return vector_points[0]

    def make_move_to_nearest_target(self, target: type):
        closest_target = self.get_nearest_target(target)
        if closest_target:
            point_to_step = self.get_step_to_target(closest_target)
            self.model.update_entity_position(self, point_to_step)
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
        super().__init__(position, '*')

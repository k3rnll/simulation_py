from abc import ABCMeta, abstractmethod
import random

import creatures
import entities


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


class IVision:
    def __init__(self, creature, distance=5):
        self._creature = creature
        self._distance = distance
        self._entities_in_sight = []

    def get_entities_in_sight(self):
        return self._entities_in_sight

    def look_around(self):
        self._entities_in_sight.clear()
        view_border_points = self.__get_vision_circle_border_set()
        for point in view_border_points:
            entity = self.__look_by_vector(point)
            if entity:
                self._entities_in_sight.append(entity)

    def __get_vision_circle_border_set(self):
        points = []
        vision_distance = 5
        current_position = self._creature.get_position()
        for x in range(vision_distance * -1, vision_distance + 1):
            points.append(entities.Position(current_position.x + x, current_position.y + vision_distance * -1))
            points.append(entities.Position(current_position.x + x, current_position.y + vision_distance))
        for y in range(vision_distance * -1 + 1, vision_distance):
            points.append(entities.Position(current_position.x + vision_distance * -1, current_position.y + y))
            points.append(entities.Position(current_position.x + vision_distance, current_position.y + y))
        return points

    def __look_by_vector(self, point_to):
        now_look_point = entities.Position(0, 0)
        x1 = self._creature.get_position().x
        y1 = self._creature.get_position().y
        x2 = point_to.x
        y2 = point_to.y
        dist_x = abs(x2 - x1)
        dist_y = -abs(y2 - y1)
        shift_x = 1 if x1 < x2 else -1
        shift_y = 1 if y1 < y2 else -1
        error = dist_x + dist_y
        p_x = x1
        p_y = y1
        while p_x != x2 or p_y != y2:
            err_5 = error * 2
            if err_5 >= dist_y:
                error += dist_y
                p_x += shift_x
            if err_5 <= dist_x:
                error += dist_x
                p_y += shift_y
            now_look_point.x = p_x
            now_look_point.y = p_y
            entity = self._creature.get_model().get_entity(now_look_point)
            if isinstance(entity, creatures.Herbivore) and entity not in self._entities_in_sight:
                return self._creature.get_model().get_entity(now_look_point)
            elif not entity or isinstance(entity, entities.Grass):
                continue
            else:
                break
        return None


class Creature(entities.Entity, IMovable, IVision):
    @abstractmethod
    def __init__(self, position=None, icon=None):
        super().__init__(position, icon)
        self._hp = 100
        self._model = None
        self.vision = IVision(self)

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


class Predator(Creature):
    def __init__(self, position=None):
        super().__init__(position, 'P')


class Herbivore(Creature):
    def __init__(self, position=None):
        super().__init__(position, 'H')

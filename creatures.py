from abc import ABCMeta, abstractmethod
import random
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


class Creature(entities.Entity, IMovable):
    @abstractmethod
    def __init__(self, position=None, icon=None):
        super().__init__(position, icon)
        self._hp = 100
        self._model = None

    def set_model(self, to_model):
        self._model = to_model

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

    def get_vision_circle_border_set(self):
        points = []
        vision_distance = 3
        for x in range(vision_distance * -1, vision_distance + 1):
            points.append(entities.Position(self._position.x + x, self._position.y + vision_distance * -1))
            points.append(entities.Position(self._position.x + x, self._position.y + vision_distance))
        for y in range(vision_distance * -1 + 1, vision_distance):
            points.append(entities.Position(self._position.x + vision_distance * -1, self._position.y + y))
            points.append(entities.Position(self._position.x + vision_distance, self._position.y + y))
        return points

    def get_closest_entities_set(self):
        seen_entities = []
        vision_distance = 5
        seen_position = entities.Position(0, 0)
        for y in range(vision_distance * -1, vision_distance + 1):
            for x in range(vision_distance * -1, vision_distance + 1):
                if x != 0 or y != 0:
                    seen_position.x = self._position.x + x
                    seen_position.y = self._position.y + y
                    box = self._model.get_entity(seen_position)
                    if box:
                        seen_entities.append(box)
        return seen_entities


class Predator(Creature):
    def __init__(self, position=None):
        super().__init__(position, 'P')


class Herbivore(Creature):
    def __init__(self, position=None):
        super().__init__(position, 'H')

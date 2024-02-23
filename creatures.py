import random

import entities
import map


class Creature(entities.Entity):
    def __init__(self, position, field):
        super().__init__(position)
        self.hp = 100
        self.field = field

    def _move_up(self):
        if self.position.y > 0:
            self.position.y -= 1

    def _move_down(self):
        if self.position.y < self.field.height - 1:
            self.position.y += 1

    def _move_left(self):
        if self.position.x > 0:
            self.position.x -= 1

    def _move_right(self):
        if self.position.x < self.field.width - 1:
            self.position.x += 1

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
    def __init__(self, position, field):
        super().__init__(position, field)
        self.icon = 'P'

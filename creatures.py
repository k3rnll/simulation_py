import random
import entities


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

    def get_vision_circle_border_set(self):
        points = []
        vision_distance = 3
        for x in range(vision_distance * -1, vision_distance + 1):
            points.append(entities.Position(self.position.x + x, self.position.y + vision_distance * -1))
            points.append(entities.Position(self.position.x + x, self.position.y + vision_distance))
        for y in range(vision_distance * -1 + 1, vision_distance):
            points.append(entities.Position(self.position.x + vision_distance * -1, self.position.y + y))
            points.append(entities.Position(self.position.x + vision_distance, self.position.y + y))
        return points

    def get_closest_entities_set(self):
        seen_entities = []
        vision_distance = 5
        seen_position = entities.Position(0, 0)
        for y in range(vision_distance * -1, vision_distance + 1):
            for x in range(vision_distance * -1, vision_distance + 1):
                if x != 0 or y != 0:
                    seen_position.x = self.position.x + x
                    seen_position.y = self.position.y + y
                    box = self.field.get_entity(seen_position)
                    if box:
                        seen_entities.append(box)
        return seen_entities


class Predator(Creature):
    def __init__(self, position, field):
        super().__init__(position, field)
        self.icon = 'P'


class Herbivore(Creature):
    def __init__(self, position, field):
        super().__init__(position, field)
        self.icon = 'H'

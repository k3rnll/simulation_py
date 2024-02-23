class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Entity:
    def __init__(self, position):
        self.position = position


class Rock(Entity):
    def __init__(self, position):
        super().__init__(position)
        self.icon = '^'


class Grass(Entity):
    def __init__(self, position):
        super().__init__(position)
        self.icon = '#'


class Tree(Entity):
    def __init__(self, position):
        super().__init__(position)
        self.icon = 'T'

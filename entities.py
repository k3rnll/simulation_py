from abc import ABCMeta, abstractmethod


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, position=None, icon=None):
        self._position = position
        self._icon = icon

    def set_position(self, position: Position):
        self._position = position

    def get_position(self):
        return self._position

    def get_icon(self):
        return self._icon


class Rock(Entity):
    def __init__(self, position=None):
        super().__init__(position, icon='^')


class Grass(Entity):
    def __init__(self, position=None):
        super().__init__(position, icon='#')


class Tree(Entity):
    def __init__(self, position=None):
        super().__init__(position, icon='T')

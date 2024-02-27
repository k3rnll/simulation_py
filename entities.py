from abc import ABCMeta, abstractmethod


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, position=None, icon=None):
        if isinstance(position, Position):
            self.__position = position
        else:
            self.__position = Position()
        self.__icon = icon

    @property
    def position(self):
        return self.__position

    @property
    def icon(self):
        return self.__icon


class Rock(Entity):
    def __init__(self, position=None):
        super().__init__(position, icon='^')


class Grass(Entity):
    def __init__(self, position=None):
        super().__init__(position, icon='▓')


class Tree(Entity):
    def __init__(self, position=None):
        super().__init__(position, icon='█')

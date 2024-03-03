from abc import ABCMeta, abstractmethod


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, position: Position = Position(), icon: str = ' '):
        self.__position = position
        self._icon = icon

    @property
    def position(self) -> Position:
        return self.__position

    @property
    def icon(self) -> str:
        return self._icon


class Rock(Entity):
    def __init__(self, position=None):
        super().__init__(position, icon='\033[94m▄\033[0m')


class Grass(Entity):
    def __init__(self, position=None):
        super().__init__(position, icon='░')


class Tree(Entity):
    def __init__(self, position=None):
        super().__init__(position, icon='\033[33m¶\033[0m')

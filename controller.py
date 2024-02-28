import creatures
import model
import view


class Controller:
    def __init__(self, predators=0, herbivores=0, trees=0, rocks=0):
        self.__model = model.Model(30, 60)
        self.__view = view.View(self.__model, self, False)
        self.__predators = predators
        self.__herbivores = herbivores
        self.__trees = trees
        self.__rocks = rocks
        self.__put_entities_on_map()
        self.__view.print_frame()

    def __put_entities_on_map(self):
        for i in range(self.__predators):
            self.__model.add_entity_randomly(creatures.Predator())
        # for i in range(self._herbivores):
        #     self._model.add_entity_randomly(creatures.Herbivore())
        # for i in range(self._trees):
        #     self._model.add_entity_randomly(entities.Tree())
        # for i in range(self._rocks):
        #     self._model.add_entity_randomly(entities.Rock())

    def spin_the_world(self):
        self.__model.move_all_creatures()
        self.__view.print_frame()

import creatures
import entities
import model
import view


class Controller:
    def __init__(self, predators=0, herbivores=0, trees=0, rocks=0):
        self._model = model.Model(30, 60)
        self._view = view.View(self._model, self, False)
        self._predators = predators
        self._herbivores = herbivores
        self._trees = trees
        self._rocks = rocks
        self._put_entities_on_map()

    def _put_entities_on_map(self):
        for i in range(self._predators):
            self._model.add_entity_randomly(creatures.Predator())
        for i in range(self._herbivores):
            self._model.add_entity_randomly(creatures.Herbivore())
        for i in range(self._trees):
            self._model.add_entity_randomly(entities.Tree())
        for i in range(self._rocks):
            self._model.add_entity_randomly(entities.Rock())

    def spin_the_world(self):
        for entity in self._model.entities_on_grid.values():
            if isinstance(entity, creatures.Predator):
                entity.make_move_to_nearest_target(creatures.Herbivore)
            if isinstance(entity, creatures.Herbivore):
                entity.make_random_move()
        self._view.print_frame()

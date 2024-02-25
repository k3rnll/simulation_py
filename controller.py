import creatures
import model
import view


class Controller:
    # View, Map, creature.Predator, herbivores, rocks, trees, grass
    def __init__(self, predators=0, herbivores=0):
        self._model = model.Model(30, 50)
        self._view = view.View(self._model, self)
        self._predators = predators
        self._herbivores = herbivores
        self._put_entities_on_map()

    def _put_entities_on_map(self):
        for i in range(self._predators):
            self._model.add_entity(creatures.Predator(), True)

    def spin_the_world(self):
        for entity in self._model.entities.values():
            if issubclass(entity.__class__, creatures.Creature):
                entity.make_random_move()
        self._view.print_frame()

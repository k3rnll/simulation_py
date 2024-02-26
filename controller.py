import creatures
import entities
import model
import view


class Controller:
    def __init__(self, predators=0, herbivores=0):
        self._model = model.Model(15, 30)
        self._view = view.View(self._model, self)
        self._predators = predators
        self._herbivores = herbivores
        self.bob = creatures.Predator()
        self.bob._icon = "B"
        self._put_entities_on_map()

    def _put_entities_on_map(self):
        self._model.add_entity_manually(self.bob, entities.Position(5, 4))
        self._model.add_entity_manually(creatures.Predator(), entities.Position(8, 5))
        self._model.add_entity_manually(creatures.Predator(), entities.Position(8, 4))
        self._model.add_entity_manually(creatures.Predator(), entities.Position(8, 6))
        self._model.add_entity_manually(creatures.Herbivore(), entities.Position(10, 7))
        self._model.add_entity_manually(creatures.Herbivore(), entities.Position(10, 6))
        self._model.add_entity_manually(creatures.Herbivore(), entities.Position(10, 5))

        self._model.add_entity_manually(entities.Tree(), entities.Position(10, 10))
        self._model.add_entity_manually(entities.Tree(), entities.Position(10, 11))
        self._model.add_entity_manually(entities.Tree(), entities.Position(10, 12))

        for i in range(self._predators):
            self._model.add_entity_randomly(creatures.Predator())

    def spin_the_world(self):
        # pass
        # for entity in self._model.entities.values():
        #     if issubclass(entity.__class__, creatures.Creature):
        #         entity.make_random_move()
        self._view.print_frame()
        print(f"bob see: {len(self.bob.vision.entities_in_sight)} objects")
        self.bob.make_move("down")


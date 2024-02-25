import creatures
import entities


class Simulation:
    # View, Map, creature.Predator, herbivores, rocks, trees, grass
    def __init__(self, display, field, predators=0, herbivores=0):
        self._display = display
        self.field = field
        self._predators = predators
        self._herbivores = herbivores
        self._put_entities_on_map()

    def _put_entities_on_map(self):
        for i in range(self._predators):
            self.field.add_entity(creatures.Predator(entities.Position(0, 0), self.field), True)
        for i in range(self._herbivores):
            self.field.add_entity(creatures.Herbivore(entities.Position(0, 0), self.field), True)

    def spin_the_world(self):
        #for entity in self.field.entities.values():
            #if issubclass(entity.__class__, creatures.Creature):
                # entity.make_random_move()
        self._display.print_frame()

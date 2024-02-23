import creatures
import entities


class Simulation:
    # map, predators, herbivores, rocks, trees, grass
    def __init__(self, field, predators=1):
        self.field = field
        self.predators = predators
        self._put_predators()

    def _put_predators(self):
        for i in range(self.predators):
            self.field.add_entity(creatures.Predator(entities.Position(0, 0), self.field), True)

    def spin_the_world(self):
        for entity in self.field.entities.values():
            if issubclass(entity.__class__, creatures.Creature):
                # print(entity)
                entity.make_random_move()

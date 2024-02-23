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

    def convey_neigh(self, x, y):
        count = 0
        if self.field.get_entity(entities.Position(x - 1, y - 1)):
            count += 1
        if self.field.get_entity(entities.Position(x - 1, y)):
            count += 1
        if self.field.get_entity(entities.Position(x - 1, y + 1)):
            count += 1
        if self.field.get_entity(entities.Position(x + 1, y - 1)):
            count += 1
        if self.field.get_entity(entities.Position(x + 1, y)):
            count += 1
        if self.field.get_entity(entities.Position(x + 1, y + 1)):
            count += 1
        if self.field.get_entity(entities.Position(x, y - 1)):
            count += 1
        if self.field.get_entity(entities.Position(x, y + 1)):
            count += 1
        return count

    def convey(self):
        to_add = []
        to_del = []
        for y in range(self.field.height):
            for x in range(self.field.width):
                n = self.convey_neigh(x, y)
                if not self.field.get_entity(entities.Position(x, y)) and n == 3:
                    to_add.append(entities.Position(x, y))
                    #self.field.add_entity(creatures.Predator(entities.Position(x, y), self.field))
                #n = self.convey_neigh(x, y)
                elif self.field.get_entity(entities.Position(x, y)) and (n > 3 or n < 2):
                    to_del.append(entities.Position(x, y))
                    #self.field.delete_entity(entities.Position(x, y))
        for p in to_add:
            self.field.add_entity(creatures.Predator(p, self.field))
        for p in to_del:
            self.field.delete_entity(p)

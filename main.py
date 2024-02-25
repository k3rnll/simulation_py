import time

import creatures
import entities
import map
import renders
import simulation


def main():
    map1 = map.Map(30, 30)
    display = renders.View(map1, is_debug=True)
    my_simulation = simulation.Simulation(display, map1, 0, 0)
    predator1 = creatures.Predator(entities.Position(11, 5), map1)
    predator2 = creatures.Predator(entities.Position(6, 5), map1)
    predator3 = creatures.Predator(entities.Position(1, 5), map1)
    map1.add_entity(predator1)
    map1.add_entity(predator2)
    map1.add_entity(predator3)
    while 1:
        my_simulation.spin_the_world()
        print("hello")
        print(predator2.get_vision_circle_border_set())
        time.sleep(0.5)


if __name__ == "__main__":
    main()

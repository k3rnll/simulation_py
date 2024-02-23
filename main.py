import map
import entities
import creatures
import renders
import time

import simulation


def main():
    map1 = map.Map(20, 40)
    my_simulation = simulation.Simulation(map1, 200)
#    print(f"x: {predator1.position.x}, y: {predator1.position.y}")
#    predator1.make_move("down")
#    print(f"x: {predator1.position.x}, y: {predator1.position.y}")
#    print(map1.entities.items())
    #map1.add_entity(creatures.Predator(entities.Position(4,5), map1))
    #map1.add_entity(creatures.Predator(entities.Position(5,7), map1))
    #map1.add_entity(creatures.Predator(entities.Position(6,6), map1))
    renders.render_map(map1)
    #my_simulation.convey()
    #time.sleep(1)
    #renders.render_map(map1)
    while 1:
        # my_simulation.spin_the_world()
        my_simulation.convey()
        renders.render_map(map1)
        time.sleep(0.05)


if __name__ == "__main__":
    main()

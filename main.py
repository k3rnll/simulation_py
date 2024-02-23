import map
import entities
import creatures
import renders
import time

import simulation


def main():
    map1 = map.Map(12, 24)
    my_simulation = simulation.Simulation(map1, 30)
#    print(f"x: {predator1.position.x}, y: {predator1.position.y}")
#    predator1.make_move("down")
#    print(f"x: {predator1.position.x}, y: {predator1.position.y}")
#    print(map1.entities.items())
    renders.render_map(map1)
    while 1:
        my_simulation.spin_the_world()
        renders.render_map(map1)
        time.sleep(0.1)


if __name__ == "__main__":
    main()

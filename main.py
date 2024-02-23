import time
import map
import renders
import simulation


def main():
    map1 = map.Map(32, 64)
    my_simulation = simulation.Simulation(map1, 250)
    renders.render_map(map1)
    while 1:
        my_simulation.spin_the_world()
        renders.render_map(map1)
        time.sleep(0.01)


if __name__ == "__main__":
    main()

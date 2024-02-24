import time
import map
import renders
import simulation


def main():
    map1 = map.Map(32, 64)
    display = renders.View(map1, is_debug=True)
    my_simulation = simulation.Simulation(display, map1, 5)
    while 1:
        my_simulation.spin_the_world()
        time.sleep(0.05)


if __name__ == "__main__":
    main()

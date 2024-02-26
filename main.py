import time
import controller


def main():
    simulation = controller.Controller()
    while 1:
        simulation.spin_the_world()
        time.sleep(1)


if __name__ == "__main__":
    main()

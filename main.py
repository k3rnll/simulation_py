import time
import controller


def main():
    simulation = controller.Controller(50, 100, 60, 5)
    while 1:
        simulation.spin_the_world()
        # time.sleep(0.1)


if __name__ == "__main__":
    main()

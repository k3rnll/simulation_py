import time
from params import SimulationParams
from controller import Controller


def main():
    time_between_frames_ns = 1000000000 / SimulationParams.fps_max
    last_call_time = 0
    simulation = Controller()
    while True:
        current_time = time.time_ns()
        if current_time - last_call_time > time_between_frames_ns:
            last_call_time = current_time
            simulation.spin_the_world()


if __name__ == "__main__":
    main()

import time
from params import SimulationParams
from model import Model


def _get_clear_display_str():
    return "\033[H\033[J"


class View:
    def __init__(self, data_model: Model, controller):
        self.__model = data_model
        self._controller = controller
        self.__is_show_fps = SimulationParams.is_show_fps
        self.__empty_cell_icon = ' '
        self.__last_call_time = 0

    def __fps_info(self):
        cur_time = time.time_ns()
        fps_str = f"fps:\t{str(1000000000 // (cur_time - self.__last_call_time))}"
        self.__last_call_time = cur_time
        return fps_str

    def __grid_render(self) -> str:
        frame = str()
        x = 1
        for cell in self.__model.grid.cells:
            if cell.items:
                frame += cell.items[-1].icon
            else:
                frame += self.__empty_cell_icon
            if x % self.__model.grid.width == 0:
                frame += '\n'
            x += 1
        return frame

    def __make_frame(self):
        if self.__is_show_fps:
            return self.__grid_render() + self.__fps_info()
        return self.__grid_render()

    def print_frame(self):
        print(_get_clear_display_str(), self.__make_frame(), sep='')

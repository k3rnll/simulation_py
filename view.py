import creatures
import model
import time


def _get_clear_display_str():
    return "\033[H\033[J"


class View:
    def __init__(self, data_model: model.Model, controller, is_debug=False, is_fps=True):
        self.__model = data_model
        self._controller = controller
        self._is_debug = is_debug
        self.__is_fps = is_fps
        self.__empty_cell_icon = '_'
        self.__last_call_time = 0

    def __fps_info(self) -> str:
        cur_time = time.time_ns()
        fps_str = f"fps:\t{str(1000000000 // (cur_time - self.__last_call_time))}"
        self.__last_call_time = cur_time
        return fps_str

    def __debug_info(self) -> str:
        entities_list = self.__model.entities_on_grid
        info_string = (f"\nentities:\t{len(entities_list())}\n"
                       f"predators:\t{len(self.__model.entities_on_grid(creatures.Predator))}\n"
                       f"herbivores:\t{len(self.__model.entities_on_grid(creatures.Herbivore))}")
        return info_string

    def __grid_render(self) -> str:
        frame = str()
        x = 1
        for cell in self.__model.grid.cells:
            if len(cell.items):
                frame += str(len(cell.items))
            else:
                frame += self.__empty_cell_icon
            if x % self.__model.grid.width == 0:
                frame += '\n'
            x += 1
        return frame

    def __make_frame(self):
        frame = self.__grid_render()
        if self.__is_fps:
            frame += self.__fps_info()
        return frame

    def print_frame(self):
        print(_get_clear_display_str(), self.__make_frame(), sep='')

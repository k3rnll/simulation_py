import creatures
import model
import time


def _get_clear_display_str():
    return "\033[H\033[J"


class View:
    def __init__(self, data_model: model.Model, controller, is_debug=False, is_fps=True):
        self._model = data_model
        self._controller = controller
        self._is_debug = is_debug
        self.__is_fps = is_fps
        self._empty_box_icon = ' '
        self.__last_call_time = 0

    def __fps_info(self) -> str:
        cur_time = time.time_ns()
        fps_str = str(1000000000 // (cur_time - self.__last_call_time))
        self.__last_call_time = cur_time
        return fps_str

    def __debug_info(self) -> str:
        entities_list = self._model.entities_on_grid
        info_string = (f"\nentities:\t{len(entities_list())}\n"
                       f"predators:\t{len(self._model.entities_on_grid(creatures.Predator))}\n"
                       f"herbivores:\t{len(self._model.entities_on_grid(creatures.Herbivore))}")
        return info_string

    def _render_map(self):
        frame = str()
        for y in range(self._model.height):
            for x in range(self._model.width):
                frame += " "
            frame += '\n'
        if self.__is_fps:
            frame += self.__fps_info() + '\n'
        if self._is_debug:
            frame += self.__debug_info()
        frame_list = list(frame)
        for ent in self._model.entities_dict.values():
            index = int(self._model.width * ent.position.y + ent.position.x + ent.position.y)
            frame_list[index] = ent.icon
        frame = ''.join(frame_list)
        return frame

    def print_frame(self):
        print(_get_clear_display_str(), self._render_map(), sep='')

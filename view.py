import creatures
import entities
import model


def _get_clear_display_str():
    return "\033[H\033[J"


class View:
    def __init__(self, data_model: model.Model, controller, is_debug=True):
        self._model = data_model
        self._controller = controller
        self._is_debug = is_debug
        self._empty_box_icon = ' '

    def __debug_info(self) -> str:
        entities_list = self._model.entities_on_grid
        info_string = (f"\nentities:\t{len(entities_list())}\n"
                       f"predators:\t{len(self._model.entities_on_grid(creatures.Predator))}\n"
                       f"herbivores:\t{len(self._model.entities_on_grid(creatures.Herbivore))}")
        return info_string

    def _render_map(self):
        frame = ""
        position = entities.Position(0, 0)
        for y in range(self._model.height):
            for x in range(self._model.width):
                position.x = x
                position.y = y
                entity = self._model.get_entity(position)
                if entity is None:
                    frame += self._empty_box_icon
                else:
                    frame += entity.icon
            frame += '\n'
        if self._is_debug:
            frame += self.__debug_info()
        return frame

    def print_frame(self):
        print(_get_clear_display_str(), self._render_map(), sep='')

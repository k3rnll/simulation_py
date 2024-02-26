import entities
import model


def _get_clear_display_str():
    return "\033[H\033[J"


class View:
    def __init__(self, data_model: model.Model, controller, is_debug=True):
        self._model = data_model
        self._controller = controller
        self._is_debug = is_debug
        self._empty_box_icon = '_'

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
                    frame += entity.get_icon()
            frame += '\n'
        if self._is_debug:
            frame += f"\nentities: {len(self._model.entities_on_grid.items())}"
        return frame

    def print_frame(self):
        print(_get_clear_display_str(), self._render_map(), sep='')

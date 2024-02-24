import entities


def _get_clear_display_str():
    return "\033[H\033[J"


class View:
    def __init__(self, field, is_debug=False):
        self._field = field
        self._is_debug = is_debug
        self._empty_box_icon = ' '

    def _render_map(self):
        frame = ""
        position = entities.Position(0, 0)
        for y in range(self._field.height):
            for x in range(self._field.width):
                position.x = x
                position.y = y
                entity = self._field.get_entity(position)
                if entity is None:
                    frame += self._empty_box_icon
                else:
                    frame += entity.icon
            frame += '\n'
        if self._is_debug:
            frame += f"\nentities: {len(self._field.entities.items())}"
        return frame

    def print_frame(self):
        print(_get_clear_display_str(), self._render_map())

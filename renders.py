import entities
import map


def clear_display():
    print("\033[H\033[J", end="")


def render_map(field):
    clear_display()
    frame = ""
    for y in range(field.height):
        for x in range(field.width):
            entity = field.get_entity(entities.Position(x, y))
            # print(entity)
            if entity is None:
                frame += '_'
            else:
                frame += entity.icon
        frame += '\n'
    print(frame)

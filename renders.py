import entities


def clear_display():
    print("\033[H\033[J", end="")


def render_map(field):
    clear_display()
    frame = ""
    position = entities.Position(0, 0)
    for y in range(field.height):
        for x in range(field.width):
            position.x = x
            position.y = y
            entity = field.get_entity(position)
            if entity is None:
                frame += '_'
            else:
                frame += entity.icon
        frame += '\n'
    print(frame)

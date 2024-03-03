import entities


def get_points_list_of_borderline(center_point: entities.Position, distance: int):
    if distance <= 0:
        return []
    x_from = center_point.x
    y_from = center_point.y
    border_points = []
    for x in range(distance * -1, distance + 1):
        border_points.append(entities.Position(x_from + x, y_from + distance * -1))
        border_points.append(entities.Position(x_from + x, y_from + distance))
    for y in range(distance * -1 + 1, distance):
        border_points.append(entities.Position(x_from + distance * -1, y_from + y))
        border_points.append(entities.Position(x_from + distance, y_from + y))
    return border_points


def get_points_of_vector(from_point: entities.Position, to_point: entities.Position):
    vector_points_list = []
    x1 = from_point.x
    y1 = from_point.y
    x2 = to_point.x
    y2 = to_point.y
    if x1 == x2 and y1 == y2:
        return [to_point]
    dist_x = abs(x2 - x1)
    dist_y = -abs(y2 - y1)
    shift_x = 1 if x1 < x2 else -1
    shift_y = 1 if y1 < y2 else -1
    error = dist_x + dist_y
    p_x = x1
    p_y = y1
    while p_x != x2 or p_y != y2:
        err_5 = error * 2
        if err_5 >= dist_y:
            error += dist_y
            p_x += shift_x
        if err_5 <= dist_x:
            error += dist_x
            p_y += shift_y
        vector_points_list.append(entities.Position(p_x, p_y))
    return vector_points_list


def calc_distance_to_point(from_point: entities.Position, to_point: entities.Position):
    x = abs(from_point.x - to_point.x)
    y = abs(from_point.y - to_point.y)
    return (x * x + y * y) ** 0.5

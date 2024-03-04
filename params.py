class SimulationParams:
    # map size
    map_width = 100
    map_height = 50

    # entities amount
    predators_amount = 30
    herbivores_amount = 60
    trees_amount = 60
    rocks_amount = 30
    grass_amount = 500

    # grass addition on each frame
    grass_addition = 50

    # render settings
    fps_max = 10
    is_show_fps = True

    # creatures eat and hunger hp
    herbivore_eat_hp = 5
    herbivore_hunger_hp = 1
    predator_eat_hp = 5
    predator_hunger_hp = 1

    # creatures vision params
    # its most cpu usage
    creatures_default_vision_distance = 5
    herbivore_vision_distance = 6
    predator_vision_distance = 12

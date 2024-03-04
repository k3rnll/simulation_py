from params import SimulationParams
from model import Model
from creatures import Predator, Herbivore
from entities import Tree, Rock, Grass
from view import View


class Controller:
    def __init__(self):
        self.__model = Model(SimulationParams.map_width, SimulationParams.map_height)
        self.__view = View(self.__model, self)
        self.__init_entities_on_map()
        self.__view.print_frame()

    def __add_grass(self, amount: int):
        for i in range(amount):
            self.__model.add_entity_randomly(Grass())

    def __init_entities_on_map(self):
        for i in range(SimulationParams.predators_amount):
            self.__model.add_entity_randomly(Predator())
        for i in range(SimulationParams.herbivores_amount):
            self.__model.add_entity_randomly(Herbivore())
        for i in range(SimulationParams.trees_amount):
            self.__model.add_entity_randomly(Tree())
        for i in range(SimulationParams.rocks_amount):
            self.__model.add_entity_randomly(Rock())
        self.__add_grass(SimulationParams.grass_amount)

    def spin_the_world(self):
        self.__add_grass(SimulationParams.grass_addition)
        self.__model.creatures_handler.ask_all_to_eat()
        self.__model.creatures_handler.move_all_creatures()
        self.__model.creatures_handler.hit_creatures_by_hunger()
        self.__view.print_frame()
        if not self.__model.creatures_handler.alive_creatures_amount:
            exit()


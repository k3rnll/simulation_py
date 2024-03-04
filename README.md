### Simulation of the wild world
### Goal:
- predators hunt for herbivores<br>
- herbivores eat grass
![](https://github.com/k3rnll/simulation_py/blob/main/doc/view.gif)
### Project structure:
- MVC
- model is a central part, has grid data structure and handles to manipulate it
- creatures are data objects that use model to understand their position and make decisions
- controller adds entities to model and asks creatures to move
- view gets data from model, search grid cells for object, makes frame, prints

### Now implemented:
- creatures have vector vision, looking for target
- vision can't see after solid objects
- creatures choose nearest target
- creatures move to target by vector
- creatures move randomly when don't see target
- predators can bite nearest herbivore
- predators rise their hp from subtract hp from herbivore
- herbivores can eat grass if they stay on it (rise hp)
- every frame creatures receive damage from hunger
- creatures have 100hp and die if 0hp

### Run:
- settings are in params.py
- python main.py

### TODO:
- read parameters from file
- change grass addition from static amount to percent of grid size
- ? read whole grid from file

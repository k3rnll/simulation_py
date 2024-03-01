### Simulation of the wild world
### Goal:
- predators hunt for herbivores<br>
- herbivores eat grass


### Project structure:
- MVC
- model is a central part, has grid data structure and handles to manipulate it
- creatures is data objects that use model to understand their position and make decisions
- controller adds entities to model and asks creatures to move
- view gets data from model, search grid cells for object, makes frame, prints

### Now implemented:
- herbivores move randomly
- predators have vector vision, looking for herbivores
- vision can't see after solid objects
- predators choose nearest target
- predators move to target by vector

### Run:
- python main.py
- runs without time pause, hits 30fps
- for slow cpus add time pause in cycle in main.py

### TODO:
- read parameters from file
- hunger for creatures
- death logic
- creatures bite nearest targets
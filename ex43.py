#ex43, Basic Object-Oriented Analysis nad Design
# Process for when you want to build something using python, specifically with object-oriented programming:
# 1. Write or draws about the problem.
# 2. Extract key concepts from 1 and research them.
# 3. Create class hierarchy and object map for the concepts.
# 4. Code the classes and a test to run them.
# 5. Repeat and refine.

#Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an
#escape pod to the planet below.  The game will be more like a Zork or Adventure type game with text outputs and funny
#ways to die.  The game will involve an engine that runs a map full of rooms or scenes.  Each room will print its own
#description when the palyer enters it and then tell the engine what room to run next out of the map.

#Therefore, I want to describe each scene:

# Death: This is when the player dies and should be something funny
# Central Corridor: This is the starting point and has a Gothon already standing there that the players have to defeat with a joke before continuing
# Laser Weapon Armory: This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod.  It has a keypad the hero has to guess the number for
# The Bridge : This is another battle scene with a Gothon where the hero places the bomb.
# Escape Pod : This is where the hero escapes but only after guessing the right escape pod.

#At this point maybe draw out a map of these/more descriptions
#EXTRACT KEY CONCEPTS AND RESEARCH THEM (make a list of all the nouns, establish a hierarchy)
#CREATE A CLASS HIERARCHY AND OBJECT MAP FOR THE CONCEPTS
#After all of that thought process I start to make a class hierarchy that looks like this:
# *Map
# *Engine
# *Scene
#   *Death
#   *Central Corridor
#   *Laser Weapon Armory
#   *The Bridge
#   *Escape Pod
#Then I go through and figure our what actions are needed on each thing based on verbs in the description.
#For example, I know from the description I'm going to need a way to "run the engine", "get the next scene" fromthe map, get the "opening scene" and "enter" a scene.
#I'll add those liek this:

# *Map
#   - next_scene
#   - opening_scene
# *Engine
#   - play
# Scene
#   - enter
#   *Death
#   *Central Corridor
#   *Laser Weapon Armory
#   *The Bridge
#   *Escape Pod
#Notice how just putting - enter under Scene since all the scenes under it will inherit it and have to override it later

#Code the Classes and Test to Run Them

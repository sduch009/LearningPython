class Scene(object):
# makes a class called scene that is-a object.  class scene has-a function that takes self param
    def enter(self):
        pass


class Engine(object):
    #makes a class called engine (that is-a object) that has-a __init__that takes self and scene_map params
    def __init__(self, scene_map):
        pass
        #the class called engine also has-a function that takes self param.
    def play(self):
        pass

class Death(Scene):
    #makes class death that is-a Scene.  class death contains function enter that taks self param
    def enter(self):
        pass

class CentralCorridor(Scene):
    #makes class CentralCorridor that is-a scene that has-a function called enter that taks self param
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    #makes class LaserWeaponArmory (that is-a scene) that has-a function enter that takes self param.
    def enter(self):
        pass

class TheBridge(Scene):
    #makes class TheBridge that is-a scene that has-a function enter that takes self param.
    def enter(self):
        pass

class EscapePod(Scene):
    #makes class EscapePod (that is-a Scene) which has=a function enter that takes self param
    def enter(self):
        pass

#makes a_map an instance of class map when ran with central corridor?
a_map = Map('central_corridor')
#make a_game an instance of class Engine ran with a_map?
a_game = Engine(a_map)
#from a_game get play()
a_game.play()

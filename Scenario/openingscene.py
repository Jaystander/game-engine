import scene
import Objects

#name each object reference as name = module.class
orc1 = orc.orc

class OpeningScene(scene.scene):
    master_list = [orc1]
    objects = []
    object_descriptions = []
    places = []
    place_descriptions = []
    npcs = []
    npc_descriptions = []
    description = 'I am testing the Scene description.'

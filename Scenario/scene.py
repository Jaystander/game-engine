import Objects

scene_change = None

class Scene():
    
    reference = ''
    master_list = []
    objects = []
    object_descriptions = []
    places = []
    place_descriptions = []
    npcs = []
    npc_descriptions = []
    description = 'This string describes the scene'
    current_object = None
    
    
    def PopLists(self):
        for item in self.master_list:
            if item.type == 'object':
                self.objects.append(item)
            elif item.type == 'place':
                self.places.append(item)
            elif item.type == 'npc':
                self.npcs.append(item)
            else:
                print('Invalid Object Type' + item.description)
                
    def PopItemDesc(self):
        for item in self.objects:
            object_descriptions.append(item.description)
        for item in self.places:
            place_descriptions.append(item.description)
        for item in self.npcs:
            npc_descriptions.append(item.description)
    
    def Respond(choice):
        current_object.Respond(choice) # pass the reff used for the response action.

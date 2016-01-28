import main

class Object():
    description = 'This is an empty object'
    can_talk = False
    can_look = False
    can_grab = False
    can_touch = False
    can_use = False
    can_go = False
    type = 'object' # npc and place are also possible.
    
    def Talk(self): # if the actions are possible define what they do.
        pass
        
    def Use(self):
        pass
        
    def Grab(self):
        pass
        
    def Touch(self):
        pass
        
    def Look(self):
        pass
    
    def Go(self):
        pass

class NPC():
    
    description = 'This is an empty object'
    can_talk = False
    can_fight = False
    can_party = False
    can_trade = False
    type = 'npc' # npc and place are also possible.
    
    def Talk(self): # if the actions are possible define what they do.
        pass
        
    def Use(self):
        pass
        
    def Grab(self):
        pass
        
    def Touch(self):
        pass
        
    def Look(self):
        pass
    

    
class Item(): #base class for usable/collectable items/equipment
    
    description = 'This is an item'
    equipable = False
    usable = False
    quantity = False
    consumable = False
    can_sell = False
    value = 0
    
    type = 'item' # npc and place are also possible.
    
    def Use(self): # if the actions are possible define what they do.
        pass
        
    def Equip(self):
        pass
        
    def Sell(self):
        pass
        
    def Touch(self):
        pass
        
    def Look(self):
        pass
    

    
class Transition():
    
    description = 'This is an empty object'
    visible = True
    locked = False
    open = False
    can_go = False
    type = 'transition'
    
    def Go(self): # if the actions are possible define what they do.
        pass
        
    def Unlock(self):
        pass
        
    def Lock(self):
        pass
        
    def Reveal(self):
        pass
        
    def Look(self):
        pass
    
    def Go(self):
        pass

class Responses():
    
    response_dictionary = [ 'reff': functioncall(),
                            'reff2': functioncall2(),
    ]
    
    def ReffCall(reff):
        response_dictionary[reff]()
    
    def activate

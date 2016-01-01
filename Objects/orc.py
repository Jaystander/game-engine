import base
import main
import Draw

class Orc(base.NPC):
  can_talk = True
  can_fight = True
  can_trade = True
  
  def Talk(self):
    pass #need a drawing fuction to handle the text boxes.
    

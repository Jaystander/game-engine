import main, Draw, base

class RobotLeader(base.NPC):
  
  met_pc = False
  opinion_pc = False
  pc_gave_treasure = False
  description = ''
  can_talk = True
  can_fight = True
  can_look = True
  can_party = False
  can_trade = False
  
  def Talk():
    if main.scenes[1].reference == "Robot Leader's Office"  
      if met_pc == False: # hasn;t met the pc yet
        pass
      elif met_pc == True and opinion_pc >= 50: #has met and likes the pc
        pass
      elif met_pc == True and opinion_pc >=0: # has met and is impartial to the pc
        pass
      else: # has met and dislikes the pc
        pass
    elif main.scenes[1].reference == "Other place you can meet him":
      pass
      if met_pc == False: # hasn't met the pc yet
        pass
      #et cetera

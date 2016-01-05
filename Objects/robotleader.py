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
      if met_pc == False:
        pass
      elif met_pc == True and opinion_pc >= 50:
        pass
      elif met_pc == True and opinion_pc >=0:
        pass
      else:
        pass
    elif main.scenes[1].reference == "Other place you can meet him"
      pass

import main, Draw, base

class RobotLeader(base.NPC):
filed = 'text.robotleader.txt'
reference = 'Robot Leader'  
  met_pc = False
  opinion_pc = 75
  pc_gave_treasure = False
  description = 'Robot leader'
  can_talk = True
  can_fight = True
  can_look = True
  can_party = False
  can_trade = False
  
  def Talk():
    if main.scenes[1].reference == "Robot Leader's Office"  
      if met_pc == False: # hasn;t met the pc yet
        npc_talk = Draw.file.DefString(filed, 'Robot Leader Not Met Office')
        response = Draw.file.DefString(filed, 'Robot Leader Not Met Office Response')
        Draw.dialogue.Dialogue.InitDialogue(npc_talk, response)
      elif met_pc == True and opinion_pc >= 50: #has met and likes the pc
        pass
      elif met_pc == True and opinion_pc >=0: # has met and is impartial to the pc
        pass
      else: # has met and dislikes the pc
        pass
    elif main.scenes[1].reference == "Other place you can meet him":
      if met_pc == False: # hasn't met the pc yet
        pass
      #et cetera
      

import pygame, draw, math

pygame.init()

dialogue_box = pygame.Rect(20, 20, 100, 300)
response_box = pygame.Rect(200, 20, 100, 300)
done = 'end' #can send done as parameter to cleanup so the code looks nicer

class Dialogue():
  display = ''
  response = ''
  response_ref = []
  response_count = 0
  response_list = []
  response_box_list = []
  response_box_location = [100, 100]
  resp_length = 300
  resp_height = 20
  keyboard_select = 0
  mouse_select = None
  
  def InitDialogue():
    Draw.draw.dialogue = True #Sets the dialogue reference to true
    response_count = 0
    response_list = []
    response_box_location = [100, 100]
    response_box_list = []
    response = ''
    '''display = text
    response = responses
    draw.typing(display, dialogue_box) 
    Dialogue.SetResponses() #Formats the response references and text, which is more complicated than the display text.
    draw.Text.ResponseText(response, response_box)'''
    
  def SetResponses(respond):
    response_check = respond.split() #split the response string into words
    response_string = ''
    tag = False #used to find reff tags
    for word in response_check:
      if tag == True:
        response_ref.append(word)
        tag = False
      elif word == 'reff':
        tag = True
      elif word != 'reff':
        response_string += '' + word
    response_list.append(response_string)
    response_count += 1
        
  def DrawResponses():
    iii = 0
    for resp in response_list:
      float(char_count) = float(len(resp) * 10)
      float(lines) = char_count/float(resp_length) #value for line length
      line_count = int(math.ceil(lines))
      response_box_list[iii] = pygame.Rect(response_box_location[0], response_box_location[1], resp_length, resp_height * line_count)
      response_box_location[1] += (resp_height * line_count) + 20
      Draw.draw.typing(resp, response_box_list[iii])
      iii += 1
  
  def HandleEvents(mouse_pos, ev):
    if ev == pygame.MOUSEBUTTONUP:
      button_pressed = None
      rbl = response_box_list
      mp = mouse_pos
      iii = 0
      for rectangle in rbl: # checks if mouse is in each response rectangle
        if mp[0] >= rbl[0] and mp[0] <= rbl[0] + rbl[2] and mp[1] >= rbl[1] and mp[1] <= rbl[1] + rbl[3]:
          button_pressed = iii
          break
        else:
          pass
      if button_pressed != None:
        button_pressed = None
        return response_ref[button_pressed]
      else:
        pass
    elif ev == pygame.KEYDOWN:
      if event.key == k_DOWN:
        if keyboard_select < response_count:
          keyboard_select += 1
        else:
          pass
      elif event.key == k_UP:
        if keyboard_select > 0:
          keyboard_select -= 1
        else:
          pass
      elif event.key == k_ENTER:
        return response_ref[keyboard_select] #return the reference string which will be passed to the scen, then object in order to get the response.
    else:
      pass #check for mouse poistion to highlight
    
    
  def CleanUpDialogue():
    display = ''
    response = ''
    response_ref = []
    Draw.draw.dialogue = False
    

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
  response_box_list = [100, 100]
  
  def InitDialogue():
    Draw.draw.dialogue = True #Sets the dialogue reference to true
    response_count = 0
    response_list = []
    response_box_list = [100, 100]
    resp_length = 300
    resp_height = 20
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
    if ev = 'Mouse Button Down':
      pass# Check location of mouse when button was pressed
    elif ev = 'Keypress':
      pass #use the keypress to activate a response
    else:
      pass #check for mouse poistion to highlight
    
    
  def CleanUpDialogue(end):
    display = ''
    response = ''
    response_ref = []
    if end == True: #Clears dialogue reference
      Draw.draw.dialogue = False
    

import pygame, draw

pygame.init()

dialogue_box = pygame.Rect(20, 20, 100, 300)
response_box = pygame.Rect(200, 20, 100, 300)
done = 'end' #can send done as parameter to cleanup so the code looks nicer

class Dialogue():
  display = ''
  response = ''
  response_ref = []
  
  def InitDialogue(text, responses):
    Draw.draw.dialogue = True #Sets the dialogue reference to true
    display = text
    response = responses
    draw.typing(display, dialogue_box) 
    Dialogue.SetResponses() #Formats the response references and text, which is more complicated than the display text.
    draw.Text.ResponseText(response, response_box)
    
  def SetResponses():
    responses = response.split() #split the response string into words
    fullstring = ''
    tag = False #used to find reff tags
    for word in responses:
      if tag == True:
        response_ref.append(word)
        tag = False
      elif word == 'reff':
        tag = True
      elif word != 'reff':
        response += '' + word
        
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
    

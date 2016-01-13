import pygame, draw

pygame.init()

dialogue_box = pygame.Rect(20, 20, 100, 300)
response_box = pygame.Rect(200, 20, 100, 300)


class Dialogue():
  display = ''
  response = ''
  response_ref = []
  
  def InitDialogue(text, responses):
    Draw.draw.dialogue = True
    display = text
    response = responses
    draw.typing(display, dialogue_box)
    Dialogue.SetResponses()
    draw.Text.ResponseText(response, response_box)
    
  def SetResponses():
    responses = response.split()
    fullstring = ''
    tag = False
    for word in responses:
      if tag == True:
        response_ref.append(word)
        tag = False
      elif word == 'reff':
        tag = True
      elif word != 'reff':
        response += '' + word

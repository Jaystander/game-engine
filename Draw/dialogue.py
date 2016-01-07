import pygame, draw

dialogue_box = pygame.Rect(1,1,1,1)
response_box = pygame.Rect(1,1,1,1)
class Dialogue():
  display = ''
  response = ''
  
  def InitDialogue(text, responses):
    Draw.draw.dialogue = True
    display = text
    response = responses
    draw.typing(display, dialogue_box)
    draw.typing(response, response_box)

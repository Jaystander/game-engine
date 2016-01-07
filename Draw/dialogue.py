import pygame, draw

pygame.init()

dialogue_box = pygame.Rect(20, 20, 100, 300)
response_box = pygame.Rect(200, 20, 100, 300)


class Dialogue():
  display = ''
  response = ''
  
  def InitDialogue(text, responses):
    Draw.draw.dialogue = True
    display = text
    response = responses
    draw.typing(display, dialogue_box)
    draw.typing(response, response_box)
    
    

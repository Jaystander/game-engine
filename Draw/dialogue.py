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
    rbl = response_box_list
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
    button_pressed = None
    if ev == pygame.MOUSEBUTTONUP:
      mp = mouse_pos
      iii = 0
      for rct in rbl: # checks if mouse is in each response rectangle
        if mp[0] >= rct[0] and mp[0] <= rct[0] + rct[2] and mp[1] >= rct[1] and mp[1] <= rct[1] + rct[3]:
          button_pressed = iii
          break
        else:
          pass
      if button_pressed != None
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
    
  def HighlightSelection(): # Not Working, must split into one for keyboard and one for mouse and have them redraw the responses each time.
    s = pygame.Surface((rbl[keyboard_select][2],rbl[keyboard_select][3]), pygame.SRCALPHA)   # per-pixel alpha
    s.fill((255,255,255,50))                         # notice the alpha value in the color
    windowSurface.blit(s, (rbl[keyboard_select][0],rbl[keyboard_select][1]))
    iii = 0
    for rct in rbl:
      mpoz = pygame.mouse.get_pos
      if mpoz[0] >= rct[0] and mpoz[0] <= rct[0] + rct[2] and mpoz[1] >= rct[1] and mpoz[1] <= rct[1] + rct[3]:
        m = pygame.Surface((rbl[iii][2], rbl[iii][3]), pygame.SRCAPLPHA)
        m.fill((255,255,255,50))
        windowSurface.blit(m, (rbl[iii][0],rbl[iii][1]))
      iii += 1
    pygame.display.flip()  
  
  def CleanUpDialogue():
    display = ''
    response = ''
    response_ref = []
    Draw.draw.dialogue = False
    

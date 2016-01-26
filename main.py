#!/usr/bin/env python3
import sys, os
sys.path.append('Scenario')
sys.path.append('Objects')
sys.path.append('Draw')
print (sys.path)
import pygame, Draw
from Draw import draw


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR = (30, 120, 90)
BUTTERSCOTCH = (193, 106, 2)
SOFTBLUE = (160, 180, 255)
length = 50
height = 20
x = 40
x2 = 95
x3 = 150
ob1 = pygame.Rect(x, 40, length, height)
ob2 = pygame.Rect(x, 60, length, height)
ob3 = pygame.Rect(x, 80, length, height)
ob4 = pygame.Rect(x, 100, length, height)
ob5 = pygame.Rect(x, 120, length, height)
ob6 = pygame.Rect(x, 140, length, height)
ob7 = pygame.Rect(x, 160, length, height)
ob8 = pygame.Rect(x, 180, length, height)
ob9 = pygame.Rect(x, 200, length, height)
ob10 = pygame.Rect(x,220, length, height)
pl1 = pygame.Rect(x2, 40, length, height)
pl2 = pygame.Rect(x2, 60, length, height)
pl3 = pygame.Rect(x2, 80, length, height)
pl4 = pygame.Rect(x2, 100, length, height)
pl5 = pygame.Rect(x2, 120, length, height)
pl6 = pygame.Rect(x2, 140, length, height)
pl7 = pygame.Rect(x2, 160, length, height)
pl8 = pygame.Rect(x2, 180, length, height)
pl9 = pygame.Rect(x2, 200, length, height)
pl10 = pygame.Rect(x2,220, length, height)
np1 = pygame.Rect(x3, 40, length, height)
np2 = pygame.Rect(x3, 60, length, height)
np3 = pygame.Rect(x3, 80, length, height)
np4 = pygame.Rect(x3, 100, length, height)
np5 = pygame.Rect(x3, 120, length, height)
np6 = pygame.Rect(x3, 140, length, height)
np7 = pygame.Rect(x3, 160, length, height)
np8 = pygame.Rect(x3, 180, length, height)
np9 = pygame.Rect(x3, 200, length, height)
np10 = pygame.Rect(x3,220, length, height)
mainscreen = pygame.Rect(250, 25, 700, 525)
leftstats = pygame.Rect(25, 25, 200, 525)
rightstats = pygame.Rect(975, 25, 200, 525)
enemystats1 = pygame.Rect(990, 40, 170, 90)
enemystats2 = pygame.Rect(990, 140, 170, 90)
enemystats3 = pygame.Rect(990, 240, 170, 90)
enemystats4 = pygame.Rect(990, 340, 170, 90)
enemystats5 = pygame.Rect(990, 440, 170, 90)
playerstats1 = pygame.Rect(40, 40, 170, 90)
button1 = pygame.Rect(50, 560, 200, 50)
button2 = pygame.Rect(275, 560, 200, 50)
button3 = pygame.Rect(500, 560, 200, 50)
button4 = pygame.Rect(725, 560, 200, 50)
button5 = pygame.Rect(950, 560, 200, 50)
button6 = pygame.Rect(50, 635, 200, 50)
button7 = pygame.Rect(275, 635, 200, 50)
button8 = pygame.Rect(500, 635, 200, 50)
button9 = pygame.Rect(725, 635, 200, 50)
button10 = pygame.Rect(950, 635, 200, 50)
object_rects = [ob1,ob2,ob3,ob4,ob5,ob6,ob7,ob8,ob9,ob10]
place_rects = [pl1,pl2,pl3,pl4,pl5,pl6,pl7,pl8,pl9,pl10]
npc_rects = [np1,np2,np3,np4,np5,np6,np7,np8,np9,np10]


class MainMenu():
    
    master_list = []
    objects = []
    object_descriptions = []
    places = []
    place_descriptions = []
    npcs = []
    npc_descriptions = []
    description = 'This string describes the scene'
    
    
    def PopLists():
        pass
        '''for item in self.master_list:
            if item.type == 'object':
                self.objects.append(item)
            elif item.type == 'place':
                self.places.append(item)
            elif item.type == 'npc':
                self.npcs.append(item)
            else:
                print('Invalid Object Type' + item.description)'''
                
    def PopItemDesc():
        pass
        '''for item in self.objects:
            object_descriptions.append(item.description)
        for item in self.places:
            place_descriptions.append(item.description)
        for item in self.npcs:
            npc_descriptions.append(item.description)'''
scenes = [None, MainMenu]
current = scenes[1]
previous = scenes[0]
object_count = 0
npc_count = 0
place_count = 0
pygame.init()

screen = pygame.display.set_mode((1200, 700)) # creates screen to be used
pygame.display.set_caption('Basic Pygame program') 
font = pygame.font.Font(None, 24)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(SOFTBLUE)
screen.blit(background, (0,0))


    

class PermanentDraw():
    
    def DrawMainRects():
        pygame.draw.rect(screen, WHITE, mainscreen)
        pygame.draw.rect(screen, BLACK, leftstats)
        pygame.draw.rect(screen, BLACK, rightstats)
        pygame.draw.rect(screen, WHITE, button1)
        pygame.draw.rect(screen, WHITE, button2)
        pygame.draw.rect(screen, WHITE, button3)
        pygame.draw.rect(screen, WHITE, button4)
        pygame.draw.rect(screen, WHITE, button5)
        pygame.draw.rect(screen, WHITE, button6)
        pygame.draw.rect(screen, WHITE, button7)
        pygame.draw.rect(screen, WHITE, button8)
        pygame.draw.rect(screen, WHITE, button9)
        pygame.draw.rect(screen, WHITE, button10)
        
    def DrawEnemyRects():
        pygame.draw.rect(screen, WHITE, enemystats1)
        pygame.draw.rect(screen, WHITE, enemystats2)
        pygame.draw.rect(screen, WHITE, enemystats3)
        pygame.draw.rect(screen, WHITE, enemystats4)
        pygame.draw.rect(screen, WHITE, enemystats5)
        
    def DrawPlayerRects():
        pygame.draw.rect(screen, WHITE, playerstats1)
        

class Text():
    
    def PrintText(string, rect):
        #set a value through rect to define the starting point of the text
        text = str(string).split()
        x = rect[0] + 2
        y = rect[1] + 2
        write = ""
        for word in text:
            write += (" " + str(word))
            if len(write) *10 >= (rect[0] + rect[2]):
                text = font.render(write, 1, BLACK)
                screen.blit(text, (x, y,))
                y = y + 18
                write = ""
        text = font.render(write, 1, BLACK)
        screen.blit(text, (x, y,))
        
        
    def MousePosCheck(pos):
        x = pos[0]
        y = pos[1]
        iii = 0
        obj_len = len(current.object_descriptions)
        npc_len = len(current.npc_descriptions)
        place_len = len(current.place_descriptions)
        for rect in object_rects:
            if x >= rect[0] and x <= rect[0] + rect[2] and y >= rect[1] and y<= rect[1] + rect[3] and iii < obj_len:
            
                FloatBox(current.object_descriptions[iii], pos)
        iii = 0
        for rect in npc_rects:
            if x >= rect[0] and x <= rect[0] + rect[2] and y >= rect[1] and y<= rect[1] + rect[3] and iii < npc_len:
                FloatBox(current.npc_descriptions, pos)
        iii = 0
        for rect in place_rects:
            if x >= rect[0] and x <= rect[0] + rect[2] and y >= rect[1] and y<= rect[1] + rect[3] and iii < place_len:
                FloatBox(current.place_descriptions, pos)
        
    def FloatBox(string, pos):
        float_box = pygame.Rect(pos[0], pos[1], 40, 30)
        pygame.draw.rect(screen, WHITE, float_box)
        PrintText(string, float_box)
    '''def PrintStats(char, box):
        name = char['name']
        lust = 'Lust  ' + str(char['lust']) +'/100'
        orgone = 'Orgone  ' + str(char['current_orgone']) + '/' + str(char['orgone_limit'])
        x = box[0]
        y = box[1]
        namer = font.render(name, 1, BLACK)
        luster = font.render(lust, 1, BLACK)
        orgoner = font.render(orgone, 1, BLACK)
        screen.blit(namer, (x,y))
        screen.blit(luster, (x,y+18))
        screen.blit(orgoner, (x,y+36))'''
        
typing = draw.Text.PrintText

class Engine(): #autoload a main menu at some point
    
    def ChangeScene(scene):
        global scenes
        scenes[0] = scenes[1]
        scenes[1] = scene
        print(scenes[1])
        Engine.SetScene()
    
    def SetScene():
        global scenes
        Engine.DisplayHud()
        current.PopLists() # populates item lists in current scene
        current.PopItemDesc() # populates item description list in current scene
        Draw.draw.typing(current.description, Draw.draw.mainscreen) #Displays main scene description
        Engine.DispLists(current.objects, current.places, current.npcs)
        Engine.SetDescription()
        pygame.display.flip()
        
    def Check(scene = False): #run button actions Engine.Check(action)
        if scene == False:
            return False
        if scene != False:
            Engine.ChangeScene(scene)
            scene = False
        
    def DispLists(object, npc, place): #handled here
        global object_count, npc_count, place_count
        iii = 0
        for item in object:
            pygame.draw.rect(screen, WHITE, object_list[iii])
            typing(item.description, object_list[iii])
            iii += 1
            object_count +=1 # used to check if slot is active and query for mouse over object descriptions
        iii = 0
        for item in npc:
            pygame.draw.rect(screen, WHITE, npc_list[iii])
            typing(item.description, npc_list[iii])
            iii += 1
            npc_count += 1
        iii = 0
        for item in place:
            pygame.draw.rect(screen, WHITE, place_list[iii])
            typing(item.description, WHITE, place_list[iii])
            iii += 1
            place_count += 1
        
    def SetObjectDescription(object, place, npc): #handled here
        Draw.draw.SetItemDesc(object, place, npc)
        
    
    def SaveGame():
        pass
        
    def LoadGame():
        pass
        
    def LoadScenario(scenario): #loads a set of scenes into the program to use.
        pass

    def BattleSet(allies, enemies):
        pass
        
    def DisplayHud():
        draw.PermanentDraw.DrawMainRects()
        
    def SetDescription(): #calls the description from the scene and displays it.
        typing(current.description, mainscreen)

        
class MainMenu():
    
    description = 'filler'
        
import Scenario
start = True        
while True:
    #print('running loop')
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        ev = event.type
        if Draw.draw.dialogue == True:
            response_choice = Draw.dialogue.Dialogue.HandleEvent(pos, ev) 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        Draw.draw.Text.MousePosCheck(pos)
    #if scene.scene_change != False: #Scan for scene change
    #    Engine.ChangeScene()
    if start == True:
        Engine.ChangeScene(MainMenu)
        start = False
    if response_choice != None:
        scenes[1].Respond(response_choice) # Pass the button pressed to the current scene so it can pass it to the object.
    #pygame.draw.rect(screen, WHITE, mainscreen)
    #pygame.draw.rect(screen, WHITE, leftstats)
    #pygame.draw.rect(screen, WHITE, rightstats)
    #screen.blit(screen, (0, 0))
    #PermanentDraw.DrawMainRects()
    #PermanentDraw.DrawPlayerRects()
    pygame.display.flip()

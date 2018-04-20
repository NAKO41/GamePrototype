import pygame
from Hero import HERO


pygame.init()

# ----- these varaibles will be used to create the menu as well as the light version of the game ------ #
WHITE = (255,255,255)
GREY = (70,70,70)
LRED = (189,147,216)
RED = (180,122,234)
LGREEN = (49,203,0)
GREEN = (17,152,34)
LBLUE = (123,205,186)
BLUE = (113,169,247)
BLACK = (0,0,0)

SCREENWIDTH = 800   #screen width
SCREENHEIGHT = 600  #screen height

clock = pygame.time.Clock()

size = (SCREENWIDTH,SCREENHEIGHT)
screen = pygame.display.set_mode(size) #creates the canvase/screen
pygame.display.set_caption("GUI")      #caption


# ------------ this function is where the buttons will do their stuff --------- #
def Button(msg,x,y,w,h,col1,col2,action = None):

    mouse = pygame.mouse.get_pos()     #tracks mouses position
    click = pygame.mouse.get_pressed() #checks if mouse has been clicked

    if x < mouse[0] < x+w and y < mouse[1] < y+h and click[0] == 1: #this checks if the mouse is in the perameters of the green button and has been pressed
        pygame.draw.rect(screen,BLACK,(x,y,w,h))                    #then turns the button black
        if click[0] == 1 and action != None:                        #this checks if the button has a specified action with its pressing
            action()                                                #then executes said command
    elif x < mouse[0] < x+w and y < mouse[1] < y+h:                 #this checks to see if the mouse is in the perameters of the button
        pygame.draw.rect(screen,col2,(x,y,w,h))                     #then changes the colour to a darker shade
    else:                                                           #if none of the above are true
        pygame.draw.rect(screen,col1,(x,y,w,h))                     #the button will be there but in a lighter state

    font = pygame.font.SysFont("comicsansms",20)    #this defines the font of the button text
    text = font.render(msg,1,(0,0,0))               #this creats the message and it's colour
    textrect = text.get_rect()
    textrect.center = (x + (w/2),y + (h/2))        
    screen.blit(text,textrect)                           
# ----------- this concludes the section of code for the buttons ------------ #




# ----------- This section of code will be for the setting menu ------------- #
def Setting():
    setting = True
    while setting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:   #if the escape button is pressed
                    setting = False              #leave the settings menu
                
        # ------ visible things go here ------- #
        screen.fill(WHITE)

        fontS = pygame.font.Font(None,35)                 #defines the font
        textS = fontS.render("SETTINGS",1,BLACK)          #renders the text
        TextSRect = textS.get_rect()                      #creates the text into an object
        TextSRect.center = (SCREENWIDTH/2,SCREENHEIGHT/5) #centers the text 
        screen.blit(textS,TextSRect)                      #print the setting title
 

        
        pygame.display.flip()
        clock.tick(60)
# ---------- this concludes the section for the settings menu ----------- #




# ---------- this section of code will create and maintain the load screen ---------- #
def Load():
    load = True
    while load:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:  #if the escape button is pressed
                    load = False                #leave the load file screen
                    
        # ------ visible things will go here ------ #
        screen.fill(WHITE)

        fontL = pygame.font.Font(None,35)                 #defines the font
        textL = fontL.render("Load Saved File",1,BLACK)   #renders the text
        TextLRect = textL.get_rect()                      #creates the text into an object
        TextLRect.center = (SCREENWIDTH/2,SCREENHEIGHT/5) #centers the text 
        screen.blit(textL,TextLRect)                      #print the Load title


        pygame.display.update()
        clock.tick(60)
# ---------- this concludes the code that is for the Load file screen ------------#




# ---------- this long ass code thing will be the test demo for a game that will incorperate the things i want into my summative ------------- #
def Game():
    Sart = True
    while Sart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.Quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    pygame.quit()

        # -------- visible items --------- #
        
        screen.fill(GREY)



        pygame.display.update()
        clock.tick(60)
# ----------- and this is the end of it ----------------------- #




# ---------- this code will be for the starting menu ---------------- #
menu = True
while menu:                           #this is the menu loop
    for event in pygame.event.get():  #for every event that happens
        if event.type == pygame.QUIT: #if red box in the corner is pressed
            pygame.quit()             #code closses
        elif event.type==pygame.KEYDOWN:
           if event.key==pygame.K_ESCAPE:
               menu = False


    # ------- draw code goes after here ------- #
    screen.fill(WHITE)

    #title font
    fontm = pygame.font.Font(None,35)                #defines the font
    textm = fontm.render("TITLE",1,BLACK)            #renders the text
    TextRect = textm.get_rect()                      #creates the text into an object
    TextRect.center = (SCREENWIDTH/2,SCREENHEIGHT/5) #centers the text 
    screen.blit(textm,TextRect)                      #print the title

    
    Button("Start",SCREENWIDTH/2-50,SCREENHEIGHT/3,100,50,RED,LRED,Game)             #green button that will start the quick demo
    Button("Load",SCREENWIDTH/2-50,SCREENHEIGHT/3+150,100,50,GREEN,LGREEN,Load)      #red button taht brings to load file menu
    Button("Settings",SCREENWIDTH/2-50,SCREENHEIGHT/3+300,100,50,BLUE,LBLUE,Setting) #blue button that brings to settings menu
    Button("ESC",10,10,100,50,WHITE,GREY,pygame.quit)                                #white button that quits the game


    pygame.display.flip()

    clock.tick(60)
# ----------- This concludes the section of the main menu code ----------- #



pygame.quit()
    

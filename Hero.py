#this class will be the class for the hero/player character
import pygame
WHITE = (255,255,255)

class HERO():


    def __init__(self,width = 50,height = 60):
        super().__init__() #this allows pygame to draw the sprite

        self.image = pygame.Surface([width,height]) #defines the sprites hitbox
        self.image.fill(WHITE)                      #makes it white
        self.image.set_colorkey(WHITE)              #makes the white transparent

        #define he hero's attributes
        self.width = width
        self.height = height
        
        #draws the visible parts of the sprite
        pygame.draw.rect(self.image,[20,0,10,20])   #sprites head
        pygame.draw.rect(self.image,[10,20,30,40])  #prites body

        #fetches the invisible hitbox of the hero
        self.rect = self.image.get_rect()
        

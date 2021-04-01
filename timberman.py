import pygame

class Timberman:

    def __init__(self):

        self.texture = pygame.image.load("Assets/timberman.png").convert_alpha()
        self.live = 1
        self.x = 20
        self.y = 512
        self.action = 0
        self.collide_y = 650
        self.state = 0 #0 is left 1 is right
    
    def setTimberman(self):

        if self.action == 0:

            if self.state == 0:
                self.texture = pygame.image.load("Assets/timberman.png").convert_alpha()
                self.x = 110
            elif self.state == 1:
                self.texture = self.texture = pygame.image.load("Assets/timberman.png").convert_alpha()
                self.texture = pygame.transform.flip(self.texture,True,False)
                self.x = 320
        else:
            if self.state == 0:
                self.texture = pygame.image.load("Assets/timbermanaction.png").convert_alpha()
                self.x = 110
            elif self.state == 1:
                self.texture = self.texture = pygame.image.load("Assets/timbermanaction.png").convert_alpha()
                self.texture = pygame.transform.flip(self.texture,True,False)
                self.x = 320

    

import pygame

class Tree:

    def __init__(self,state):

        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.state = state #0 is normal 1 is branch left 2 is branch right
        self.texture = pygame.image.load("Assets/tree.png").convert_alpha()

    def setTree(self):

        if self.state == 0:
            self.texture = pygame.image.load("Assets/tree.png").convert_alpha()
            self.x = 200
            self.width = 120
            self.height = 100
        elif self.state == 1:
            self.texture = pygame.image.load("Assets/treeb.png").convert_alpha()
            self.x = 80
            self.width = 240
            self.height = 100
        elif self.state == 2:
            self.texture = pygame.image.load("Assets/treeb.png").convert_alpha()
            self.texture = pygame.transform.rotate(self.texture,180)
            self.x = 200
            self.width = 240
            self.height = 100





                                

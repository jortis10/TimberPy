from tree import  Tree
from timberman import  Timberman
from random import randint
import pygame

class Game:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.nb = 6
        self.trees = []
        self.timberman = Timberman()
        self.isDetruit = False
        self.point = 0
        self.branch = 50

    def updateView(self, screen: pygame.Surface, nb):
        self.displayTimberman(screen)
        self.displayTrees(screen, nb)
        self.displayPoint(screen)



    def generateTrees(self, probability):
        if len(self.trees) == 0:
            for k in range(self.nb):
                self.trees.append(Tree(0))
        elif self.isDetruit:

            for k in range(self.nb-1,0,-1):
                self.trees[k].state = self.trees[k-1].state

            if self.trees[1].state == 0:
                a = randint(0,100)
                b = randint(0,100)
                if a <= probability:
                    self.trees[0].state = 0
                else:
                    if b <= 50:
                        self.trees[0].state = 1
                    else:
                        self.trees[0].state = 2
            else:
                self.trees[0].state = 0

            self.isDetruit = False
            

    def displayTrees(self, screen: pygame.Surface, settree):
        for k in range(self.nb):
            if settree == 1:
                self.trees[k].setTree()

            self.trees[k].y = k*self.trees[k].height
            screen.blit(self.trees[k].texture,(self.trees[k].x,self.trees[k].y))

    def displayTimberman(self, screen: pygame.Surface):
        self.timberman.setTimberman()
        screen.blit(self.timberman.texture,(self.timberman.x,self.timberman.y))


    def displayPoint(self, screen: pygame.Surface):
        font = pygame.font.SysFont("Assets/arial", 60)

        text = font.render(str(self.point), True, (64, 64, 64))
        screen.blit(text,(30,30))

    def displayHighScore(self, screen: pygame.Surface):
        pygame.draw.rect(screen,pygame.Color(255, 255, 255),(0,0,32,32))
        print("Meilleur score: " + str(self.point))

    def displayWoodCut(self, screen: pygame.Surface, direction):

        if direction == 0: #left
            r = range(240, 480, 20)
            for x in r:
                y = 0.0048*x**2-3.6*x+1128.57
                screen.blit(self.trees[5].texture,(x,y))
                pygame.display.flip()
                screen.blit(pygame.image.load("Assets/background.png").convert_alpha(),(0,0))
                self.updateView(screen,0)
                pygame.time.Clock().tick(500)

        if direction == 1: #right
            r = range(150, -100, -20)
            for x in r:
                y = 0.01*x**2-1.45*x+500
                screen.blit(self.trees[5].texture,(x,y))
                pygame.display.flip()
                screen.blit(pygame.image.load("Assets/background.png").convert_alpha(),(0,0))
                self.updateView(screen,0)
                pygame.time.Clock().tick(500)



        





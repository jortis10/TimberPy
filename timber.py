import pygame
from game import Game


whidth = 480
height = 720

def main():
    #initialisation pygame
    pygame.init()

    FPS = 30 # frames per second setting
    fpsClock = pygame.time.Clock()

   

    #Generation de la fenêtre
    screen = pygame.display.set_mode((whidth,height))
    #icon = pygame.image.load("Assets/icon.png").convert()
    #pygame.display.set_icon(icon)
    pygame.display.set_caption("Timber")
    background = pygame.image.load("Assets/background.png").convert_alpha()

    screen.blit(background,(0,0))

    jeu = Game(whidth,height)

    running = True
    count = 0
    while running:
        for event in pygame.event.get():

            jeu.generateTrees(jeu.branch)

            if event.type == pygame.QUIT or jeu.timberman.live < 1:
                running = False          

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                jeu.timberman.state = 0
                jeu.isDetruit = True
                jeu.point += 1
                jeu.timberman.action = 1
                jeu.displayWoodCut(screen,0)

            elif keys[pygame.K_RIGHT]:
                jeu.timberman.state = 1
                jeu.isDetruit = True
                jeu.point += 1
                jeu.timberman.action = 1
                jeu.displayWoodCut(screen,1)
            
            if (jeu.timberman.state == 0 and jeu.trees[5].state == 1) or (jeu.timberman.state == 1 and jeu.trees[5].state == 2):
                jeu.timberman.live -= 1
                jeu.isDetruit = True
            
        #Routine de frame
        screen.blit(background,(0,0))
        jeu.updateView(screen,1)
        pygame.display.flip()

        #Animation
        if count == 5:
            jeu.timberman.action = 0
            count = 0

        if jeu.point > 100:
            jeu.branch = 30
        elif jeu.point > 200:
            jeu.branch = 20


        fpsClock.tick(FPS)
        count+=1


    #while True:
    jeu.displayHighScore(screen)


    #Fermeture du jeu
    pygame.quit()




if __name__ == '__main__':
    main()


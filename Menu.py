import pygame
import os #importer os pour pouvoir ouvir d'autre fenetre


def change_de_fenetre():#on met une fonction pour changer de fenetre
    cmd = "Platformer.py"# ouvrir le fichier jeu_pong.py
    
    os.startfile("Platformer.py")#pour quon puisse ouvrir la fenetre

pygame.init()

continuer = True

screen = pygame.display.set_mode((1280, 720))

bg = pygame.image.load("IMG2/background.png")

play = pygame.image.load("IMG2/play.png")
play = pygame.transform.scale(play, (250, 100))
play_rect = play.get_rect()
play_rect.x, play_rect.y = 500, 480

Quit = pygame.image.load("IMG2/quit.png")
Quit = pygame.transform.scale(Quit, (250, 100))
Quit_rect = Quit.get_rect()
Quit_rect.x, Quit_rect.y = 200, 480

option = pygame.image.load("IMG2/option.png")
option = pygame.transform.scale(option, (75, 75))
option_rect = option.get_rect()
option_rect.x, option_rect.y = 1180, 30

rules = pygame.image.load("IMG2/rules.png")
rules = pygame.transform.scale(rules, (250, 100))
rules_rect = rules.get_rect()
rules_rect.x, rules_rect.y = 800, 480

back = pygame.image.load("IMG2/return.png")
back = pygame.transform.scale(back, (250, 100))
back_rect = back.get_rect()
back_rect.x, back_rect.y = 800, 10080

volume_off = pygame.image.load("IMG2/volume_off.png")
volume_off = pygame.transform.scale(back, (250, 100))
volume_off_rect = volume_off.get_rect()
volume_off_rect.x, volume_off_rect.y = 800, 10080

volume_on = pygame.image.load("IMG2/volume_on.png")
volume_on = pygame.transform.scale(back, (250, 100))
volume_on_rect = volume_on.get_rect()
volume_on_rect.x, volume_on_rect.y = 800, 10080

#pygame.mixer.music.load()
#pygame.mixer.music.play(-1)
#pygame.mixer.music.set_volume(0.2)
#pygame.mixer.music.stop()


while continuer:
    screen.blit(bg, (0,0))
    
    screen.blit(play, play_rect)
        
    screen.blit(Quit, Quit_rect)

    screen.blit(option, option_rect)

    screen.blit(rules, rules_rect)

    screen.blit(back, back_rect)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
        x,y = pygame.mouse.get_pos()

        if play_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            continuer = False
            os.startfile("Platformer.py")
            pygame.quit()
            
        if Quit_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            pygame.quit()

        if option_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            volume_on_rect.x, volume_on_rect.y = 500, 480
            play_rect.x, play_rect.y = 500, 580
            Quit_rect.x, Quit_rect.y = 200, 580
            back_rect.x, back_rect.y = 800, 580
            rules_rect.x, rules_rect.y = 800, 10080
            option_rect.x, option_rect.y = 1180, 10080

        if rules_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            bg = pygame.image.load("IMG2/background2.png")
            play_rect.x, play_rect.y = 500, 580
            Quit_rect.x, Quit_rect.y = 200, 580
            back_rect.x, back_rect.y = 800, 580
            rules_rect.x, rules_rect.y = 800, 10080

        if back_rect.collidepoint(x,y) and event.type == pygame.MOUSEBUTTONUP:
            bg = pygame.image.load("IMG2/background.png")
            play_rect.x, play_rect.y = 500, 480
            Quit_rect.x, Quit_rect.y = 200, 480
            back_rect.x, back_rect.y = 800, 10080
            rules_rect.x, rules_rect.y = 800, 480
            option_rect.x, option_rect.y = 1180, 30
            
    pygame.display.update()

        

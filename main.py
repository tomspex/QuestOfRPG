import threading
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

import global_var
import game
import data
import player

p = player.player()

gamethread = threading.Thread(target=game.run, args=(p,))
gamethread.start()

# graphics loop

pygame.init()
pygame.display.set_caption(data.locations[p.location]["name"].title())
screen = pygame.display.set_mode((640, 480)) 

pygame.mixer.music.load("music/1.mp3")
pygame.mixer.music.play(-1)

bg = pygame.image.load("bg/1.png").convert()
bg = pygame.transform.scale(bg, screen.get_size())

background_color = (0, 0, 0)

while global_var.running:
    screen.fill(background_color)

    screen.blit(bg, (0, 0))

    pygame.display.flip()
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            print("Input \"exit\" to quit the game.")

pygame.quit()
gamethread.join()

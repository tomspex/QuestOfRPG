import threading
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

import global_var
import graphics
import game
import data
import player

pygame.init()

p = player.player()
gamethread = threading.Thread(target=game.run, args=(p,))
gamethread.start()  

pygame.display.set_caption(data.locations[p.location]["name"].title())
screen = pygame.display.set_mode((640, 480)) 
global_var.screen = screen

global_var.bg = graphics.refresh(p)

background_color = (0, 0, 0)

while global_var.running:
    screen.fill(background_color)

    screen.blit(global_var.bg, (0, 0))

    pygame.display.flip()
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            print("Input \"exit\" to quit the game.")

pygame.quit()
gamethread.join()

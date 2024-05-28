import pygame

import global_var
import player
import data

def refresh_graphics(p:player.player):
	bg = pygame.image.load("bg/" + data.locations[p.location]["bg"]).convert()
	bg = pygame.transform.scale(bg, global_var.screen.get_size())
	return bg

def refresh_audio(p:player.player):
    try:
        pygame.mixer.music.load("music/" + data.locations[p.location]["music"])
        pygame.mixer.music.play(-1)
    except:
        pass

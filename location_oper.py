import pygame

import player
import data

def sleep(p:player.player):
    p.health = p.max_health
    p.mana = p.max_mana
    print("All your stats have been restored.")

def throwbrickatwindow(p:player.player):
    pygame.mixer.Sound("sfx/window_smash.mp3").play()
    print("You threw a brick at the window and smashed it.")
    print("Why did you do that?")
    for i in range(len(data.locations[p.location]["inspect_list"])):
        if(data.locations[p.location]["inspect_list"][i]["type"] == "window"):
            data.locations[p.location]["inspect_list"][i]["smashed"] = True
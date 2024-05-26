import inspect_obj
import player
import data

def sleep(p:player.player()):
    p.health = p.max_health
    p.mana = p.max_mana
    print("All your stats have been restored.")

import sys

import player

def inventory(p:player.player()):
    p.get_inventory()

def damage(p:player.player()):
    print("Pick the item you wish to see the damage of.")
    p.get_item_damage(input())

def help(p:player.player()):
    print("List of possible commands:")
    operations = dir(sys.modules[__name__])
    for i in range(len(operations)):
        if(operations[i][0] != '_'):
            print("    " + operations[i])
    print("")


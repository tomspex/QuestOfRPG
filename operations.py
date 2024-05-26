import sys
import os

import player
import data

notcommands = [
    "os",
    "sys",
    "player",
    "notcommands"
]

def inventory(p:player.player()):
    p.get_inventory()

def damage(p:player.player()):
    print("Pick the item you wish to see the damage of.\n")
    p.get_item_damage(input())

def help(p:player.player()):
    global notcommands
    print("List of possible commands:")
    operations = dir(sys.modules[__name__])
    for i in range(len(operations)):
        if(operations[i][0] != '_'):
            iscommand = True
            for j in range(len(notcommands)):
                if(operations[i] == notcommands[j]):
                    iscommand = False
            if(iscommand):
                print("    " + operations[i])
    print("")

def clear(p:player.player()):
    os.system("cls" if os.name == "nt" else "clear")

def location(p:player.player()):
    print("\nYou are currently " + data.locations[p.location]["preposition"] + " " + data.locations[p.location]["name"] + ".")
    print("What do you wish to do? (input \"help\" for a list of operations)\n")

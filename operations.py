import sys
import os

import inspect_obj
import player
import data

notcommands = [
    "os",
    "sys",
    "player",
    "data",
    "inspect_obj",
    "notcommands"
]

def inventory(p:player.player):
    p.get_inventory()

def damage(p:player.player):
    print("Pick the item you wish to see the damage of.\n")
    p.get_item_damage(input())

def help(p:player.player):
    global notcommands
    print("List of possible global commands:")
    operations = dir(sys.modules[__name__])
    for i in range(len(operations)):
        if(operations[i][0] != '_'):
            iscommand = True
            for j in range(len(notcommands)):
                if(operations[i] == notcommands[j]):
                    iscommand = False
            if(iscommand):
                print("    " + operations[i])
    print("List of possible local commands:")
    if("commands" in data.locations[p.location]):
        for i in range(len(data.locations[p.location]["commands"])):
            print("    " + data.locations[p.location]["commands"][i])
    print("")

def clear(p:player.player):
    os.system("cls" if os.name == "nt" else "clear")

def location(p:player.player):
    print("\nYou are currently " + data.locations[p.location]["preposition"] + " " + data.locations[p.location]["name"] + ".")
    print("What do you wish to do? (input \"help\" for a list of operations)\n")

def inspect(p:player.player):
    if("inspect_list" in data.locations[p.location]):
        print("List of objects to inspect:")
        locations_length = len(data.locations[p.location]["inspect_list"]) 
        for i in range(locations_length):
            print("    " + data.locations[p.location]["inspect_list"][i]["name"])
        print("What do you want to inspect?\n")
        answer = input()
        found = False
        for i in range(locations_length):
            if(data.locations[p.location]["inspect_list"][i]["name"] == answer):
                found = True
                if("type" in data.locations[p.location]["inspect_list"][i]):
                    try:
                        exec("inspect_obj." + data.locations[p.location]["inspect_list"][i]["type"] + "(p, data.locations[p.location][\"inspect_list\"][i])")
                        break
                    except:
                        pass
        if(found == False):
            print(answer + " is not an inspectable object.")
    else:
        print("Nothing to inspect.")

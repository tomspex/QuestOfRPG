import data
import player
import location_oper

def door(p:player.player, obj):
    message(p, obj)
    print("Enter? (y/n)\n")
    if(input() == "y"):
        print("Entering the " + obj["name"])
        p.location = obj["door_target"]

def bed(p:player.player, obj):
    message(p, obj)
    print("Sleep? (y/n)\n")
    if(input() == "y"):
        location_oper.sleep(p)

def message(p:player.player, obj):
    if("message" in obj):
        print(obj["message"])

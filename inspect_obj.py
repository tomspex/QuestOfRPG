import reset_win
import player
import location_oper
import global_var
import operations

def door(p:player.player, obj):
    message(p, obj)
    print("Enter? (y/n)\n")
    if(input() == "y"):
        print("Entering the " + obj["name"] + "...")
        p.location = obj["door_target"]
        global_var.bg = reset_win.refresh_graphics(p)
        reset_win.refresh_audio(p)
        operations.location(p)

def bed(p:player.player, obj):
    message(p, obj)
    print("Sleep? (y/n)\n")
    if(input() == "y"):
        location_oper.sleep(p)

def window(p:player.player, obj):
    message(p, obj)
    if(obj["smashed"] == True):
        print("It's smashed.")
    else:
        print("You can see your reflection in it.")

def message(p:player.player, obj):
    if("message" in obj):
        print(obj["message"])

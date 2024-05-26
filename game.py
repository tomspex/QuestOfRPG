import globalvar
import player
import location
import operations

def run(p:player.player()):
    operations.location(p)
    
    while globalvar.running:
        print("")
        location.run_location(p)
        #os.system("cls" if os.name == "nt" else "clear")

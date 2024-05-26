import global_var
import player
import location
import operations

def run(p:player.player()):
    operations.location(p)
    
    while global_var.running:
        print("")
        location.run_location(p)
        #os.system("cls" if os.name == "nt" else "clear")

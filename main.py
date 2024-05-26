import player
import location
import operations

player = player.player()

operations.location(player)

run = True
while run:
    print("")
    run = location.run_location(player)
    #os.system("cls" if os.name == "nt" else "clear")

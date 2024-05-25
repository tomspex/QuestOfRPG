import data
import func
import player
import operations

player = player.player()

while True:
    print("\nYou are currently " 
        + player.location["preposition"] 
        + " " 
        + player.location["name"] 
        + "."
    )
    print("What do you wish to do? (input \"help\" for a list of operations)\n")
    answer = input()
    try:
        exec("operations." + answer + "(player)")
    except:
        if(answer == "exit"):
            quit()
        else:
            print("Input is not valid.")

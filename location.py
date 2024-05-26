import data
import operations

def run_location(player):
    answer = input()
    try:
        exec("operations." + answer + "(player)")
    except:
        if(answer == "exit"):
            return False
        elif(len(answer) != 0):
            print(answer + " is not a valid command.\n")
            operations.help(player)
    #input()
    return True

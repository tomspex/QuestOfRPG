import sys

import global_var
import data
import operations
import location_oper

def run_location(player):
    answer = input()
    try:
        exec("operations." + answer.replace(" ", "") + "(player)")
    except:
        try:
            exec("location_oper." + answer.replace(" ", "") + "(player)")
        except:
            if(answer == "exit"):
                global_var.running = False
            elif(len(answer) != 0):
                print(answer + " is not a valid command.\n")
                operations.help(player)
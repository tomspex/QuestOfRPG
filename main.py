import data
import func
import classes

player = classes.player()

while True:
	print("You are currently " 
		+ player.location["preposition"] 
		+ " " 
		+ player.location["name"] 
		+ "."
	)
	print("What do you wish to do? (input ? for a list of operations)\n")
	answer = input()
	match answer:
		case "inventory":
			player.get_inventory()
		case "damage":
			print("Pick the item you wish to see the damage of.\n")
			player.get_item_damage(input())
		case "leave":
			quit()

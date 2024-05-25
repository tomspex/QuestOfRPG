import data

class player:
	health = 10
	location = data.locations[0]
	mana = 5
	defense = 1
	intelligence = 1
	luck = 1

	inventory = [0, 1]

	def get_inventory(self):
		for i in range(len(self.inventory)):
			print(data.items[self.inventory[i]])
		print("")

	def get_item_damage(self, item):
		for i in range(len(self.inventory)):
			if(item == data.items[self.inventory[i]]["name"]):
				print(item 
				+ " damage: " 
				+ str(data.items[self.inventory[i]]["damage"]) + "\n")

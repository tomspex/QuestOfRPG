import data

class player:
    max_health = 10
    max_mana = 5

    location = 1
    health = 10
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
        found = False
        for i in range(len(self.inventory)):
            if(item == data.items[self.inventory[i]]["name"]):
                found = True
                if("damage" in data.items[self.inventory[i]]): 
                    print(item 
                    + " damage: " 
                    + str(data.items[self.inventory[i]]["damage"]))
                else:
                    print(item + " does not have a damage property.")
        if(not found):
            print(item + " is not a valid item. Input \"inventory\" for a list of items.")

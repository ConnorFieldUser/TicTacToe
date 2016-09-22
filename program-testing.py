
# Inventory tracker Infinity Blade

# Player
# Inventory
# Items

player = {"bag": {"large health regen potion": 20}}
{
    "large health regen potion": {
        "quantity": 1
    }
}
sacrifice_name = input("Welcome warrior! What is your name? ")
player["name"] = sacrifice_name
player["bag"] = ""
print(player)


while True:
    choice = input("Would you like to look in your (b)ag or (s)hop?\n>>>")

    if choice == 'b':
        print("checking bag")
        for item in player["bag"].keys():
            quantity = player["bag"][item]["quantity"]
            print("{} - {}".format(item, quantity))

    elif choice == 's':
        item_name = input("What item fo you want? ")
        item_quantity = int(input("How many?"))
        player["bag"][item_name] = {"quantity": item_quantity}

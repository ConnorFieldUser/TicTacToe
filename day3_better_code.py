# NEW FILE
# Inventory tracker Infinity Blade

# Player
# Inventory
# Items


def add_item_to_inventory(player):
    item_name = input("What item fo you want? ")
    item_quantity = int(input("How many?"))
    if item_name in player["inventory"].keys():
        player["inventory"][item_name]["quantity"] += item_quantity
    else:
        player["bag"][item_name] = {"quantity": item_quantity}


def inspect_bag(player):
    print("checking bag")
    for item in player["bag"].keys():
        quantity = player["bag"][item]["quantity"]
        print("{} - {}".format(item, quantity))


def player_input(player, choice):
    if choice == 'b':
        inspect_bag(player)
    elif choice == 's':
        player["bag"] = add_item_to_inventory(player)


def make_character():
    player = {"bag": {"large health regen potion": {"quantity": 20}}}

    sacrifice_name = input("Welcome warrior! What is your name? ")
    player["name"] = sacrifice_name
    player["bag"] = ""
    return player

#############################################################################

player = make_character()

while True:
    choice = input("Would you like to look in your (b)ag or (s)hop?\n>>>")
    player_input(player, choice)

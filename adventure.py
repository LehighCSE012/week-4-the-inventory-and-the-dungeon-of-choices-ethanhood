import random
# Method to display player health
def display_player_status(player_health):
    print("Your current health: " + str(player_health))

def handle_path_choice(player_health):
    choice=random.choice(["left", "right"])
    if choice=="right":
        print("You fall into a pit and lose 15 health points.")
        player_health = player_health-15
        if player_health < 0:
            player_health=0
            print("You are barely alive!")
    else:
        print("You encounter a friendly gnome who heals you for 10 health points")
        if player_health<= 90:
            player_health=player_health+10
    updated_player_health = player_health
    return updated_player_health

def player_attack(monster_health):
    print("You strike the monster for 15 damage!")
    monster_health = monster_health-15
    updated_monster_health = monster_health
    return updated_monster_health

def monster_attack(player_health):
    CRITICAL = random.random()
    if CRITICAL<=.5:
        player_health = player_health-20
        print("The monster lands a critical hit for 20 damage!")
    else:
        player_health = player_health-10
        print("The monster hits you for 10 damage!")
    updated_player_health = player_health
    return updated_player_health

def combat_encounter(player_health, monster_health, has_treasure):
    # ... function code ...
    while 1:
        if player_health <=0:
            print("Game Over")
            treasure_found_and_won = False
            break
        elif monster_health<=0:
            print("You defeated the monster!")
            treasure_found_and_won = has_treasure
            break
        else:
            monster_health = player_attack(monster_health)
            display_player_status(player_health)
            player_health = monster_attack(player_health)


    return treasure_found_and_won, player_health # boolean

def check_for_treasure(has_treasure):
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

def acquire_item(inventory, item):
    inventory.append(item)
    print("You acquired a " + str(item) + "!")
    return inventory

def display_inventory(inventory):
    i = 1
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for item in inventory:
            print(str(i) + ". " + str(item))
            i=i+1
def enter_dungeon(player_health, inventory, dungeon_rooms):
    for room in dungeon_rooms:
        print("Entering... " + room[0])
        if room[1] != "None":
            inventory = acquire_item(inventory, room[1])
        match room[2]:
            case "puzzle":
                print("You encounter a puzzle!")
                choice = input("Would you like to Solve or Skip the puzzle?\n")
                if choice=="solve":
                    result = random.choice([True, False])
                    if result==True:
                        print(room[3][0])
                        player_health = player_health + int(room[3][2])
                    else:
                        print(room[3][1])
                        player_health = player_health + int(room[3][2])
                        display_player_status(player_health)
                    if player_health <= 0:
                        player_health=0
                        print("You are barely alive!")
                else:
                    print("Really? Okay fine, be boring...")
            case "trap":
                print("You see a potential trap!")
                choice = input("Would you like to disarm or bypass the trap?\n")
                if choice=="disarm":
                    # True is success and False is failure
                    result = random.choice([True, False])
                    if result==True:
                        print(room[3][0])
                        player_health = player_health + int(room[3][2])
                    else:
                        print(room[3][1])
                        player_health = player_health + int(room[3][2])
                        display_player_status(player_health)
                    if player_health < 0:
                        player_health=0
                        print("You are barely alive!")
                else:
                    print("Really? Okay fine, be boring...")
            case "none":
                print("There doesn't seem to be a challenge in this room. You move on.")
        display_inventory(inventory)

    display_player_status(player_health)
    return player_health, inventory

def main():
    player_health = 100
    monster_health = 70 # Example hardcoded value
    has_treasure = False
    inventory = []
    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle",
            ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
        ("A narrow passage with a creaky floor", "None", "trap",
            ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none",
            None),
        ("A small room with a locked chest", "treasure", "puzzle",
            ("You cracked the code!", "The chest remains stubbornly locked.", -5))]

    has_treasure = random.choice([True, False]) # Randomly assign treasure

    player_health = handle_path_choice(player_health)

    treasure_obtained_in_combat, player_health = combat_encounter(
        player_health,
        monster_health,
        has_treasure
    )

    display_player_status(player_health)

    player_health, inventory = enter_dungeon(player_health,
                                            inventory,
                                            dungeon_rooms)

    check_for_treasure(treasure_obtained_in_combat) # Or has_treasure, depending on logic

    print("\n")

if __name__ == "__main__":
    main()

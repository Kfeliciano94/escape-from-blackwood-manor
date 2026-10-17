# ProjectTwo.py
# Author: Krystal Feliciano
# Description:
# "Escape from Blackwood Manor" - a text-based horror/adventure game.
# The player must collect all items to break the curse before encountering the ghost of Lady Blackwood

# Functions

def show_instructions():
    """Display the main menu and commands."""
    print("Escape from Blackwood Manor")
    print("Collect all 7 items to break the curse and escape the manor.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("Type 'exit' to quit the game.")
    print("---------------------------")


def show_status(current_room, inventory, rooms):
    """Display the player's current status."""
    print("---------------------------")
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("---------------------------")


def get_new_state():
    """Main game loop and logic control (driver function)."""

    # Dictionary linking rooms, directions, and items
    rooms = {
        'Foyer': {'North': 'Library', 'East': 'Kitchen', 'item': 'Candle'},
        'Library': {'South': 'Foyer', 'West': 'Study', 'East': 'Dining Hall', 'item': 'Ancient Tome'},
        'Dining Hall': {'West': 'Library', 'South': 'Chapel', 'item': 'Silver Key'},
        'Chapel': {'North': 'Dining Hall', 'West': 'Haunted Basement', 'item': 'Holy Relic'},
        'Kitchen': {'West': 'Foyer', 'North': 'Servants Quarters', 'item': 'Rusty Knife'},
        'Servants Quarters': {'South': 'Kitchen', 'East': 'Haunted Basement', 'item': 'Pocket Watch'},
        'Haunted Basement': {'West': 'Servants Quarters', 'East': 'Chapel', 'North': 'Study', 'villain': 'Lady Blackwood'},
        'Study': {'South': 'Haunted Basement', 'East': 'Library', 'item': 'Cursed Mirror'}
    }

   
    current_room = 'Foyer'
    inventory = []
    required_items = ['Candle', 'Ancient Tome', 'Silver Key', 'Rusty Knife', 'Cursed Mirror', 'Pocket Watch', 'Holy Relic']

    show_instructions()

    # --- Simplified While Loop ---
    while True:
        # Show player status each turn
        show_status(current_room, inventory, rooms)
        move = input("Enter your move: ").strip().title()

        # Unified quit condition
        if move.lower() == 'exit':
            print("You fled the manor... alive, but cursed forever.")
            break

        # Check if item is in current room
        if move.startswith("Get "):
            item_name = move[4:]
            if 'item' in rooms[current_room] and item_name == rooms[current_room]['item']:
                inventory.append(item_name)
                print(f"{item_name} collected!")
                del rooms[current_room]['item']
            else:
                print("That item isn't here.")

        # movement
        elif move.startswith("Go "):
            direction = move[3:]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way.")

        # Invalid commands
        else:
            print("Invalid command. Try again.")

        # Check for villain encounter
        if 'villain' in rooms[current_room]:
             if all(item in inventory for item in required_items): # player wins
                 print("\n✨ The Holy Relic glows brightly as Lady Blackwood fades into the mist...")
                 print("Congratulations! You have broken the curse and escaped Blackwood Manor!")
                 break
             else: # player loses
                 print("\n💀 The ghost of Lady Blackwood rises before you..")
                 print("You have not gathered all the relics - your soul belongs to her now!")
                 print("GAME OVER.")
                 break


# Run game
if __name__ == "__main__":
    get_new_state()





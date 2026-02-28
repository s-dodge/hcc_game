# HCC Text-Based Adventure game by Soren M. Dodge | 2026
# from colorama import init, Fore, Back
from helpers import typewrite, clear_screen



# WORLD
rooms = {
    "it department":{
        "name": "IT Department",
        "description": ("The bright, fluorescent lights here illuminate stacks of old equipment and tangles of Cat6 cable...where did everyone go?\n\nThe lights flicker..."
        ),
        "exits": {"north": "storage", "east": "printing department", "south":"south hallway"},
        "items": ["stick of ddr5 ram", "book", "workstation", "broken keyboard", "bin of mice"]

    },
    "south hallway":{
        "name":"south hallway",
        "description":("The hallway is empty. You see the parking lot to the west, the cafeteria to the east, and a stairwell to the south"),
        "exits":{"north":"it department","west":"parking lot","east":"cafeteria", "south":"south stairwell"},
        "items":[]
    },
    "east hallway":{
        "name":"east hallway",
        "description":("The hallway is empty. Where is everyone...?"),
        "exits":{"west":"printing department", "south":"cafeteria"},
        "items":[]
    },
    "printing department":{
        "name":"printing department",
        "description":("The room is empty. Norm is usually here this time of day."),
        "exits":{"east":"east hallway", "west":"it department"},
        "items":["pamphlet","poster"]
    },
    "storage":{
        "name":"storage area",
        "description":("The walls are lined with shelves of assets...power cables, monitors, laptop bags, network switches, and unnameable layer 3 devices."),
        "exits":{"south":"it department"},
        "items":["usb drive", "sticky note", "keycard"]
    },
    "cafeteria":{
        "name":"cafeteria",
        "description":(""),
        "exits":{"north":"east hallway","west":"south hallway", "south":"exit"},
        "items":[]
    },
    "parking lot":{
        "name":"parking lot",
        "description":(""),
        "exits":{"east":"south hallway"},
        "items":[]
    },
    "south stairwell":{
        "name":"south stairwell",
        "description":(""),
        "exits":{"north":"south hallway","south":"exit"},
        "items":[]
    },
    "exit":{
        "name":"Main Campus",
        "description":(""),
        "exits":{"north":"cafeteria","south":"library","east":"kepler theater"},
        "items":[]
    },

}

# ITEMS
item_descriptions = {
    "book":"It's an untouched copy of 'Windows 11: Inside Out'.",
    "keycard":"It's the IT intern's keycard.",
    "bin of mice":"A bin of real living mice...no that can't be right. Of course, it's just computer mice.",
    "workstation":"This workstation seems to be broken...maybe the intern was working on it...",
    "broken keyboard":"This keyboard is broken. It looks like someone smashed it on their desk in frustration...only the 'H' 'E' 'L' and 'P' keys remain. How strange...",
    "stick of ddr5 ram":"jackpot!",
    "usb drive":"A standard 64GB usb drive. What could be on it...?",
    "pamphlet":"This is the Fall 2026 course catalogue. Didn't know these were out yet.",
    "poster":"It's a poster for Student Activities this summer",
    # "":"",
    # "":"",
}

readable_items = {
    "sticky note":"The note reads, \"All assets must be signed out with date and technician name!\"",
    "book":"It seems to be a textbook about learning Windows 11. Truly fascinating.",
    "pamphlet":"This can't be right...HCC doesn't offer Ancient Sumerian as a language..."
}

item_aliases = {
    "ram":"stick of ddr5 ram",
    "ddr5":"stick of ddr5 ram",
    "ddr5 ram":"stick of ddr5 ram",
    "keyboard":"broken keyboard",
    "mice":"bin of mice",
    "drive":"usb drive",
    "note":"sticky note",
}
# PLAYER STATE
player = {
    "inventory":[],
    "sanity": 100,
    "visited_rooms":set()
}

# AREA ACCESS
locked_exits = {
    ("south hallway", "west")
}


# def intro(): #This will be some text, will use some functions to type characters one by one
#     print("""

# INTRODUCTION / STORY BACKGROUND TEXT HERE

# """)


def display_room(room_name, force_full=False):
    """display room description. force-full=True always shows full description"""
    room = rooms[room_name]

    # Only show "entered" message when actually moving to a room (not when using look)
    if not force_full:
        typewrite(f"You have entered the {room['name'].title()}\n")

    # Show description
    if force_full or room_name not in player["visited_rooms"]:
        typewrite(room["description"])
        player["visited_rooms"].add(room_name)
    else:
        print("[You've been here before]")

    # Always show items and exits
    if room['items']:
        if len(room['items']) == 1:
            typewrite(f"\nYou see a {room['items'][0]}.")
        else:
            all_but_last = ', a '.join(room['items'][:-1])
            typewrite(f"\nYou see a {all_but_last} and a {room['items'][-1]}.")
    typewrite(f"\nExits: {', '.join(room['exits'])}")

def resolve_alias(noun):
    return item_aliases.get(noun, noun)

def parse(raw):
    """Return (verb, noun) from raw input string"""
    parts=raw.lower().strip().split(None, 1)
    verb = parts[0] if parts else ""
    noun = parts[1] if len(parts) > 1 else ""
    for article in ("the ","a ", "an "):
        if noun.startswith(article):
            noun = noun[len(article):]
            break
    return verb, noun

def main():
    clear_screen()
    # Welcome Loop
    typewrite("Welcome to the Hagerstown Community College IT Help Desk Adventure!\nPress Enter to begin, or Q to quit\n")
    location = "it department"
    selection = input("> ").strip().lower()
    if selection == "q":
        return
    
    # Game Loop
    display_room(location)
    while True:
        try:
            raw = (input("> ")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            typewrite("\nGoodbye.")
            break

        if not raw:
            continue

        # Normalize multi-word verb phrases before parsing
        raw = raw.replace("pick up ", "take ", 1)
        raw = raw.replace("look at ", "examine ", 1)

        verb, noun = parse(raw)
        noun = resolve_alias(noun)

        # Check quit first
        if verb == "q" or verb == "quit" or verb == "exit":
            break

        # Check help
        elif verb == "help" or verb == "h":
            print("""
Available commands:
  go [direction] - Move in a direction (n/s/e/w also work)
  where - Show your current location and exits
  look (l) - Look around the current room
  examine [item] (x) - Examine an item closely
  read [item] - Read a document or note
  take [item] (get) - Pick up an item
  drop [item] - Drop an item from inventory
  inventory (i) - Check what you're carrying
  use [item] - Use an item
  help - Show this message
  quit (q) - Exit the game
""")
            continue

        # Transform verb synonyms (separate chain)
        if verb in ["n", "north"]: verb, noun = "go", "north"
        elif verb in ["s", "south"]: verb, noun = "go", "south"
        elif verb in ["e", "east"]: verb, noun = "go", "east"
        elif verb in ["w", "west"]: verb, noun = "go", "west"
        elif verb == "x": verb = "examine"
        elif verb == "l": verb = "look"
        elif verb == "get": verb = "take"
        elif verb == "walk": verb = "go"

        # Handle commands (separate chain starts here)
        if verb == "go":
            if noun in rooms[location]['exits']:
                if (location, noun) in locked_exits:
                    typewrite("The door is locked. Strange...doors aren't normally locked from the inside...")
                else:
                    location = rooms[location]['exits'][noun]
                    display_room(location)
            else:
                typewrite("You can't go that way")

        elif verb == "where":
            typewrite(f"You are in the {rooms[location]['name'].title()}.")
            typewrite(f"\nExits: {', '.join(rooms[location]['exits'])}")

        elif verb == "look":
            display_room(location, force_full=True)

        elif verb == "examine":
            if noun in rooms[location]["items"] or noun in player["inventory"]:
                if noun in item_descriptions:
                    typewrite(item_descriptions[noun])
                elif noun in readable_items:
                    typewrite("It says something...")
                else:
                    typewrite(f"There doesn't seem to be anything special about the {noun}.")
            else:
                typewrite(f"You don't see a {noun} here.")
                

        elif verb == "take":
            if noun in rooms[location]["items"]:
                rooms[location]["items"].remove(noun)
                player["inventory"].append(noun)
                typewrite(f"\nYou pick up the {noun}. It is now in your inventory.")
            else:
                typewrite(f"\nYou don't see a {noun} here")
        
        elif verb == "drop":
            if noun in player["inventory"]:
                player["inventory"].remove(noun)
                rooms[location]["items"].append(noun)
                typewrite(f"You drop the {noun}.")
            else:
                typewrite("You aren't carrying that.")
        
        elif verb == "read":
            if noun in rooms[location]["items"] or noun in player["inventory"]:
                if noun in readable_items:
                    typewrite(readable_items[noun])
                else:
                    typewrite("There's nothing written on this")
            else:
                typewrite(f"There's no {noun} here")

        elif verb == "use":
            if noun in player["inventory"] or noun in rooms[location]["items"]:
                #specific use cases here
                # if noun == {special}:
                    # some action
                typewrite("You can't use that right now.")
            else:
                typewrite("You don't have that item. ")

        elif verb == "inventory" or verb == "i":
            if player["inventory"]:
                typewrite(f"Inventory: \n{', \n'.join(player['inventory'])}")
            else:
                typewrite("You aren't carrying anything.")

        else:
            typewrite("Command not recognized")



if __name__ == "__main__":
    main()
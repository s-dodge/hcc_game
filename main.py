# HCC Text-Based Adventure game by Soren M. Dodge | 2026
import os

# WORLD
rooms = {
    "it department":{
        "name": "IT Department",
        "description": ("The bright, fluorescent lights here illuminate a tangle of old equipment...where did everyone go?"
        ),
        "exits": {"north": "storage", "east": "printing department", "south":"south hallway"},
        "items": ["DDR5 Ram", "Workstation", "Broken Keyboard", "Bin of Mice"]

    },
    "south hallway":{
        "name":"south hallway",
        "description":(""),
        "exits":{"north":"it department","west":"parking lot","east":"cafeteria", "south":"south stairwell"},
        "items":[]
    },
    "east hallway":{
        "name":"east hallway",
        "description":(""),
        "exits":{"west":"printing department", "south":"cafeteria"},
        "items":[]
    },
    "printing department":{
        "name":"printing department",
        "description":(""),
        "exits":{"east":"east hallway", "west":"it department"},
        "items":[]
    },
    "storage":{
        "name":"storage area",
        "description":(""),
        "exits":{"south":"it department"},
        "items":[]
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
    "pamphlet": "",
    "book":"",
    "keycard":""
}

# PLAYER STATE
player = {
    "inventory":[],
    "sanity": 100
}

# AREA ACCESS
locked_exits = {
    ("south hallway", "west")
}


# def intro(): #This will be some text, will use some functions to type characters one by one
#     print("""

# INTRODUCTION / STORY BACKGROUND TEXT HERE

# """)


def display_room(room_name):
    room = rooms[room_name]
    print(f"You are in the {room['name'].title()}")
    print(room["description"])
    print(f"Exits: {', '.join(room['exits'])}")

def parse(raw):
    """Return (verb, noun) from raw input string"""
    parts=raw.lower().strip().split(None, 1)
    verb = parts[0] if parts else ""
    noun = parts[1] if len(parts) > 1 else ""
    return verb, noun

def main():
    # Welcome Loop
    print("Welcome to the Hagerstown Community College IT Help Desk Adventure! Press Enter to begin, or Q to quit\n")
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
            print("\nGoodbye.")
            break

        if not raw:
            continue

        verb, noun = parse(raw)
        if verb == "q" or verb == "quit":
            break

        elif verb == "go":
            if noun in rooms[location]['exits']:
                if (location, noun) in locked_exits:
                    print("The door is locked.")
                else:
                    location = rooms[location]['exits'][noun]
                    display_room(location)
            else:
                print("You can't go that way")

        else:
            print("Command not recognized")














if __name__ == "__main__":
    main()
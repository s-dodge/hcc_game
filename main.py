# HCC Text-Based Adventure game by Soren M. Dodge | 2026
import os

# WORLD
rooms = {
    "it department":{
        "name": "IT Department",
        "description": ("The bright, fluorescent lights here illuminate a tangle of old equipment...where did everyone go?"
        ),
        "exits": {"north": "storage", "east": "printing department", "south":"south hallway"},
        "items": ["stick of ddr5 ram", "workstation", "broken keyboard", "bin of mice"]

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
    "book":"An untouched copy of 'Windows 11 Inside Out'.",
    "keycard":"The IT intern's keycard.",
    "bin of mice":"A bin of real living mice...no that can't be. Of course, it's just computer mice.",
    "workstation":"This workstation seems to be broken...maybe the intern was working on it...",
    "broken keyboard":"This keyboard is broken. It looks like someone smashed it on their desk in frustration.",
    "stick of ddr5 ram":"jackpot.",
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
    if room['items']:
        print(f"You see a {', a '.join(room['items'])}.")
    print(f"Exits: {', '.join(room['exits'])}")

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

        elif verb == "look":
            display_room(location)

        elif verb == "examine":
            if noun in item_descriptions:
                print(item_descriptions[noun])
            else:
                print("You don't see that here.")

        elif verb == "take":
            if noun in rooms[location]["items"]:
                rooms[location]["items"].remove(noun)
                player["inventory"].append(noun)
                print(f"\nYou pick up the {noun}. ")
                print(f"\nThe {noun} is now in your inventory. ")
            else:
                print("\nYou don't see that here")
        
        elif verb == "drop":
            if noun in player["inventory"]:
                player["inventory"].remove(noun)
                rooms[location]["items"].append(noun)
                print(f"You drop the {noun}.")
            else:
                print("You aren't carrying that.")

        elif verb == "inventory" or verb == "i":
            if player["inventory"]:
                print(f"Inventory: \n{', \n'.join(player['inventory'])}")
            else:
                print("You aren't carrying anything.")

        else:
            print("Command not recognized")



if __name__ == "__main__":
    main()
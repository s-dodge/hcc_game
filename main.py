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
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
}

readable_items = {
    "note":"",
    "email":"",
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


def display_room(room_name):
    room = rooms[room_name]
    print(f"You have entered the {room['name'].title()}")

    if room_name not in player["visited_rooms"]:
        print(room["description"])
        player["visited_rooms"].add(room_name)
    else:
        print("[You've been here before]")

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

        elif verb == "help" or verb == "h":
            print("""
Available commands:
  go [direction] - Move in a direction (n/s/e/w also work)
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
            if noun in rooms[location]["items"] or noun in player["inventory"]:
                if noun in item_descriptions:
                    print(item_descriptions[noun])
                else:
                    print(f"There doesn't seem to be anything special about the {noun}.")
            else:
                print(f"You don't see a {noun} here.")
                

        elif verb == "take":
            if noun in rooms[location]["items"]:
                rooms[location]["items"].remove(noun)
                player["inventory"].append(noun)
                print(f"\nYou pick up the {noun}. ")
                print(f"\nThe {noun} is now in your inventory. ")
            else:
                print(f"\nYou don't see a {noun} here")
        
        elif verb == "drop":
            if noun in player["inventory"]:
                player["inventory"].remove(noun)
                rooms[location]["items"].append(noun)
                print(f"You drop the {noun}.")
            else:
                print("You aren't carrying that.")
        
        elif verb == "read":
            if noun in rooms[location]["items"] or noun in player["inventory"]:
                if noun in readable_items:
                    print(readable_items(noun))
                else:
                    print("There's nothing written on this")
            else:
                print(f"There's no {noun} here")

        elif verb == "use":
            if noun in player["inventory"] or noun in rooms [location]["items"]:
                #specific use cases here
                # if noun == {special}:
                    # some action
                print("You can't use that right now.")
            else:
                print("You don't have that item. ")

        elif verb == "inventory" or verb == "i":
            if player["inventory"]:
                print(f"Inventory: \n{', \n'.join(player['inventory'])}")
            else:
                print("You aren't carrying anything.")

        else:
            print("Command not recognized")



if __name__ == "__main__":
    main()
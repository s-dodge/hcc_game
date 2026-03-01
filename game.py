from helpers import typewrite, clear_screen
import time

class Game:

    def __init__(self, player, rooms=None, locked_exits=None):
        self.player = player
        self.rooms = rooms if rooms is not None else {}
        self.locked_exits = locked_exits if locked_exits is not None else ()

    def parse(self, raw):
        """Return (verb, noun) from raw input string"""

        parts=raw.lower().strip().split(None, 1)
        verb = parts[0] if parts else ""
        noun = parts[1] if len(parts) > 1 else ""
        for article in ("the ","a ", "an "):
            if noun.startswith(article):
                noun = noun[len(article):]
                break
        return verb, noun
    
    def exit_labels(self, room):
        labels = []
        for direction, target_key in room.exits.items():
            target = self.rooms.get(target_key)
            if target and target.visited:
                labels.append(f"{direction} ({target.name})")
            else:
                labels.append(direction)
        return ', '.join(labels)

    def display_room(self, room, force_full=False):
        """display room description. force-full=True always shows full description"""

        # Only show "entered" message when actually moving to a room (not when using look)
        if not force_full:
            typewrite(f"You have entered the {room.name.title()}\n")

        # Show description
        if force_full or not room.visited:
            typewrite(room.get_description(self.player.sanity))
            room.visited = True
        else:
            print("[You've been here before]")

        # Always show items and exits
        if room.items:
            if len(room.items) == 1:
                typewrite(f"\nYou see a {room.items[0].name}.")
            else:
                all_but_last = ', a '.join(item.name for item in room.items[:-1])
                typewrite(f"\nYou see a {all_but_last} and a {room.items[-1].name}.")
        typewrite(f"\nExits: {self.exit_labels(room)}")

    def run(self):
        clear_screen()
        typewrite("Welcome to the Hagerstown Community College IT Help Desk Adventure!\nPress Enter to begin, or Q to quit\n")
        selection = input("> ").strip().lower()
        if selection == "q":
            return

        clear_screen()
        # --- Intro beats ---
        typewrite("The morning is gray and cold, and rain patters lightly on the roof of the building and runs in slow rivulets down the window of your office.\n\n")
        typewrite("A notification appears in the corner of your monitor. A ServiceDesk ticket has been assigned to you.\n\n")
        typewrite("The subject reads: \"Urgent - Password reset needed IN PERSON at the LRC. Can't get my work done. Send someone now if possible\"\n\n")
        typewrite("Better take a look...\n")
        time.sleep(2)
        clear_screen()

        # --- Cinematic room intro (first visit only) ---
        typewrite("You are in your office at HCC. You hear the hum of the heating system running behind the walls, and the boredom of the mid-semester is dragging the inexorable march of time down to a crawl \n")  
        typewrite("At least this ticket has come up so you can take a walk.\n")  # add as many typewrite() lines as you need
        typewrite("\n")  # delete unused lines when done

        # Mark as visited so returning here later shows the brief revisit version
        self.player.location.visited = True

        # Show items and exits to hand off to gameplay
        room = self.player.location
        if room.items:
            if len(room.items) == 1:
                typewrite(f"\nYou see a {room.items[0].name}.")
            else:
                all_but_last = ', a '.join(item.name for item in room.items[:-1])
                typewrite(f"\nYou see a {all_but_last} and a {room.items[-1].name}.")
        typewrite(f"\nExits: {self.exit_labels(room)}")

        while True:
            try:
                raw = input("> ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                typewrite("\nGoodbye.")
                break

            if not raw:
                continue

            # Normalize multi-word verb phrases
            raw = raw.replace("pick up ", "take ", 1)
            raw = raw.replace("look at ", "examine ", 1)

            verb, noun = self.parse(raw)

            if verb in ("q", "quit", "exit"):
                break

            elif verb in ("help", "h"):
                print("""
Available commands:
  go [direction] - Move in a direction (n/s/e/w also work)
  where          - Show your current location and exits
  look (l)       - Look around the current room
  examine (x)    - Examine an item closely
  read           - Read a document or note
  take (get)     - Pick up an item
  drop           - Drop an item from inventory
  inventory (i)  - Check what you're carrying
  use [item]            - Use an item
  use [item] on [item]  - Use an item on something
  leave          - Leave the current room
  help           - Show this message
  quit (q)       - Exit the game
""")
                continue

            # Verb synonyms
            if verb in ("n", "north"):   verb, noun = "go", "north"
            elif verb in ("s", "south"): verb, noun = "go", "south"
            elif verb in ("e", "east"):  verb, noun = "go", "east"
            elif verb in ("w", "west"):  verb, noun = "go", "west"
            elif verb == "x":            verb = "examine"
            elif verb == "l":            verb = "look"
            elif verb == "get":          verb = "take"
            elif verb == "walk":         verb = "go"

            # Dispatch
            if verb == "go":                    self.handle_go(noun)
            elif verb == "look":                self.handle_look()
            elif verb == "where":               self.handle_where()
            elif verb == "examine":             self.handle_examine(noun)
            elif verb == "take":                self.handle_take(noun)
            elif verb == "drop":                self.handle_drop(noun)
            elif verb == "read":                self.handle_read(noun)
            elif verb == "use":                 self.handle_use(noun)
            elif verb in ("inventory", "i"):    self.handle_inventory()
            elif verb == "leave":               self.handle_leave()
            else:                               typewrite("Command not recognized.")

    def handle_go(self, noun):
        room = self.player.location
        if noun in room.exits:
            if (room.name, noun) in self.locked_exits:
                typewrite("The door is locked. Strange...these doors aren't normally locked from the inside...")
            else:
                self.player.location = self.rooms[room.exits[noun]]
                self.display_room(self.player.location)
        else:
            typewrite("You can't go that way.")

    def handle_look(self):
        self.display_room(self.player.location, force_full=True)

    def handle_where(self):
        room = self.player.location
        typewrite(f"You are in the {room.name.title()}.")
        typewrite(f"\nExits: {self.exit_labels(room)}")

    def handle_examine(self, noun):
        room = self.player.location
        item = room.get_item(noun) or self.player.has_item(noun)
        if item:
            typewrite(item.get_description(self.player.sanity))
        else:
            typewrite(f"You don't see a {noun} here.")

    def handle_take(self, noun):
        room = self.player.location
        item = room.get_item(noun)
        if item:
            if item.takeable:
                room.items.remove(item)
                self.player.inventory.append(item)
                typewrite(f"\nYou pick up the {item.name}. It is now in your inventory.")
            else:
                reason = f", it's {item.untakeable_reason}" if item.untakeable_reason else ""
                typewrite(f"You can't take the {item.name}{reason}.")
        else:
            typewrite(f"\nYou don't see a {noun} here.")

    def handle_drop(self, noun):
        item = self.player.has_item(noun)
        if item:
            self.player.inventory.remove(item)
            self.player.location.items.append(item)
            typewrite(f"You drop the {item.name}.")
        else:
            typewrite("You aren't carrying that.")

    def handle_read(self, noun):
        room = self.player.location
        item = room.get_item(noun) or self.player.has_item(noun)
        if item:
            if item.is_readable:
                typewrite(item.read_text)
            else:
                typewrite("There's nothing written on this.")
        else:
            typewrite(f"There's no {noun} here.")

    def handle_use(self, noun):
        # Split "item on target"
        if " on " in noun:
            item_name, target_name = noun.split(" on ", 1)
            for article in ("the ", "a ", "an "):
                if target_name.startswith(article):
                    target_name = target_name[len(article):]
                    break
        else:
            item_name, target_name = noun, None

        item = self.player.has_item(item_name) or self.player.location.get_item(item_name)
        if not item:
            typewrite("You don't have that.")
            return

        target = self.player.location.get_item(target_name) if target_name else None
        if target_name and not target:
            typewrite(f"You don't see a {target_name} here.")
            return

        # --- Specific use cases ---

        if item.name == "power cable" and target and target.name == "workstation":
            if target.state == "powered":
                typewrite("It's already plugged in.")
            else:
                target.state = "powered"
                target.description = "The workstation hums quietly. The screen glows."  # update examine text
                self.player.inventory.remove(item)
                typewrite("You plug in the power cable. The workstation flickers on.")

        elif item.name == "usb drive" and target and target.name == "workstation":
            if target.state != "powered":
                typewrite("The workstation isn't on.")
            elif item.state == "used":
                typewrite("You've already read what's on this drive.")
            else:
                item.state = "used"
                typewrite("You insert the drive...\n\n")
                typewrite("""
some_file.txt
some_other_file.txt
""")  # replace with writing
                self.player.adjust_sanity(-20)

        else:
            typewrite("You can't use that here.")

    def handle_inventory(self):
        if self.player.inventory:
            items_str = ', \n'.join(item.name for item in self.player.inventory)
            typewrite(f"Inventory:\n{items_str}")
        else:
            typewrite("You aren't carrying anything.")

    def handle_leave(self):
        exits = self.player.location.exits
        if len(exits) == 1:
            self.handle_go(list(exits.keys())[0])
        else:
            typewrite(f"Which way? ({', '.join(exits)})")

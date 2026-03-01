from items import book, keycard, bin_of_mice, workstation, broken_keyboard, ddr5_ram, usb_drive, pamphlet, poster, sticky_note

class Room:

    def __init__(self, name, description, exits=None, items=None, visited=False, sanity_descriptions=None):
        self.name = name
        self.description = description
        self.exits = exits if exits is not None else {}
        self.items = items if items is not None else []
        self.visited = visited
        self.sanity_descriptions = sanity_descriptions if sanity_descriptions is not None else {}

    def get_description(self, sanity):
        for threshold in sorted(self.sanity_descriptions):
            if sanity <= threshold:
                return self.sanity_descriptions[threshold]
        return self.description

    def get_item(self, name):
        for item in self.items:
            if name == item.name or name in item.aliases:
                return item
        return None

    def __repr__(self):
        return f"Room({self.name})"


# --- Room instances ---

it_department = Room(
    name="it department",
    description="The bright, fluorescent lights here illuminate stacks of old equipment and tangles of Cat6 cable...\n\nThe lights flicker...\n\nWhere is everyone?",
    exits={"north": "storage", "east": "printing department", "south": "south hallway"},
    items=[ddr5_ram, book, workstation, broken_keyboard, bin_of_mice]
)

south_hallway = Room(
    name="south hallway",
    description="The hallway is empty. You see the parking lot to the west, the atrium to the east, and a stairwell to the south.",
    exits={"north": "it department", "west": "parking lot", "east": "atrium", "south": "south stairwell"}
)

east_hallway = Room(
    name="east hallway",
    description="The hallway is empty. Where is everyone...?",
    exits={"west": "printing department", "south": "atrium"}
)

printing_department = Room(
    name="printing department",
    description="The room is empty...Norm is usually here this time of day.",
    exits={"east": "east hallway", "west": "it department"},
    items=[pamphlet, poster]
)

storage = Room(
    name="storage",
    description="The walls are lined with shelves of assets...power cables, monitors, laptop bags, network switches, and unnameable layer 3 devices.",
    exits={"south": "it department"},
    items=[usb_drive, sticky_note, keycard]
)

atrium = Room(
    name="atrium",
    description="",
    exits={"north": "east hallway", "west": "south hallway", "south": "exit"}
)

parking_lot = Room(
    name="parking lot",
    description="",
    exits={"east": "south hallway"}
)

south_stairwell = Room(
    name="south stairwell",
    description="",
    exits={"north": "south hallway", "south": "exit"}
)

campus_exit = Room(
    name="exit",
    description="",
    exits={"north": "atrium", "south": "library", "east": "kepler theatre"}
)

library = Room(
    name="library",
    description="",
    exits={}
)

kepler_theatre = Room(
    name="kepler theatre",
    description="",
    exits={}
)

# --- World data ---

all_rooms = {
    "it department": it_department,
    "south hallway": south_hallway,
    "east hallway": east_hallway,
    "printing department": printing_department,
    "storage": storage,
    "atrium": atrium,
    "parking lot": parking_lot,
    "south stairwell": south_stairwell,
    "exit": campus_exit,
    "library": library,
    "kepler theatre": kepler_theatre,
}

locked_exits = {
    ("south hallway", "west")
}

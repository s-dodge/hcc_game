from items import *

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

# CPB BUILDING ROOMS

help_desk_office = Room(
    name="help desk office",
    description="Your office - a small room in the main IT department. It's cold in here today, and quiet.",
    exits={"east": "IT department"},
    items=[helpdesk_workstation, filing_cabinet, office_phone]
)

it_department = Room(
    name="IT department",
    description="The bright, fluorescent lights here illuminate stacks of old equipment and tangles of Cat6 cable...\n\nThe lights flicker...\n\nWhere is everyone...?\n\nYou see your office to the west, the storage room to the north, the printing department to the east, and the exit to the south.",
    sanity_descriptions={70:"Is that mold in the corners of the room...?\nAs you approach, you reach out and touch the wall. It's moss that's growing here on the walls", 40:"The walls seem to move like a breathing organism, and ichor seeps from cracks that have formed near the windows and doors"},
    exits={"west": "help desk office", "north": "storage room", "east": "printing department", "south": "south hallway"},
    items=[book, workstation, broken_keyboard, bin_of_mice]
)

south_hallway = Room(
    name="south hallway",
    description="The hallway is empty.\nYou see the parking lot to the west, the atrium to the east, and a stairwell to the south.",
    exits={"north": "IT department", "west": "parking lot", "east": "atrium", "south": "south stairwell"}
)

east_hallway = Room(
    name="east hallway",
    description="The hallway is empty. Where is everyone...?\nYou see the Printing Department to the west and the Atrium to the south",
    exits={"west": "printing department","south": "atrium", "east":"IT closet"},
    items=[badge_reader]
)

printing_department = Room(
    name="printing department",
    description="The room is empty...Norman is usually here this time of day.\nYou see the exit to the hallways to the east and the IT Department to the west",
    exits={"east": "east hallway", "west": "IT department"},
    items=[course_catalogue, poster]
)

storage_room = Room(
    name="storage room",
    description="The walls are lined with shelves of assets...power cables, monitors, laptop bags, network switches, and unnameable layer 3 devices.\n The only exit is south, back to the IT Department.",
    exits={"south": "IT department"},
    items=[power_cable, sticky_note, badge, asset_log]
)

atrium = Room(
    name="atrium",
    description="The lights in this large open area are flickering too...normally the natural light from the windows at the top of the room make this space inviting.\nWait...there are no lights here, just the windows...it's the sky that's flickering...\n\nNo that can't be right. It must have been a cloud passing the sun...",
    exits={"north": "east hallway", "west": "south hallway", "south": "exit"},
    sanity_descriptions={70:"Description_2", 40:"Description_3"}
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

it_closet = Room(
    name="IT closet",
    description="The air in the closet is heavy and stale. The walls are cluttered by racks and panels, and patch cables cross each other in tangles as switch lights blink on and off. Some of the patch cables look strange...\n\nAs you look closer, the cables are chunks of hair, and others look like plant roots or...fungal threads?",
    exits={"west": "east hallway"},
    items=[usb_drive]

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


# LRC BUILDING ROOMS

# main_room = room(
#     name="",
#     description="",
#     items=[],
#     exits={"north":"","south":"","east":"","west":""},

# )
# --- World data ---

all_rooms = {
    "help desk office": help_desk_office,
    "IT department": it_department,
    "south hallway": south_hallway,
    "east hallway": east_hallway,
    "printing department": printing_department,
    "storage room": storage_room,
    "atrium": atrium,
    "parking lot": parking_lot,
    "south stairwell": south_stairwell,
    "exit": campus_exit,
    "library": library,
    "kepler theatre": kepler_theatre,
    "IT closet": it_closet
}

locked_exits = {
    ("south hallway", "west"), #PARKING LOT
    ("south stairwell", "south"), #EXIT 
    ("atrium", "south"), #EXIT
    ("east hallway", "east") #IT CLOSET
}

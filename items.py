class Item:
    def __init__(self, name, description, aliases=None, read_text=None, takeable=True, untakeable_reason=None, usable=False, state=None, sanity_descriptions=None):
        self.name = name
        self.description = description
        self.aliases = aliases if aliases is not None else []
        self.read_text = read_text
        self.takeable = takeable
        self.untakeable_reason = untakeable_reason
        self.usable = usable
        self.state = state
        self.sanity_descriptions = sanity_descriptions if sanity_descriptions is not None else {}

    def get_description(self, sanity):
        for threshold in sorted(self.sanity_descriptions):
            if sanity <= threshold:
                return self.sanity_descriptions[threshold]
        return self.description

    @property
    def is_readable(self):
        return self.read_text is not None

    def __repr__(self):
        return f"Item({self.name})"


# --- Item instances ---

# HELP DESK OFFICE

helpdesk_workstation = Item(
    name="help desk workstation",
    description="Your computer. The ticket for the password reset in the Library is up on the screen.",
    takeable=False,
    untakeable_reason="too heavy",
    usable=False,
    aliases = ["workstation", "computer"]
)

filing_cabinet = Item(
    name="filing cabinet",
    description = "Your filing cabinet. Nothing in here but some old meeting notes.",
    takeable=False,
    untakeable_reason="too heavy",
)

# IT DEPARTMENT
book = Item(
    name="book",
    description="It's an untouched copy of 'Windows 11: Inside Out'.",
    read_text="It seems to be a textbook about learning Windows 11. Truly fascinating.\nThe pages are warm to the touch..."
)

bin_of_mice = Item(
    name="bin of mice",
    description="A bin of real living mice...no that can't be right. Of course, it's just computer mice.",
    aliases=["mice"]
)

workstation = Item(
    name="workstation",
    description="This workstation isn't functional...maybe the intern was working on it...",
    takeable=False,
    untakeable_reason="too heavy",
    usable=False
)

broken_keyboard = Item(
    name="broken keyboard",
    description="This keyboard is broken. It looks like someone smashed it on their desk in frustration...only the 'H' 'E' 'L' and 'P' keys remain. How strange...",
    aliases=["keyboard"]
)

ddr5_ram = Item(
    name="stick of ddr5 ram",
    description="jackpot!",
    aliases=["ram", "ddr5", "ddr5 ram"]
)

# STORAGE ROOM

power_cable = Item(
    name="power cable",
    description="A standard IEC power cable. These go missing all the time.",
    aliases=["cable"],
    usable=True
)

keycard = Item(
    name="keycard",
    description="It's the IT intern's keycard."
)

usb_drive = Item(
    name="usb drive",
    description="A standard 64GB usb drive. What could be on it...?",
    aliases=["drive", "usb"],
    usable=True
)

sticky_note = Item(
    name="sticky note",
    description="A yellow sticky note. There's writing on it.",
    aliases=["note"],
    read_text='The note reads, "All assets must be signed out with date and technician name"'
)



# PRINTING DEPARTMENT

pamphlet = Item(
    name="pamphlet",
    description="This is the Fall 2026 course catalogue. Didn't know these were out yet...",
    read_text="This can't be right...HCC doesn't offer Ancient Sumerian as a language..."
)

poster = Item(
    name="poster",
    description="It's a poster for Student Activities this summer\nThere's something strange about the students faces...you can't quite put your finger on it."
)

# ATRIUM

# EAST HALLWAY

# SOUTH HALLWAY

# LIBRARY

# KEPLER THEATRE


all_items = {
    "help desk workstation": helpdesk_workstation,
    "filing cabinet": filing_cabinet,
    "book": book,
    "bin of mice": bin_of_mice,
    "workstation": workstation,
    "broken keyboard": broken_keyboard,
    "stick of ddr5 ram": ddr5_ram,
    "power cable": power_cable,
    "keycard": keycard,
    "usb drive": usb_drive,
    "sticky note": sticky_note,
    "pamphlet": pamphlet,
    "poster": poster,
}



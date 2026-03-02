class Item:
    def __init__(self, name, description, sanity_name=None, aliases=None, read_text=None, takeable=True, untakeable_reason=None, usable=False, state=None, sanity_descriptions=None, sanity_read_texts=None):
        self.name = name
        self.description = description
        self.sanity_name = sanity_name if sanity_name is not None else ""
        self.aliases = aliases if aliases is not None else []
        self.read_text = read_text
        self.takeable = takeable
        self.untakeable_reason = untakeable_reason
        self.usable = usable
        self.state = state
        self.sanity_descriptions = sanity_descriptions if sanity_descriptions is not None else {}
        self.sanity_read_texts = sanity_read_texts if sanity_read_texts is not None else {}

    def get_description(self, sanity):
        for threshold in sorted(self.sanity_descriptions):
            if sanity <= threshold:
                return self.sanity_descriptions[threshold]
        return self.description
    
    def get_read_text(self, sanity):
        for threshold in sorted(self.sanity_read_texts):
            if sanity <= threshold:
                return self.sanity_read_texts[threshold]
        return self.read_text

    @property
    def is_readable(self):
        return self.read_text is not None

    def __repr__(self):
        return f"Item({self.name})"


# --- Item instances ---

# HELP DESK OFFICE

helpdesk_workstation = Item(
    name="help desk workstation",
    description="The computer screen glows in the dim office, casting an anaemic light into the room. The ticket for the password reset in the Library is up on the screen.",
    takeable=False,
    untakeable_reason="it's too awkward to carry",
    usable=False,
    aliases = ["workstation", "computer"]
)

filing_cabinet = Item(
    name="filing cabinet",
    description = "Your filing cabinet. Nothing in here but some old meeting notes.",
    takeable=False,
    untakeable_reason="it's too heavy",
    aliases=["cabinet", "drawers"]
)

# IT DEPARTMENT
book = Item(
    name="book",
    description="It's an untouched copy of 'Windows 11: Inside Out'. This could be useful...",
    read_text="It seems to be a textbook about learning Windows 11. Truly fascinating.\nThe pages are warm to the touch...",
    sanity_read_texts={70:"The cover reads 'Windows 11: Inside Out'...but the pages seem to be written in Latin.",40:"The grimoire writhes in your hands. The text is written in a language that predates human civilization. You understand every word."},
    sanity_name={40:"Ancient Grimoire"}
)

bin_of_mice = Item(
    name="bin of mice",
    description="A bin of real living mice...no that can't be right. Of course, it's just computer mice.",
    aliases=["mice"],
    sanity_descriptions={70:"A bin of real living mice...that's not right...", 40:"The bin contains a writhing mass of living mice - their tails knotted together as they chitter unceasingly."}
)

workstation = Item(
    name="workstation",
    description="This workstation won't power on...maybe the intern was working on it...",
    takeable=False,
    untakeable_reason="it's too awkward to carry",
    usable=False
)

broken_keyboard = Item(
    name="broken keyboard",
    description="This keyboard is broken. It looks like someone smashed it on their desk in frustration...only the 'H' 'E' 'L' and 'P' keys remain. How strange...",
    aliases=["keyboard"]
)

ddr3_ram = Item(
    name="stick of ddr3 ram",
    description="jackpot!",
    aliases=["ram", "ddr3", "ddr3 ram"]
)

# STORAGE ROOM

power_cable = Item(
    name="power cable",
    description="A standard IEC power cable. These go missing all the time.",
    aliases=["cable"],
    usable=True
)

badge = Item(
    name="badge",
    description="It's the IT intern's badge.",
    aliases=["id badge", "keycard"]
)

usb_drive = Item(
    name="usb drive",
    description="A standard 64GB usb drive. What could be on it...?",
    aliases=["drive", "usb"],
    usable=True
)

sticky_note = Item(
    name="sticky note",
    description="A yellow sticky note. It says something...",
    aliases=["note"],
    read_text='The note reads, "All assets must be signed out with date and technician name."',
    sanity_read_texts={70:"All assets must be signed out with a human soul and waiver of independent consciousness"}
)



# PRINTING DEPARTMENT

pamphlet = Item(
    name="pamphlet",
    description="This is the Fall 2026 course catalogue. Didn't know these were out yet...wonder what we're offering...",
    read_text="This can't be right...HCC doesn't offer Ancient Sumerian as a language...",
    aliases=["catalogue", "course catalogue"]
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
    "stick of ddr3 ram": ddr3_ram,
    "power cable": power_cable,
    "badge": badge,
    "usb drive": usb_drive,
    "sticky note": sticky_note,
    "pamphlet": pamphlet,
    "poster": poster,
}



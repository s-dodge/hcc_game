class Player:

    def __init__(self, location, sanity=100, inventory=None):
        self.location = location
        self.sanity = sanity
        self.inventory = inventory if inventory is not None else []

    def has_item(self, name):
        for item in self.inventory:
            if name == item.name or name in item.aliases:
                return item
        return None
    
    def adjust_sanity(self, amount):
        self.sanity = max(0, min(100, self.sanity + amount))

    def __repr__(self, sanity):
        return f"Player(sanity={self.sanity})"


    


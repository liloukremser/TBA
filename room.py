""" Define the Room class."""
class Room:
    """class room"""
    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = {}

    # Define the get_exit method.
    def get_exit(self, direction):
        """ Return the room in the given direction if it exists."""

        if direction in self.exits.keys():
            return self.exits[direction]
        return None

    def get_exit_string(self):
        """ Return a string describing the room's exits."""

        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_long_description(self):
        """ Return a long description of this room including exits."""

        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """retourne l'inventaire de la salle """

        if len(self.inventory) >= 1 or len(self.characters) >= 1:
            print("La pièce contient :")

        # Afficher uniquement les objets non cachés
            for item_name, item in self.inventory.items():
                if not item.hidden:
                    print(f" -{item_name} : {item.description}")

        # Afficher les personnages
            for character_name, character in self.characters.items():
                print(f" -{character_name} : {character.description}\n")

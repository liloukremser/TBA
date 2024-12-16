# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"


    def get_inventory(self):
        try :
            if len(self.inventory) >= 1: # on regarde si on a au moins un item
                print("La pièce contient :")
                for item_name, item in self.inventory.items() : #item balaye la liste
                    print(f"   -{item_name} : {item.description}")
            else:
                print("Il n'y a rien ici.")
        except Exception as e:
            print(f"Une erreur est survenue... ")
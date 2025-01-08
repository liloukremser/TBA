# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from beamer import Beamer
from character import Character

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher les salles visitées", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : permet de revenir dans la salle précédente", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : permet de voir les objets dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : permet de prendre un objet de la pièce et de le placer dans l'inventaire", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : permet de reposer un objet de la pièce et de l'enlever de l'inventaire", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : permet de voir l'inventaire", Actions.check, 0)
        self.commands["check"] = check
        use = Command("use", " : utilise un item de ton inventaire", Actions.use, 1)
        self.commands["use"] = use
        charge = Command("charge", " : charger un Beamer avec la salle actuelle", Actions.charge, 1)
        self.commands["charge"] = charge
        talk = Command("talk", " <someone> : parler avec un personnage", Actions.talk, 1)
        self.commands["talk"] = talk

        # Setup rooms

        vestiaire1 = Room("Vestiaire1", "dans le vestiaire.")
        self.rooms.append(vestiaire1)
        entrainement = Room("Entrainement", "dans la salle d'entraînement.")
        self.rooms.append(entrainement)
        bar = Room("Bar", "au bar.")
        self.rooms.append(bar)
        stade1 = Room("Stade1", "dans le premier stade.")
        self.rooms.append(stade1)
        village = Room("Village", "dans le village.")
        self.rooms.append(village)
        stade2 = Room("Stade2", "dans le stade intermédiaire.")
        self.rooms.append(stade2)
        vestiaire2 = Room("vestiaire2", "dans le second vestiaire.")
        self.rooms.append(vestiaire2)
        sdt = Room("Sdt", "dans la salle des trophées.")
        self.rooms.append(sdt)
        stade3 = Room("Stade3", "dans le stade final.")
        self.rooms.append(stade3)

        
        # Create exits for rooms

        vestiaire1.exits = {"N" : None, "E" : entrainement, "S" : None, "O" : bar, "U" : None, "D" : None}
        entrainement.exits = {"N" : None, "E" : None, "S" : stade1, "O" : vestiaire1, "U" : None, "D" : None}
        bar.exits = {"N" : None, "E" : vestiaire1, "S" : None, "O" : None, "U" : None, "D" : None}
        stade1.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : village, "D" : None}
        village.exits = {"N" : None, "E" : None, "S" : None, "O" : stade2, "U" : None, "D" : None}
        stade2.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : vestiaire2}
        vestiaire2.exits = {"N" : None, "E" : sdt, "S" : None, "O" : None, "U" : None, "D" : None}
        sdt.exits = {"N" : None, "E" : stade3, "S" : None, "O" : vestiaire2, "U" : None, "D" : None}
        stade3.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = vestiaire1

        #tous les items du jeu 
        
        raquette1 = Item("raquette1","blablabla", 2) 
        vestiaire1.inventory[raquette1.name] = raquette1
        raquette2 = Item("raquette2","blablabla", 2) 
        vestiaire2.inventory[raquette2.name] = raquette2
        raquette3 = Item("raquette3","blablabla", 2) 
        vestiaire2.inventory[raquette3.name] = raquette3
        
        # tous les PNJ du jeu 

        pnj1 = Character("pnj1","blabla",["oui c moi", "pouet pouet"])
        vestiaire1.characters[pnj1.name] = pnj1

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Faire bouger tous les PNJ avant chaque tour
            for room in self.rooms:
            # Faire une copie des clés car le dictionnaire peut être modifié pendant l'itération
                characters = list(room.characters.keys())
            for char_name in characters:
                room.characters[character_name].move()

            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word == '':
            print(f">")
        elif command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()

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

        loge = Room("Loge", "dans la loge.")
        self.rooms.append(loge)
        plateau = Room("Plateau", "sur le plateau de tournage.")
        self.rooms.append(plateau)
        tapis = Room("Tapis", "sur le tapis rouge.")
        self.rooms.append(tapis)
        hollywood = Room("Hollywood", "à Hollywood Boulevard.")
        self.rooms.append(hollywood)
        scene = Room("Scene", "sur la scène.")
        self.rooms.append(scene)
        theatre = Room("Theatre", "dans le théâtre.")
        self.rooms.append(theatre)
        toilette = Room("Toilette", "dans les toilettes.")
        self.rooms.append(toilette)
        cinema = Room("Cinema", "dans le cinéma.")
        self.rooms.append(cinema)
        fanz = Room("Fanz", "dans la fan zone.")
        self.rooms.append(fanz)

        
        # Create exits for rooms

        loge.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : theatre}
        plateau.exits = {"N" : scene, "E" : None, "S" : None, "O" : cinema, "U" : None, "D" : None}
        tapis.exits = {"N" : hollywood, "E" : scene, "S" : cinema, "O" : None, "U" : None, "D" : None}
        hollywood.exits = {"N" : None, "E" : theatre, "S" : tapis, "O" : None, "U" : None, "D" : None}
        scene.exits = {"N" : theatre, "E" : None, "S" : plateau, "O" : tapis, "U" : None, "D" : None}
        theatre.exits = {"N" : None, "E" : None, "S" : scene, "O" : hollywood, "U" : loge, "D" : None}
        toilette.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : cinema, "D" : None}
        cinema.exits = {"N" : tapis, "E" : plateau, "S" : fanz, "O" : None, "U" : None, "D" : toilette}
        fanz.exits = {"N" : cinema, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = fanz

        #tous les items du jeu 
        
        raquette1 = Item("raquette1","blablabla", 2) 
        loge.inventory[raquette1.name] = raquette1
        raquette2 = Item("raquette2","blablabla", 2) 
        loge.inventory[raquette2.name] = raquette2
        raquette3 = Item("raquette3","blablabla", 2) 
        loge.inventory[raquette3.name] = raquette3
        stylo = Item("stylo","youpi",2)
        fanz.inventory[stylo.name] = stylo
        
        # tous les PNJ du jeu 

        pnj1 = Character("pnj1",fanz,"blabla",["oui c moi", "pouet pouet"])
        fanz.characters[pnj1.name] = pnj1
        pnj2 = Character("pnj2",fanz,"blabla",["oui c moi", "pouet pouet"],False)
        fanz.characters[pnj2.name] = pnj2

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
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
             # Faire bouger tous les PNJ avant chaque tour
            for room in self.rooms:
            # Faire une copie des clés car le dictionnaire peut être modifié pendant l'itération
                characters = list(room.characters.values())
                for character in characters:
                    character.move()

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

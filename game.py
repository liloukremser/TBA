"""Description: Game class"""
#pylint: disable = line-too-long
#pas possible de les raccourcir

#pylint: disable = too-many-locals
#pylint: disable = too-many-statements
#impossible de raccourcir

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from conditions import Conditions


class Game:
    """Description: Game class"""
    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.condition = None
        self.talked_to_brad_pitt = False
        self.talked_to_melvin = False

    # Setup the game
    def setup(self):
        """ inventaire et initialisation de tout"""
        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction(N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher les salles visitées", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : permet de revenir dans la salle précédente", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : permet de voir les objets dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre un objet de la pièce et de le placer dans l'inventaire", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : reposer un objet dans la pièce et de l'enlever de l'inventaire", Actions.drop, 1)
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

        loge = Room("Loge", "dans la loge. On retrouve souvent des célébrités dans ce lieu privé. L'accès est souvent très restreint.")
        self.rooms.append(loge)
        plateau = Room("Plateau", "sur le plateau de tournage. Un des plus grands films d'action est en train d'être réalisé.")
        self.rooms.append(plateau)
        tapis = Room("Tapis", "sur le tapis rouge. Les costumes des stars sont toutes éblouissantes. On y voit plus rien à cause des flashs des paparazzis.")
        self.rooms.append(tapis)
        hollywood = Room("Hollywood", "à Hollywood Boulevard. L'une des allées les plus connues au monde.")
        self.rooms.append(hollywood)
        scene = Room("Scene", "sur la scène. La danse, la musique, le rythme, tout ce mélange dans ce lieu. ")
        self.rooms.append(scene)
        theatre = Room("Theatre", "dans le théâtre. La pièce est somptueuse mais les commères font rages")
        self.rooms.append(theatre)
        toilette = Room("Toilette", "dans les toilettes. Une envie pressante ?")
        self.rooms.append(toilette)
        cinema = Room("Cinema", "dans le cinéma. Une avant-première avec plusieurs fans du nouveau film sorti récemment.")
        self.rooms.append(cinema)
        fanz = Room("Fanz", "dans la fan zone. La salle est pleine, mais heureusement, il y a une connaissance dans la foule.")
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

        carnet = Item("carnet","c'est le carnet de Bastien avec les autographes qu'il a déjà", 2)
        cinema.inventory[carnet.name] = carnet
        autographez = Item("autographez","autographe de Zendaya", 2, hidden=True)
        loge.inventory[autographez.name.lower()] = autographez
        autographetr = Item("autographetr","autographe de The Rock", 2, hidden=True)
        hollywood.inventory[autographetr.name.lower()] = autographetr
        stylo = Item("stylo","ce stylo vous permet de faire signer les autographes",2, hidden = True)
        plateau.inventory[stylo.name] = stylo

        # tous les PNJ du jeu

        bradpitt = Character("bradpitt",plateau,"Un acteur séduisant à en perdre son but.",["Dommage pour toi ;)"])
        plateau.characters[bradpitt.name] = bradpitt
        therock = Character("therock",hollywood,"Un acteur intimidant mais avec le coeur sur la main.",["Tu veux me demander une chose crevette ?"],False)
        hollywood.characters[therock.name] = therock
        zendaya = Character("zendaya",loge,"Actrice aimée de tous",["Vous êtes adorable, merci pour votre soutient."],False)
        loge.characters[zendaya.name] = zendaya
        bastien = Character("bastien",fanz,"un fan des grandes stars",["J'ai une mission pour toi ! Mais d'abord trouve mon carnet dans le cinéma puis reviens me parler. ", "Il me faut absolument les autographes des stars de Hollywood :) Ramène-les moi ! "],False)
        fanz.characters[bastien.name] = bastien
        melvin = Character("melvin",toilette,"l'hystérique des toilettes",["Donne moi ton carnet !!!!!"],False)
        toilette.characters[melvin.name] = melvin
        realisateur = Character("realisateur",toilette,"il est très strict pour que tout soit en ordre mais il est indispensable dans le bon déroulement des choses.",["Pour réussir il te faut absolument un stylo, regarde autour de toi."],False)
        plateau.characters[realisateur.name] = realisateur
        paparazzi = Character("paparazzi",toilette,"C'est un vrai espion, il sait tout sur tout.",["J'ai vu The Rock près de Hollywood Boulevard."],False)
        tapis.characters[paparazzi.name] = paparazzi
        commere = Character("commere",theatre,"Elle est à l'affut du dernier potin mais elle est très fourbe.",["Il parait que la personne dans les toilettes est une star très connue sous couverture."],False)
        theatre.characters[commere.name] = commere



        self.condition = Conditions(self)

    # Play the game
    def play(self):
        """ jeu """
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
            end_message = self.condition.check_conditions()
            if end_message:
                self.finished = True
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """ exécution des commandes"""
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
        """ accueil du joueur """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())


def main():
    """Create a game object and play the game"""
    Game().play()


if __name__ == "__main__":
    main()

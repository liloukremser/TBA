# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        #direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        #player.move(direction)
        #return True

# Si le mot entré n'appartient pas à la liste de mots valide 
        exits = {"N": "N", "NORD": "N", "E" : "E", "EST":"E","S" : "S", "SUD" : "S","O" : "O","OUEST" : "O", "U" : "U","UP":"U","D" : "D", "DOWN":"D"}
        direction = list_of_words[1]
        direction = direction.upper()

        if direction in exits.keys():
            direction = exits[direction]
            player.move(direction)

        else:
            print("\nLa direction donnée n'existe pas.")
        
        return True


    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def history(game,list_of_words, number_of_parameters): 
        if len(list_of_words) != number_of_parameters +1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return game.player.get_history()
            

    def back(game,list_of_words, number_of_parameters):
        """attention à rajouter une partie pour que le joueur ne puisse pas revenir en arrière si la sortie est à sens unique"""
        if len(list_of_words) != number_of_parameters +1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return game.player.back()


    def inventory(game,list_of_words, number_of_parameters): 
        if len(list_of_words) != number_of_parameters +1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return game.player.get_inventory()

    
    def look(game, list_of_words, number_of_parameters): 
        if len(list_of_words) != number_of_parameters +1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return game.player.current_room.get_inventory()



    

    def take(game, list_of_words, number_of_parameters):

        #on vérifie si le nombre de paramètre est correct 
        if len(list_of_words) != number_of_parameters +1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # on vérifie que l'item à prendre a été spécifié 
        item_name = list_of_words[1]
        current_room = game.player.current_room

        #chercher l'item dans l'inventaire de la pièce actuelle
        
        if item_name in current_room.inventory:
            item = current_room.inventory[item_name]
            #ajouter l'item à l'inventaire du joueur
            if game.player.add(item):
            #retirer l'item à l'inventaire de la pièce
                current_room.inventory.pop(item_name)
                print(f"Vous avez pris {item_name}.")
                return True
            else:
                print(f"Vous ne pouvez pas orendre {item_name}, poids maximum dépassé.")
                return False
        else:
            print(f"L'item n'est pas dans cette pièce.")
            return False

    def drop(game, list_of_words, number_of_parameters):
         #on vérifie si le nombre de paramètre est correct 
        if len(list_of_words) != number_of_parameters +1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # on vérifie que l'item à prendre a été spécifié 
        item_name = list_of_words[1]
        current_room = game.player.current_room

        #chercher l'item dans l'inventaire de la pièce actuelle
        
        if item_name in game.player.inventory:
            item = game.player.inventory[item_name]
            #ajouter l'item à l'inventaire du joueur 
            #retirer l'item à l'inventaire de la pièce
            current_room.inventory[item_name] = item
            game.player.remove(item_name)
            print(f"Vous avez déposé {item_name}.")
            return True
        else:
            print(f"{item_name} n'est pas dans votre inventaire")
            return False

    def check(game, list_of_words, number_of_parameters):
         #on vérifie si le nombre de paramètre est correct 
        if len(list_of_words) != number_of_parameters +1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        return game.player.get_inventory()
        
    def use(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        item_name = list_of_words[1]
        item = game.player.inventory.get(item_name, None)
        
        if item_name in game.player.inventory:
            if isinstance(item, Beamer):
                return item.use(game)
        else:
            print(f"L'objet '{item_name}' n'est pas utilisable ou n'est pas un Beamer.")
            return False

    def charge(game, list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        item_name = list_of_words[1]
        item = game.player.inventory.get(item_name, None)
        print(item_name)
        
        if item_name in game.player.inventory:
            item.charge(game.player.current_room)
            return True
        else:
            print(f"L'objet '{item_name}' ne peut pas être chargé ou n'est pas un Beamer.")
            return False

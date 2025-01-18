""" Module contenant les conditions de victoire et de défaite du jeu. """
import time

class Conditions:
    """ Classe représentant les conditions de victoire et de défaite du jeu. """
    def __init__(self, game):
        self.game = game

    def check_victory(self):
        """
        Vérifie si le joueur a gagné en ramenant les autographes 
        de Zendaya et The Rock dans la fan zone.
        Returns:
            bool: True si le joueur a gagné, False sinon.
        """
        required_items = ["autographez", "autographetr"]
        current_room = self.game.player.current_room

        if current_room.name.lower() == "fanz":
            if all(item.lower() in [i.name.lower() for i in self.game.player.inventory.values()] for item in required_items):
                messages = [
                    f"Félicitations {self.game.player.name}, vous avez gagné en ramenant les autographes de Zendaya et The Rock dans la fan zone!",
                    "Vous avez accompli toutes les quêtes.",
                    "Votre aventure à Hollywood est un succès.",
                    "À bientôt pour de nouvelles aventures !",
                    "Merci d'avoir joué!"
                ]
                print_with_delay(messages)
                self.game.finished = True
                return True
        return False

    def check_defeat(self):
        """
        Vérifie si le joueur a perdu en parlant à Brad Pitt ou à Melvin.
        Returns:
            bool: True si le joueur a perdu, False sinon.
        """
        current_room = self.game.player.current_room

        if self.game.talked_to_brad_pitt:
            messages = [
                f"Désolé {self.game.player.name}, vous avez perdu en parlant à Brad Pitt.",
                "Brad Pitt vous a reconnu et a appelé la sécurité.",
                "La sécurité vous a retiré tout ce que vous possédez..."
            ]
            print_with_delay(messages)
            self.game.finished = True
            return True

        if "melvin" in current_room.characters and self.game.talked_to_melvin:
            messages = [
                f"Désolé {self.game.player.name}, vous avez perdu en parlant à Melvin.",
                "Melvin vous a volé votre carnet d'autographes et est parti en courant comme un gnôme malicieux !",
                "Vous ne pouvez plus collecter d'autographes..."
            ]
            print_with_delay(messages)
            self.game.finished = True
            return True

        return False
    def check_conditions(self):
        """
        Vérifie les conditions de victoire et de défaite du jeu.
        Returns:
            str: Message de victoire ou de défaite, None sinon.
        """
        victory_message = self.check_victory()
        if victory_message:
            return "Victoire"

        defeat_message = self.check_defeat()
        if defeat_message:
            return "Défaite"

        return None

def print_with_delay(messages, delay=2.0):
    """ 
    Affiche une liste de messages avec un délai entre chaque message.
    Args:
        messages (list): Liste des messages à afficher.
        delay (float): Délai entre chaque message.
    """
    for message in messages:
        print(message)
        time.sleep(delay)

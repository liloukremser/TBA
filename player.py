# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        self.history.append(next_room)
        print(self.current_room.get_long_description())
        self.get_history()
        return True

    def get_history(self) :
        """Créer un historique pour permettre au joueur de savoir où il en est dans le jeu
        on fait un try car si la liste est vide, il affiche une liste vide (pas esthétique)"""
        try : 
            if len(self.history) > 1: # on regarde si on a visité une pièce au minimum
                print("Vous êtes déjà allés : \n   -dans le vestiaire.")
                for room in self.history[:-1] : #room balaye la liste
                    print(f"   -{room.description}")
            else: 
                print("Vous avez visité le vestiaire.")
        except Exception as e: 
            print("Une erreur est survenue... ")
                
        
    def back(self) : 
        try :
            if len(self.history) > 1 :
                self.history.pop()
                self.current_room = self.history[-1]
                print(self.current_room.get_long_description())
                self.get_history()
                return True
            else :
                print("Pas de retour en arrière possible.")
                return False
        
        except Exception as e :
            print(f" Une erreur innatendue s'est produite lors du retour en arrière : {e}")
            return False
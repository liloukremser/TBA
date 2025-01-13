import random
from player import Player
from config import DEBUG

class Character(Player):
    def __init__(self, name, current_room, description, msgs, can_move=True):
        super().__init__(name, current_room)
        self.description = description 
        self.msgs = msgs 
        self.can_move = can_move

    def __str__(self):
        return f"{self.name} : {self.description}, dans la salle :{self.current_room}/n{self.msgs}" 

    def move(self):
        # Une chance sur deux de se déplacer (0 ou 1)
        if random.randint(0, 1) == 1 and self.can_move:
            # Récupérer les sorties possibles (non None) depuis la salle actuelle
            possible_exits = [room for direction, room in self.current_room.exits.items() if room is not None]
            
            # S'il y a des sorties possibles
            if possible_exits:
                # Choisir une salle au hasard parmi les sorties possibles
                new_room = random.choice(possible_exits)
                
                # Retirer le PNJ de la salle actuelle
                del self.current_room.characters[self.name]
                
                # Mettre à jour la salle actuelle
                self.current_room = new_room
                if DEBUG :
                    print(f"{self.name} a bougé vers {self.current_room.name}")
                
                # Ajouter le PNJ dans la nouvelle salle
                new_room.characters[self.name] = self
                
                return True
        
        return False

    def get_msg(self):
        # Si la liste des messages est vide, on remet tous les messages de l'historique
        if not self.msgs:
            self.msgs = self.msg_history
            self.msg_history = []
            
        if self.msgs:
            # Retire et retourne le premier message de la liste
            current_msg = self.msgs.pop(0)
            # Ajoute ce message à l'historique
            self.msgs.append(current_msg)
            return current_msg
        
        return "tg"  # Au cas où il n'y aurait aucun message
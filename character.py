
class Character:
    def __init__(self, name, description, msgs):
        self.name = name
        self.current_room = None
        self.description = description 
        self.msgs = msgs 

    def __str__(self):
        return f"{self.name} : {self.description}, dans la salle :{self.current_room}/n{self.msgs}" 

    def move():
        # Une chance sur deux de se déplacer (0 ou 1)
        if random.randint(0, 1) == 1:
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
            self.msg_history.append(current_msg)
            return current_msg
        
        return "tg"  # Au cas où il n'y aurait aucun message
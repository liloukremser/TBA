class Item : 

    def __init__(self, name, description, weight):
        self.name = name 
        self.description = description 
        self.weight = int 

#tous les items du jeu 

    raquette = Item("raquette","blablabla", 2)

    def __str__(self):
        return self.name 
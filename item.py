""" classe des items """ 
class Item:
    """
    Classe représentant un item dans le jeu.
    
    Attributes:
        name (str): Nom de l'item
        description (str): Description de l'item
        weight (int): Poids de l'item en grammes
        hidden (bool): État de visibilité de l'item (True si caché, False si visible)
    """

    def __init__(self, name, description, weight, hidden=False):
        """
        Initialise un nouvel item.
        
        Args:
            name (str): Nom de l'item
            description (str): Description de l'item
            weight (int): Poids de l'item en grammes
            hidden (bool, optional): État initial de visibilité. Defaults to False.
        """
        self.name = name.lower()  # Stocke le nom en minuscules pour la cohérence
        self.description = description
        self.weight = weight
        self.hidden = hidden

    def __str__(self):
        """
        Retourne une représentation textuelle de l'item.
        
        Returns:
            str: Description formatée de l'item
        """
        if self.hidden:
            return ""  # Ne retourne rien si l'item est caché
        return f"{self.name} : {self.description} ({self.weight} g)"

    def hide(self):
        """
        Cache l'item.
        
        Returns:
            bool: True si l'opération a réussi
        """
        self.hidden = True
        return True

    def reveal(self):
        """
        Rend l'item visible.
        
        Returns:
            bool: True si l'opération a réussi
        """
        self.hidden = False
        return True

    def is_hidden(self):
        """
        Vérifie si l'item est caché.
        
        Returns:
            bool: True si l'item est caché, False sinon
        """
        return self.hidden

    def get_weight(self):
        """
        Retourne le poids de l'item.
        
        Returns:
            int: Poids de l'item en grammes
        """
        return self.weight

    def get_name(self):
        """
        Retourne le nom de l'item.
        
        Returns:
            str: Nom de l'item
        """
        return self.name

    def get_description(self):
        """
        Retourne la description de l'item.
        
        Returns:
            str: Description de l'item, ou chaîne vide si l'item est caché
        """
        if self.hidden:
            return ""
        return self.description

    def get_inventory_items(self):
        """Retourne la liste des items visibles dans l'inventaire."""
        visible_items = []
        for item in self.items.values():
            if not item.hidden:  # Vérifie si l'item n'est pas caché
                visible_items.append(str(item))
        return visible_items

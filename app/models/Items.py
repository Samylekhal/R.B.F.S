class Items:

    def __init__(self, name = "Aucun", id = 0, description = "aucun effet", item_category = "aucune catégorie"):
        self.name = name
        self.id = id
        self.description = description
        self.item_category = item_category

    def __str__(self):
        return f"{self.name} (#{self.id}) catégorie: {self.item_category}\neffet: {self.description}"
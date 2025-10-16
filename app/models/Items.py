class Items:

    def __init__(self, name, id, description, item_category):
        self.name = name
        self.id = id
        self.description = description
        self.item_category = item_category

    def __str__(self):
        return f"{self.name} (#{self.id}) catégorie: {self.item_category}\neffet: {self.description}"
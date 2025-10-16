class Abilities:

    def __init__(self,name,id, description):
        self.name = name
        self.id = id
        self.description = description

    def __str__(self):
        return f"{self.name} (#{self.id}) : {self.description}" 




class BasePokemon:
    def __init__(self, name, id, types, weight, height, stats, abilities, movepool):
        self.name = name
        self.id = id
        self.types = types              
        self.weight = weight
        self.height = height
        self.stats = stats              
        self.abilities = abilities          
        self.movepool = movepool        

    def __str__(self):
        return f"{self.name.title()} (#{self.id}) — Types: {', '.join(self.types)}"

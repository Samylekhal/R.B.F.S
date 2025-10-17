class Natures:
    
    def __init__(self, name, id, INCstat, DECstat):

        self.name = name
        self.id = id
        self.INCstat = INCstat
        self.DECstat = DECstat

    def get_nature_modifier(self):
        stats_modifiers = {
            "attack": 1.0,
            "defense": 1.0,
            "special-attack": 1.0,
            "special-defense": 1.0,
            "speed": 1.0
        }

        if self.INCstat in stats_modifiers:
            stats_modifiers[self.INCstat] = 1.1
        if self.DECstat in stats_modifiers:
            stats_modifiers[self.DECstat] = 0.9
    
        return stats_modifiers

    def __str__(self):
        return f"{self.name} (#{self.id}) | +: {self.INCstat} -: {self.DECstat}"
class Natures:

    def __init__(self, name):
        self.name = name
        self.id = None
        self.nature_modifier = self.get_nature_modifier(name)
        self.INCstat = self.get_INCstat()
        self.DECstat = self.get_DECstat()

    def get_nature_modifier(self, name):
        stats_modifiers = {
            "attack": 1.0,
            "defense": 1.0,
            "special-attack": 1.0,
            "special-defense": 1.0,
            "speed": 1.0
        }
        match name:
            case "bold":
                stats_modifiers["attack"] = 0.9 
                stats_modifiers["defense"] = 1.1
            case "modest":
                stats_modifiers["attack"] = 0.9
                stats_modifiers["special-attack"] = 1.1
            case "calm":
                stats_modifiers["attack"] = 0.9
                stats_modifiers["special-defense"] = 1.1
            case "timid":
                stats_modifiers["attack"] = 0.9
                stats_modifiers["speed"] = 1.1
            case "lonely":
                stats_modifiers["defense"] = 0.9
                stats_modifiers["attack"] = 1.1
            case "mild":
                stats_modifiers["defense"] = 0.9
                stats_modifiers["special-attack"] = 1.1
            case "gentle":
                stats_modifiers["defense"] = 0.9
                stats_modifiers["special-defense"] = 1.1
            case "hasty":
                stats_modifiers["defense"] = 0.9
                stats_modifiers["speed"] = 1.1
            case "adamant":
                stats_modifiers["special-attack"] = 0.9
                stats_modifiers["attack"] = 1.1
            case "impish":
                stats_modifiers["special-attack"] = 0.9
                stats_modifiers["defense"] = 1.1  
            case "careful":
                stats_modifiers["special-attack"] = 0.9
                stats_modifiers["special-defense"] = 1.1
            case "rash":
                stats_modifiers["special-defense"] = 0.9
                stats_modifiers["special-attack"] = 1.1
            case "jolly":
                stats_modifiers["special-attack"] = 0.9
                stats_modifiers["speed"] = 1.1
            case "naughty":
                stats_modifiers["special-defense"] = 0.9
                stats_modifiers["attack"] = 1.1
            case "lax":
                stats_modifiers["special-defense"] = 0.9
                stats_modifiers["defense"] = 1.1
            case "naive":
                stats_modifiers["special-defense"] = 0.9
                stats_modifiers["speed"] = 1.1
            case "brave":
                stats_modifiers["speed"] = 0.9
                stats_modifiers["attack"] = 1.1
            case "relaxed":
                stats_modifiers["speed"] = 0.9
                stats_modifiers["defense"] = 1.1
            case "quiet":
                stats_modifiers["speed"] = 0.9
                stats_modifiers["special-attack"] = 1.1
            case "sassy":
                stats_modifiers["speed"] = 0.9
                stats_modifiers["special-defense"] = 1.1
            case _:
                pass  # nature neutre, pas de modifications
        return stats_modifiers

    def get_INCstat(self):
        for stat, modifier in self.nature_modifier.items():
            if modifier > 1.0:
                return stat
        return "null"
    
    def get_DECstat(self):
        for stat, modifier in self.nature_modifier.items():
            if modifier < 1.0:
                return stat
        return "null"
    
    def __str__(self):
        return f"{self.name} (#{self.id}) | +: {self.INCstat} -: {self.DECstat}"
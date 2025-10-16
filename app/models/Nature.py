class Natures:
    
    def __init__(self, name, id, INCstat, DECstat):

        self.name = name
        self.id = id
        self.INCstat = INCstat
        self.DECstat = DECstat
    
    def __str__(self):
        return f"{self.name} (#{self.id}) | +: {self.INCstat} -: {self.DECstat}"
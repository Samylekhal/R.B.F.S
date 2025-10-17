class Moves:

    def __init__(self,name,id,damageclass,type, Basepower,PP, accuracy, description):

        self.name = name
        self.id = id
        self.damageclass = damageclass
        self.type = type
        self.Basepower = Basepower
        self.PP = PP
        self.PPmax = round(PP * 1.6)
        self.accuracy = accuracy
        self.description = description
        

    def __str__(self):
        return f"{self.name} (#{self.id})\nType: {self.type} |Damageclass: {self.damageclass} |Puissance: {self.Basepower} | PP: {self.PP} | Précision: {self.accuracy}\nDescription:\n{self.description}"
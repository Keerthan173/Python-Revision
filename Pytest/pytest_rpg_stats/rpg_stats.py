def generate_strength():
    return 5

def is_stat_valid(stat_value):
    return 1<=stat_value<=10

class Character:
    def __init__(self,strength,intelligence,dexterity):
        self.strength=strength
        self.intelligence=intelligence
        self.dexterity=dexterity
    
    def get_combat_readiness(self):
        return self.strength+self.dexterity
    
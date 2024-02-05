class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return f"Weapon(name={self.name}, damage={self.damage})"


class Spell:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def __repr__(self):
        return f"Spell(name={self.name}, effect={self.effect})"

class Key:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Key(name={self.name}, description={self.description})"

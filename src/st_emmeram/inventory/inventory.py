from src.st_emmeram.inventory.items import Weapon, Spell, Key
import logging

ModuleLogger = logging.getLogger(__name__)


class Inventory:

    def __init__(self):
        self.slots = {'weapons': [], 'spells': [], 'key': []}
        self.max_slots = {'weapons': 2,
                          'spells': 3,
                          'key': 1}

    def add_item(self, item):
        if isinstance(item, Weapon) and len(self.slots['weapons']) < self.max_slots['weapons']:
            self.slots['weapons'].append(item)
        elif isinstance(item, Spell) and len(self.slots['spells']) < self.max_slots['spells']:
            self.slots['spells'].append(item)
        elif isinstance(item, Key) and len(self.slots['key']) < self.max_slots['key']:
            self.slots['key'].append(item)
        else:
            ModuleLogger.error("Cannot add item, either due to type mismatch or slot limitations.")

    def remove_item(self, item_type, item=None):
        if item_type in self.slots:
            if item in self.slots[item_type]:
                self.slots[item_type].remove(item)
            else:
                ModuleLogger.error("Item not found.")
        else:
            ModuleLogger.error("Invalid item type.")

    def check_inventory(self):
        return self.slots

    def render_inventory(self):
        pass

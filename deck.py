import genanki
from note import Note
import random

class Deck:
    def __init__(self, group_num):
        self.deck = genanki.Deck(
            random.randrange(1 << 30, 1 << 31),
            f'GRE Vocab Group {group_num}'
        )

    def add_note(self, note):
        self.deck.add_note(note)
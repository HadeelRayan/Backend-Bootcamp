import random
from dataclasses import dataclass, field
from typing import List


@dataclass
class Player:
    name: str
    visited_places: List[str] = field(default_factory=list)
    favorite_weapons: List[str] = field(default_factory=list)
    is_assassin: bool = False

    def visit_places(self, places):
        self.visited_places = random.sample(places, random.randint(1, 3))



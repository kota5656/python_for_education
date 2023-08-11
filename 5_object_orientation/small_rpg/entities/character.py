from typing import Optional
from dataclasses import dataclass

@dataclass
class CharacterData():
    name: str
    level: int
    hp: int = 0
    mp: int = 0
    tp: int = 0
    max_hp: int
    max_mp: int
    max_tp: int
    patk: int
    pdef: int
    matk: int
    mdef: int
    speed: int
    patk_rank: int = 0
    pdef_rank: int = 0
    matk_rank: int = 0
    mdef_rank: int = 0
    speed_rank: int = 0
    hit_rank: int = 0
    avoid_rank: int = 0

class Character():
    def __init__(self, character_data: CharacterData) -> None:
        self.character_data = character_data
    
    def damage_hp(self, damage) -> None: 
        self.character_data["hp"] = min(0, self.character_data["hp"]-damage)
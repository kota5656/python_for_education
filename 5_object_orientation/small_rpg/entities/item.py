from typing import List, TypedDict

class MedicalKit(TypedDict):
    hp: int
    mp: int
    tp: int

class Equipment(TypedDict):
    patk: int
    pdef: int
    matk: int
    mdef: int
    speed: int
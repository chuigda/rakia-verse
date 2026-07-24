from typing import List

from .kind import Terrain, DamageKind
from .capability import Capability


class Species:
    """
    种族模板，定义基础生命值、敏捷、移动力、防御及抗性。
    """

    def __init__(self,
                 id: str,
                 base_hp: int,
                 level_hp: int,
                 hp_regen: int,
                 agility: int,
                 movement: List[float],
                 defence: List[float],
                 resistance: List[float],
                 capabilities: List[Capability]):
        assert len(movement) == len(Terrain)
        assert len(defence) == len(Terrain)
        assert len(resistance) == len(DamageKind)

        self.id = id
        self.base_hp = base_hp
        self.level_hp = level_hp
        self.hp_regen = hp_regen
        self.agility = agility
        self.movement = movement
        self.defence = defence
        self.resistance = resistance
        self.capabilities = capabilities

from typing import List

from .kind import Terrain, DamageKind
from .capability import Capability


class Species:
    """
    种族模板，定义基础生命值、敏捷、移动力、防御及抗性。

    Attributes:
        id: 种族唯一标识符。
        base_hp: 基础生命值。
        level_hp: 每级生命值增长。
        hp_regen: 每回合生命恢复量。
        agility: 敏捷值，决定行动顺序。
        movement: 各地形移动力消耗列表。
        defence: 各地形防御修正列表。
        resistance: 各伤害类型抗性列表。
        capabilities: 种族自带能力列表。
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
        """初始化种族属性，包含HP、敏捷、地形移动/防御及伤害抗性。"""
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

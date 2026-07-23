from typing import List

from .coin import Coin
from .species import DamageKind


class Capability:
    """
    单位能力基类。

    Attributes:
        type: 能力类型标识。
        id: 能力唯一 ID。
        prerequests: 前置能力列表。
        xp_cost: 学习所需经验值，`None` 表示不可通过经验学习。
        coin_cost: 学习所需货币花费。
    """

    def __init__(self,
                 type: str,
                 id: str,
                 prerequests: List[Capability],
                 xp_cost: int | None,
                 coin_cost: Coin | None):
        """初始化能力，设置类型、ID、前置需求及花费。"""
        self.type = type
        self.id = id
        self.prerequests = prerequests
        self.xp_cost = xp_cost
        self.coin_cost = coin_cost

    def learnable(self) -> bool:
        """判断该能力是否可学习（所有前置已满足且有经验花费）。"""
        return all(p.learnable() for p in self.prerequests) and (self.xp_cost is not None)


class AttackCapability(Capability):
    """
    攻击类能力，包含近战/远程攻击属性。

    Attributes:
        ranged: 是否为远程攻击。
        strike: 命中修正值。
        damage: 伤害值。
        damage_type: 伤害类型。
        specials: 特殊效果列表。
    """

    def __init__(self,
                 id: str,
                 prerequests: List[Capability],
                 xp_cost: int | None,
                 coin_cost: Coin | None,
                 ranged: bool,
                 strike: int,
                 damage: int,
                 k_damage: DamageKind,
                 specials: List[str]):
        """初始化攻击能力，包含命中、伤害、伤害类型及特殊效果。"""
        type_str = "attack/" + ("ranged" if ranged else "melee")
        super().__init__(type_str, id, prerequests, xp_cost, coin_cost)

        self.ranged = ranged
        self.strike = strike
        self.damage = damage
        self.damage_type = k_damage
        self.specials = specials

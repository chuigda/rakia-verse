from typing import List
from abc import abstractmethod
from .coin import Coin
from .species import DamageKind
from .unit import Unit


class Capability:
    """
    单位能力基类。
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

    @property
    def learnable(self) -> bool:
        """判断该能力是否可学习（所有前置已满足且有经验花费）。"""
        return all(p.learnable for p in self.prerequests) and (self.xp_cost is not None)


class OnBeforeLevelUp(Capability):
    @abstractmethod
    def on_before_level_up(self, unit: Unit):
        """单位升级时触发的能力效果。"""
        pass


class OnAfterLevelUp(Capability):
    @abstractmethod
    def on_after_level_up(self, unit: Unit):
        """单位升级后触发的能力效果。"""
        pass


class OnCapabilityLearned(Capability):
    @abstractmethod
    def on_capability_learned(self, unit: Unit, capability: Capability):
        """单位学习该能力时触发的效果。"""
        pass


class AttackCapability(Capability):
    """
    攻击类能力。
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

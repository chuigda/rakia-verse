from typing import List
import uuid

from .coin import Coin
from .capability import Capability
from .equipment import EquipmentTemplate, Equipment
from .species import Species


class UnitTemplate:
    """
    单位模板，定义一类单位的能力和装备组合。
    """

    def __init__(self,
                 id: str,
                 capabilities: List[Capability],
                 equipments: List[EquipmentTemplate]):
        self.id = id
        self.capabilities = capabilities
        self.equipments = equipments

        assert all(c.learnable for c in self.capabilities)
        assert all(e.purchasable for e in self.equipments)

    @property
    def train_xp_cost(self) -> int:
        """计算训练该单位所需的总经验值。"""
        return sum(c.xp_cost for c in self.capabilities if c.xp_cost is not None)

    @property
    def train_coin_cost(self) -> Coin:
        """计算训练该单位所需的总货币花费（装备+能力）。"""
        return sum((e.price for e in self.equipments if e.price is not None), Coin()) + \
               sum((c.coin_cost for c in self.capabilities if c.coin_cost is not None), Coin())


class Unit:
    """
    单位实例，代表战场上的一个具体单位。
    """

    def __init__(self,
                 history_id: str | None,
                 name: str,
                 species: Species,
                 level: int,
                 learnt: list[Capability],
                 equipments: list[Equipment],
                 hp: int,
                 xp: int,
                 free_xp: int):
        self.id = str(uuid.uuid4())
        self.history_id = history_id
        self.name = name
        self.species = species
        self.level = level
        self.learnt = learnt
        self.equipments = equipments
        self.hp = hp
        self.xp = xp
        self.free_xp = free_xp

    @property
    def capabilities(self) -> list[Capability]:
        """获取单位当前拥有的能力列表（种族+已学习+装备给予）。"""
        equipment_capabilities = [cap for e in self.equipments for cap in e.capabilities]
        return self.species.capabilities + self.learnt + equipment_capabilities

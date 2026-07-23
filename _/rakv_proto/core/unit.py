from typing import List
import uuid

from .coin import Coin
from .capability import Capability
from .equipment import EquipmentTemplate, Equipment
from .species import Species


class UnitTemplate:
    """
    单位模板，定义一类单位的能力和装备组合。

    Attributes:
        id: 模板唯一标识。
        capabilities: 单位具备的能力列表。
        equipments: 单位配备的装备列表。
    """

    def __init__(self,
                 id: str,
                 capabilities: List[Capability],
                 equipments: List[EquipmentTemplate]):
        """初始化单位模板，验证所有能力可学习且装备可购买。"""
        self.id = id
        self.capabilities = capabilities
        self.equipments = equipments

        assert all(c.learnable() for c in self.capabilities)
        assert all(e.purchasable() for e in self.equipments)

    def train_xp_cost(self) -> int:
        """计算训练该单位所需的总经验值。"""
        return sum(c.xp_cost for c in self.capabilities if c.xp_cost is not None)

    def train_coin_cost(self) -> Coin:
        """计算训练该单位所需的总货币花费（装备+能力）。"""
        return sum((e.price for e in self.equipments if e.price is not None), Coin()) + \
               sum((c.coin_cost for c in self.capabilities if c.coin_cost is not None), Coin())


class Unit:
    """单位实例，代表战场上的一个具体单位。

    Attributes:
        id: 运行时唯一标识 (UUID)。
        history_id: 关联的历史记录 ID，可为 None。
        name: 单位名称。
        species: 单位所属种族。
        learnt: 单位当前学会的能力列表。
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
        """初始化单位实例，自动分配 UUID。"""
        self.id = str(uuid.uuid4())
        self.history_id = history_id
        self.name = name
        self.species = species
        self.level = level
        self.learnt = learnt
        self.hp = hp
        self.xp = xp
        self.free_xp = free_xp

from typing import List
import uuid

from .coin import Coin
from .kind import Terrain, DamageKind
from .capability import Capability


class EquipmentTemplate:
    """
    装备模板，定义装备的价格及各项属性修正。

    Attributes:
        id: 装备唯一标识。
        price: 购买价格，None 表示不可购买。
        hp_mod: 生命值修正。
        level_up_mod: 升级生命值修正。
        defence_mod: 各地形防御修正列表。
        resistance_mod: 各伤害类型抗性修正列表。
        movement_mod: 各地形移动力修正列表。
        capabilities: 装备附带的能力列表。
    """

    def __init__(self,
                 id: str,
                 price: Coin | None,
                 hp_mod: int | None,
                 level_up_mod: int | None,
                 defence_mod: List[float] | None,
                 resistance_mod: List[float] | None,
                 movement_mod: List[float] | None,
                 capabilities: List[Capability]):
        """初始化装备模板，设置价格及HP/升级/防御/抗性/移动修正。"""
        if defence_mod is not None:
            assert len(defence_mod) == len(Terrain)
        if resistance_mod is not None:
            assert len(resistance_mod) == len(DamageKind)
        if movement_mod is not None:
            assert len(movement_mod) == len(Terrain)

        self.id = id
        self.price = price
        self.hp_mod = hp_mod
        self.level_up_mod = level_up_mod
        self.defence_mod = defence_mod
        self.resistance_mod = resistance_mod
        self.movement_mod = movement_mod
        self.capabilities = capabilities

    def purchasable(self) -> bool:
        """判断该装备是否可购买（有价格）。"""
        return self.price is not None


class Equipment:
    """
    装备实例，代表单位实际配备的装备。

    Attributes:
        id: 运行时唯一标识 (UUID)。
        history_id: 关联的历史记录 ID，可为 None。
        template: 装备模板，定义装备属性。
    """
    def __init__(self, history_id: str | None, template: EquipmentTemplate):
        """初始化装备实例，关联模板。"""
        self.id = str(uuid.uuid4())
        self.history_id = history_id
        self.template = template

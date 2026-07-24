from typing import List
import uuid

from .coin import Coin
from .kind import Terrain, DamageKind
from .capability import Capability


class EquipmentTemplate:
    """
    装备模板，定义装备的价格及各项属性修正。
    """

    def __init__(self,
                 id: str,
                 tags: List[str],
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
        self.tags = tags
        self.price = price
        self.hp_mod = hp_mod
        self.level_up_mod = level_up_mod
        self.defence_mod = defence_mod
        self.resistance_mod = resistance_mod
        self.movement_mod = movement_mod
        self.capabilities = capabilities

    @property
    def purchasable(self) -> bool:
        """判断该装备是否可购买（有价格）。"""
        return self.price is not None


class Equipment:
    """
    装备实例，代表单位实际配备的装备。
    """
    def __init__(self,
                 history_id: str | None,
                 template: EquipmentTemplate,
                 additional_capabilities: List[Capability] = []):
        """初始化装备实例，关联模板。"""
        self.id = str(uuid.uuid4())
        self.history_id = history_id
        self.template = template
        self.additional_capabilities = additional_capabilities

    @property
    def capabilities(self) -> List[Capability]:
        """获取装备附带的能力列表。"""
        return self.template.capabilities + self.additional_capabilities

from enum import Enum


class Terrain(Enum):
    """
    地形类型枚举，影响单位移动力和防御修正。
    """

    IMPASSABLE = 0       # 不可通过（洞穴墙壁）
    UNWALKABLE = 1       # 不可行走（深渊、熔岩）
    MOUNTAINS = 2        # 山脉
    HILLS = 3            # 丘陵
    CAVE = 4             # 洞穴（地下）
    FUNGUS = 5           # 蘑菇（菌类地形）
    FOREST = 6           # 森林
    FLAT = 7             # 平地（草地、道路等）
    RAILS = 8            # 铁轨
    CASTLE = 9           # 城堡
    VILLAGE = 10         # 村庄
    FROZEN = 11          # 冰冻（雪地、冰面）
    SAND = 12            # 沙地（沙漠）
    SWAMP = 13           # 沼泽
    COASTAL_REEF = 14    # 沿岸礁石
    SHALLOW_WATER = 15   # 浅水
    DEEP_WATER = 16      # 深水


class DamageKind(Enum):
    """
    伤害类型枚举，用于计算抗性。
    """

    SLASH  = 0 # 劈砍
    PIERCE = 1 # 穿刺
    IMPACT = 2 # 冲击
    FIRE   = 3 # 火焰
    ICE    = 4 # 冰寒
    ACID   = 5 # 强酸
    POISON = 6 # 毒素
    ARCANE = 7 # 奥术
    REAL   = 8 # 真实伤害（无视抗性）


class UnitStatus(Enum):
    """
    单位状态枚举，用于表示单位当前的异常状态。
    """
    POISONED = 0x01 # 中毒
    BURNING  = 0x02 # 灼烧
    SLOWED   = 0x04 # 减速
    STUNNED  = 0x08 # 定身


class AttackSpecial(Enum):
    """
    攻击特殊效果枚举，用于表示攻击的特殊属性。
    """
    NONE   = 0x00 # 无特殊效果
    POISON = 0x01 # 中毒效果
    BURN   = 0x02 # 灼烧效果
    SLOW   = 0x04 # 减速效果
    STUN   = 0x08 # 定身效果


DEFAULT_MOVEMENT_LIST = [
    99.9, # IMPASSABLE
    99.9, # UNWALKABLE
    2.0,  # MOUNTAINS
    1.5,  # HILLS
    1.25,  # CAVE
    1.25, # FUNGUS
    1.25, # FOREST
    1.0,  # FLAT
    1.0,  # RAILS
    1.0,  # CASTLE
    1.0,  # VILLAGE
    2.0,  # FROZEN
    1.25, # SAND
    1.5,  # SWAMP
    1.5,  # COASTAL_REEF
    2.0,  # SHALLOW_WATER
    99.9, # DEEP_WATER
]

DEFAULT_DEFENCE_LIST = [
    0.0,  # IMPASSABLE
    0.0,  # UNWALKABLE
    +0.2, # MOUNTAINS
    +0.2, # HILLS
    +0.1, # CAVE
    +0.1, # FUNGUS
    +0.1, # FOREST
    +0.0, # FLAT
    +0.0, # RAILS
    +0.2, # CASTLE
    +0.2, # VILLAGE
    -0.1, # FROZEN
    -0.1, # SAND
    -0.1, # SWAMP
    -0.1, # COASTAL_REEF
    -0.2, # SHALLOW_WATER
    -0.4, # DEEP_WATER
]

assert len(DEFAULT_MOVEMENT_LIST) == len(Terrain)
assert len(DEFAULT_DEFENCE_LIST) == len(Terrain)

DEFAULT_RESISTANCE_LIST = [0.0 for _ in DamageKind]

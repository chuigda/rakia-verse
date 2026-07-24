from ...core.capability import Capability


_MEDIUM_ARMOR_USE = Capability(
    type="armor_use",
    id="medium_armor_use",
    prerequests=[],
    xp_cost=8,
    coin_cost=None,
)

_HEAVY_ARMOR_USE = Capability(
    type="armor_use",
    id="heavy_armor_use",
    prerequests=[],
    xp_cost=12,
    coin_cost=None,
)

_SHIELD_USE = Capability(
    type="armor_use",
    id="shield_use",
    prerequests=[],
    xp_cost=12,
    coin_cost=None,
)

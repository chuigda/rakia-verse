from ...core.species import Species
from ...core.kind import DEFAULT_MOVEMENT_LIST, DEFAULT_DEFENCE_LIST, DEFAULT_RESISTANCE_LIST
from ...core.capability import OnCapabilityLearned, Capability
from ...core.unit import Unit


class _HumanLearnReward(OnCapabilityLearned):
    def on_capability_learned(self, unit: Unit, capability: Capability):
        if capability.xp_cost is not None:
            unit.free_xp += int(capability.xp_cost * 0.2)


_HUMAN_LEARN_REWARD = _HumanLearnReward(
    type="human_learn_reward",
    id="human_learn_reward",
    prerequests=[],
    xp_cost=None,
    coin_cost=None,
)


HUMAN = Species(
    id="human",
    base_hp=24,
    level_hp=6,
    hp_regen=2,
    agility=6,
    movement=DEFAULT_MOVEMENT_LIST,
    defence=DEFAULT_DEFENCE_LIST,
    resistance=DEFAULT_RESISTANCE_LIST,
    capabilities=[_HUMAN_LEARN_REWARD],
)

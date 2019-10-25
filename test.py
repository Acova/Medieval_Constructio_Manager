from building_level import BuildingLevel
from building_cost import BuildingCost
from capabilty import Capability
from condition import Condition

bc1 = BuildingCost("wooden","3","800","city")
con1 = Condition("requires factions { england, scotland, france, hre, denmark, spain, portugal, milan, venice, papal_states, sicily, }")
cap1 = Capability("recruit_pool \"NE Bombard\" 1 0.4 3 0",con1.getDefinition())
con2 = Condition("requires factions { northern_european, middle_eastern, eastern_european, greek, southern_european, } and event_counter gunpowder_discovered 1")

b1 = BuildingLevel("gunsmith", "city", [con2.getDefinition()], "1", bc1.getCosts(), "cannon_maker", [cap1.getDefinition()])

print(b1.getLevel())
from building_level import BuildingLevel
from building_cost import BuildingCost
from capabilty import Capability
from condition import Condition
from building import Building
from inout import Input_Output

#bc1 = BuildingCost("wooden","3","800","city")
#capCon1 = Condition("factions { england, scotland, france, hre, denmark, spain, portugal, milan, venice, papal_states, sicily, }")
#cap1 = Capability("recruit_pool \"NE Bombard\" 1 0.4 3 0",capCon1.getDefinition())
#con1 = Condition("factions { northern_european, middle_eastern, eastern_european, greek, southern_european, }")
#con2 = Condition("event_counter gunpowder_discovered 1")
#
#bl1 = BuildingLevel("gunsmith", "city", [con1.getDefinition(), con2.getDefinition()], "1", bc1.getCosts(), "cannon_maker", [cap1.getDefinition(), cap1.getDefinition()])
#
#b1 = Building("wall", "castle_wall", "christian")
#
#b1.addLevel(bl1)
#b1.addLevel(bl1)
#
#print(b1.getBuilding())

io = Input_Output("./Tools/test_file.txt")

io.openFile()

io.readBuildings()
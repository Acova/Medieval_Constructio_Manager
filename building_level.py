class BuildingLevel:
    """All the data in a building level"""

    def __init__(self, name, settlementType, buildingConditions, convert_to, buildingCost, upgrades, capabilities):
        self.name = name
        self.settlementType = settlementType
        self.buildingConditions = buildingConditions
        self.convert_to = convert_to #Level of the building to wich this converts when changing castle <> cith
        self.capabilities = capabilities
        self.buildingCost = buildingCost
        self.upgrades = upgrades #string with the name of the upgrades

    def getLevel(self):
        s = ("\t\t" + self.name + " " + self.settlementType + " " + self.buildingConditions +
            "\t\t" + "{" + "\n" +
            "\t\t\tconvert_to " + self.convert_to + "\n" +
            "\t\t\tcapability" + "\n" +
            "\t\t\t{\n")
        for capability in self.capabilities:
            s = (s +
                "\t\t\t\t" + capability + "\n")

        s = (s + "\t\t\t}\n" +
            self.buildingCost +
            "\t\t\tupgrades\n\t\t\t{\n\t\t\t\t" + self.upgrades + "\n\t\t\t}\n\t\t}")

        return s
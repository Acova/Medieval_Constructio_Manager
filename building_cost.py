class BuildingCost:
    """This class represents the costs for building a settlement"""

    def __init__(self, material, construction, cost, settlement_min):
        self.material = material
        self.construction = construction
        self.cost = cost
        self.settlement_min = settlement_min

    def getCosts(self):
        """This function will return a string with the costs"""

        s = ("\t\t\tmaterial " + self.material + "\n" +
            "\t\t\tconstruction " + self.construction + "\n" +
            "\t\t\tcost " + self.cost + "\n" +
            "\t\t\tsettlement_min " + self.settlement_min + "\n")

        return s
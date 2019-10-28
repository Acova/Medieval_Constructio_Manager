class Building:
    """Class representing a building"""

    def __init__(self, name, converTo, religion=None):
        self.name = name
        self.converTo = converTo
        if religion:
            self.religion = religion
        else:
            self.religion = None

        self.levels = []

    def addLevel(self, level):
        self.levels.append(level)

    def getBuilding(self):
        s = ("building " + self.name + "\n" +
            "{\n" +
            "\t" + "levels")

        for level in self.levels:
            s = s + " " + level.getName()
        s = s + "\n"

        if self.religion:
            s = s + "\treligion " + self.religion + "\n"
        s = s + "\t{\n"

        for level in self.levels:
            s = s + level.getLevel()

        s = s + "\t}\n\tplugins\n\t{\n\t}\n}"

        return s
from building import Building

class Input_Output:
    """This class will help with all the reading/writing stuff"""

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def openFile(self):
        self.file = open(self.filename, 'r')

    def readBuildings(self):
        buildings = []
        inBuilding = False
        inLevel = False
        name = ""
        convert_to = ""
        religion = None
        numberOfLevels = 0
        for line in self.file:
            l = line.rstrip()
            if inBuilding:
                if inLevel:
                    pass
                else:
                    if "convert_to" in l:
                        convert_to = l[l.find("convert_to")+11:]
                        print(convert_to)
                    elif "religion" in l:
                        religion = l[l.find("religion")+8:]
                        print(religion)
                    elif "levels" in l:
                        numberOfLevels = l[l.find("levels"):].find(" ")
                        print(l[l.find("levels"):])
                        #print(str(numberOfLevels) + " nieveles")
            else:
                if "building" in l:
                    inBuilding = True
                    name = l[l.find(" ")+1:]
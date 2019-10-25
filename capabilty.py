class Capability:
    """This function is used to represent a capability"""

    def __init__(self, definition, condition):
        self.definition = definition
        self.condition = condition

    def getDefinition(self):
        """Returns a string with the definition of the capability"""
        return self.definition + self.condition

    def setDefinition(self, newDefinition):
        self.definition = newDefinition
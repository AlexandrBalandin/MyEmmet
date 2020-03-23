from leaf import Leaf


class Tag(Leaf):
    def __init__(self, leafId: int, parentId: int, tagName: str, attributes: dict, textInTag: str):
        self.leafId = leafId
        self.parentId = parentId
        self.childrenId = []
        self.tagName = tagName
        self.attributes = attributes
        self.textInTag = textInTag
        self.used = 0

    def WrapInTag(self):
        returnedString = "<" + self.tagName
        for attribute in self.attributes:
            returnedString += " " + attribute + "=\"" + self.attributes[attribute] + "\""
        returnedString += ">\n" + self.textInTag + "\n<\\" + self.tagName + ">\n"
        return returnedString

    def deleteChildById(self, childId):
        self.childrenId.remove(childId)







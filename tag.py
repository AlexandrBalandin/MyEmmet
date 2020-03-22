from leaf import Leaf


class Tag(Leaf):
    def __init__(self, leafId: int, parentId: int, tagName: str, attributes: dict, textInTag: str):
        self.leafId = leafId
        self.parentId = parentId
        self.childrenId = []
        self.tagName = tagName
        self.attributes = attributes
        self.textInTag = textInTag

    def WrapInTag(self):
        returnedString = "<" + self.tagName
        for attribute in self.attributes:
            returnedString += " " + attribute + "=\"" + self.attributes[attribute] + "\""
        returnedString += ">" + self.textInTag + "<\\" + self.tagName + ">"
        return returnedString



class Leaf:
    def __init__(self, leafId: int, parentId: int):
        self.leafId = leafId
        self.parentId = parentId
        self.childrenId = []

    def appendChild(self, other):
        self.childrenId.append(other.leafId)

    def getLeafId(self):
        return self.leafId
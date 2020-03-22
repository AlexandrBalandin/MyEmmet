class Tree:
    def __init__(self):
        self.mass = []

    def getElementById(self, leafId: int):
        for leaf in self.mass:
            if (leaf.leafId == leafId):
                return leaf
        return "error, leaf not find"

    def appendLeaf(self, leaf: object):
        self.mass.append(leaf)

    def deleteElementById(self, id: int):
        self.mass.remove(self.getElementById(id))

    def getLastAdded(self):
        return self.mass[-1]

    def printTree(self):
        for elem in self.mass:
            print(elem.WrapInTag() + " id: " + str(elem.leafId) + " children: " + str(elem.childrenId) + " parent: " + str(elem.parentId))


class Tree:
    def __init__(self):
        self.mass = []

    def getElementById(self, leafId: int):
        for leaf in self.mass:
            if leaf.leafId == leafId:
                return leaf
        return "error, leaf not find"

    def appendLeaf(self, leaf: object):
        self.mass.append(leaf)

    def deleteElementById(self, leafId: int):
        self.mass.remove(self.getElementById(leafId))

    def getLastAdded(self):
        return self.mass[-1]

    def printTree(self):
        for elem in self.mass:
            print(elem.WrapInTag() + " id: " + str(elem.leafId) + " children: " +
                  str(elem.childrenId) + " parent: " + str(elem.parentId))

    def DFS(self, leafId):
        leaf = self.getElementById(leafId)
        leaf.used = 1
        for child in leaf.childrenId:
            childTag = self.getElementById(int(child))
            if childTag.used != 1:
                self.DFS(childTag.leafId)
                leaf.textInTag += childTag.WrapInTag()



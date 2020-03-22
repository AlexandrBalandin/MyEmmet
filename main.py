from tag import Tag
from tree import Tree
import re


def main():
    inputString = "div1>div2>div3^div4+div5{text}[title=\"hop\"]"
    operationPattern = "[+*>^{}\[\]]"
    tags = re.split(operationPattern, inputString)
    tags = list(filter(None, tags))
    operations = re.findall(operationPattern, inputString)

    print(tags)
    print(operations)

    tagId = 0
    parentID = -1
    tree = Tree()
    startTag = Tag(tagId, parentID, "startTag", {}, "")
    tree.appendLeaf(startTag)

    tagId = tagId + 1
    firstTag = Tag(tagId, startTag.leafId, tags.pop(0), {}, "")
    startTag.appendChild(firstTag)
    tree.appendLeaf(firstTag)
    for val in tags:
        tagId = tagId + 1
        operation = operations.pop(0)
        if operation == ">":
            lastAddedTag = tree.getLastAdded()
            tag = Tag(tagId, lastAddedTag.leafId, val, {}, "")
            lastAddedTag.appendChild(tag)
            tree.appendLeaf(tag)
        if operation == "+":
            lastAddedTag = tree.getLastAdded()
            parent = tree.getElementById(lastAddedTag.parentId)
            tag = Tag(tagId, parent.leafId, val, {}, "")
            parent.appendChild(tag)
            tree.appendLeaf(tag)
        if operation == "*":
            lastAddedTag = tree.getLastAdded()
            for i in range(1, int(val)):
                tag = Tag(lastAddedTag.leafId + i, lastAddedTag.parentId,
                          lastAddedTag.tagName, lastAddedTag.attributes,
                          lastAddedTag.textInTag)
                parent = tree.getElementById(lastAddedTag.parentId)
                parent.appendChild(tag)
                tree.appendLeaf(tag)
        if operation == "^":
            lastAddedTag = tree.getLastAdded()
            parent = tree.getElementById(lastAddedTag.parentId)
            grandparent = tree.getElementById(parent.parentId)
            while operations[0] == "^":
                operations.pop(0)
                grandparent = tree.getElementById(grandparent.parentId)
            tag = Tag(tagId, grandparent.leafId, val, {}, "")
            grandparent.appendChild(tag)
            tree.appendLeaf(tag)
        if operation == "{":
            lastAddedTag = tree.getLastAdded()
            lastAddedTag.textInTag = val
            operations.pop(0)
        if operation == "[":
            lastAddedTag = tree.getLastAdded()
            attributes = val.split(',')
            for attribute in attributes:
                key, value = attribute.split("=")
                value = value.replace("\"", '')
                lastAddedTag.attributes[key] = value
    tree.printTree()
if __name__ == "__main__":
    main()


def RNP():
    operation_pattern = "[+*>^]"
    input_string = "div+div>p>span^span+em"
    tags = re.split(operation_pattern, input_string)
    tags = list(filter(None, tags))
    operations = re.findall(operation_pattern, input_string)
    print(tags)
    print(operations)

import json
import re

class Tag:
    def __init__(self, tagName, attributes, textInTag):
        self.tagName = tagName
        self.attributes = attributes
        self.textInTag = textInTag

    def WrapInTag(self):
        returnedString = "<" + self.tagName
        for attribute in self.attributes:
            returnedString += " " + attribute + "=\"" + self.attributes[attribute] + "\""
        returnedString+= ">" + self.textInTag + "<\\" + self.tagName + ">"
        return returnedString

    def __add__(self, other):
        return self.WrapInTag() + other.WrapInTag()

    def __mul__(self, other):
        returnedString = ""
        for i in range(other):
            returnedString = returnedString + self.WrapInTag()
        return returnedString
    def __xor__ (self, other):
        pass
    def __gt__ (self, other):
        self.textInTag = self.textInTag + other.WrapInTag()
        return self.WrapInTag()

#Переписать полностью под ООП
def SquareBrackets(text):
    if [s for s in text if s in '[]']:
        results = text.split("[")
        return results[0] + " " + results[1][0:-1]
    else:
        return text



def SplitKeys(inputDisc):
    retDisc = dict()
    for key in inputDisc:
        newKeys = key.split('|')
        for newKey in newKeys:
            retDisc[newKey] = inputDisc[key]
    return retDisc


with open("snippets/html.json", "r") as read_file:
    jsonHtml = json.load(read_file)
html = SplitKeys(jsonHtml)
#inputString = input()
# заменить на нормальный парсер операций
tagDiv = Tag("div",[],"Hi, World")

tagP = Tag("p", [], "nothing")
#print(tagDiv>tagP*3)


def RNP():
    operation_pattern = "[+*>^]"
    input_string = "div+div>p>span^span+em"
    tags = re.split(operation_pattern,input_string)
    tags = list(filter(None, tags))
    operations = re.findall(operation_pattern,input_string)
    print(tags)
    print(operations)

RNP()

def ParseTag(list_tag):
    Tags = []
    for tag in list_tag:
        temp = Tag(tag,[],"")
        Tags.append(temp)
    return Tags

import json


class Tags:
    def __init__(self, tagName, attributes):
        self.tagName = tagName
        self.attributes = dict

    def WrapInTag(self):
        returnedString = "<" + self.tagName
        for attribute in self.attributes:
            returnedString += " " + attribute + "=\"" + self.attributes[attribute] + "\""
        return returnedString


def Plus(text):
    resultString = ""
    plusMass = text.split("+")
    for word in plusMass:
        resultString = resultString + " " + WrapInTag(word)
    return resultString


def SquareBrackets(text):
    if [s for s in text if s in '[]']:
        results = text.split("[")
        return results[0] + " " + results[1][0:-1]
    else:
        return text


# Переписать полностью, тут сложнее
def OpenString():
    for word in parsedString:
        print(WrapInTag(SquareBrackets(html[word])))


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
inputString = input()
# заменить на нормальный парсер операций
parsedString = inputString.split('+')
OpenString()

import json

with open("snippets/html.json", "r") as read_file:
    jsonHtml = json.load(read_file)


def SplitKeys(inputDisc):
    retDisc = dict()
    for key in  inputDisc:
        newKeys = key.split('|')
        for newKey in newKeys:
            retDisc[newKey] = inputDisc[key]
    return retDisc
inputString = input()
parsedString = inputString.split('+')#заменить на нормальный парсер операций
html = SplitKeys(jsonHtml)


def WrapInTag(text):
    return "<" + text + ">" + "<\\" + text + ">"

#если нет строк в словаер, просто оборачивать в теги
def OpenString():
    for word in parsedString:
        print(WrapInTag(html[word]))


OpenString()

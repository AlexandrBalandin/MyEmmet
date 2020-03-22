import json

def SplitKeys(inputDisc):
    retDisc = dict()
    for key in inputDisc:
        newKeys = key.split('|')
        for newKey in newKeys:
            retDisc[newKey] = inputDisc[key]
    return retDisc

def openJSON():
    with open("snippets/html.json", "r") as read_file:
        jsonHtml = json.load(read_file)
        html = SplitKeys(jsonHtml)
    return  html



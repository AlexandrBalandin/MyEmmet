import json

with open("snippets/html.json", "r") as read_file:
    html = json.load(read_file)


print(type(html))
inputString = input()

parsedString = inputString.split('+')


def WrapInTag(text):
    return "<" + text + ">" + "<\\" + text + ">"


def OpenString():
    for word in parsedString:
        print(WrapInTag(html[word]))
OpenString()

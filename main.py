import json

with open("snippets/html.json", "r") as read_file:
    html = json.load(read_file)


print(html)#разбить ключи в словаре

inputString = input()

parsedString = inputString.split('+')#заменить на нормальный парсер операций


def WrapInTag(text):
    return "<" + text + ">" + "<\\" + text + ">"

#если нет строк в словаер, просто оборачивать в теги
def OpenString():
    for word in parsedString:
        print(WrapInTag(html[word]))


OpenString()

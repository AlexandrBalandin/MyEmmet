inputString = input()

parsedString = inputString.split('+')


def WrapInTag(text):
    return "<" + text + ">" + "<\\" + text + ">"


def OpenString():
    for i in parsedString:
        print(WrapInTag(i))
    return 0


OpenString()

import re
from lexer.lexerTokens import tokens


class Token:
    def __init__(self, value, name):
        self.value = value
        self.name = name


def lexer(code):
    tokenList = []
    begin = 0
    matched = False

    i = 0
    n = len(code)
    while (i < n):
        curString = code[begin: i + 1]
        flag = matched
        breakFlag = True

        for j in range(len(tokens)):
            if (None != re.match(tokens[j].value, curString)):
                matched = j
                breakFlag = False
                break

        if (flag != False and breakFlag):
            name = tokens[matched].name
            if((name != "comments") and (name != "spaces")):
                tokenList.append(Token(
                    code[begin:i], code[begin:i] if tokens[matched].needLexeme else tokens[matched].name))
            begin = i
            i -= 1
            matched = False
        i += 1

    if (flag != False):
        name = tokens[matched].name
        if((name != "comments") and (name != "spaces")):
            tokenList.append(Token(
                code[begin:i], code[begin:i] if tokens[matched].needLexeme else tokens[matched].name))

    print("{:<24s}{:s}".format("=====================+==", "========="))
    print("{:<24s}{:s}".format("Token", "Value"))
    print("{:<24s}{:s}".format("=====================+==", "========="))
    for i in tokenList:
        print("{:<24s}{:s}".format(i.name, i.value))

    return tokenList

import parse.parseTable as ps


def formatString(st, size):
    temp = st[:]
    len1 = (size - len(st)) // 2
    st = " " * len1 + st + " " * len1
    if(len(st) != size):
        st += " "
    return st


def printRow(top, input, result):
    print(formatString(top, 16) + "|" + formatString(input, 16) +
          "|     " + formatString(result, 46))


def parse(tokenList):
    stack = ["$", "Functions"]
    print("=" * 16 + "+" + "=" * 16 + "+" + "=" * 48)
    print(formatString("Top of Stack", 16) + "|" +
          formatString("Input Symbol", 16) + "|" + formatString("action", 46))
    print("=" * 16 + "+" + "=" * 16 + "+" + "=" * 48)
    while (len(stack) != 0 and len(tokenList) != 0):
        if (stack[-1] == "$"):
            if(tokenList[0].name == "$"):
                printRow("$", "$", "Accepted")
                break

        if (stack[-1] == "''"):
            stack.pop()

        if (stack[-1][0].isupper()):
            row = ps.nonTerminals.index(stack[-1])
            column = ps.terminals.index(tokenList[0].name)
            production = ps.parseTable[row][column][:]

            if (production == "sync"):
                printRow(stack[-1], tokenList[0].name, "sync")
                stack.pop()
            elif (len(production) == 0):
                tokenList.pop(0)
            else:
                printRow(stack[-1], tokenList[0].name,
                         stack[-1] + " -> " + " ".join(production))
                stack.pop()
                production.reverse()
                stack.extend(production)

        elif (tokenList[0].name == stack[-1]):
            printRow(stack[-1], tokenList[0].name, "Match : " + stack[-1])
            stack.pop()
            tokenList.pop(0)
        else:
            printRow(stack[-1], tokenList[0].name, "Not Matched")
            stack.pop()
    if(len(stack) == 0 or len(tokenList) == 0):
        printRow(" ", " ", "Error")

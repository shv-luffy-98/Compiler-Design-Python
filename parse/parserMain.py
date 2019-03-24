import parse.parseTable as ps


def parse(tokenList):
    stack = ["$", "Functions"]

    while (len(stack)):
        if (stack[-1] == "$"):
            print("Accepted")
            break

        if (stack[-1] == "''"):
            stack.pop()
            # stack.pop()

        if (stack[-1][0].isupper()):
            row = ps.nonTerminals.index(stack[-1])
            column = ps.terminals.index(tokenList[0].name)
            production = ps.parseTable[row][column][:]
            print(stack[-1], "->", production, )

            stack.pop()
            production.reverse()
            stack.extend(production)
        elif (tokenList[0].name == stack[-1]):
            stack.pop()
            tokenList.pop(0)
        else:
            print("Error : ", tokenList[0].name, stack[-1])
            break

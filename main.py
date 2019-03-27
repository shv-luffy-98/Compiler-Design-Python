from lexer.lexerMain import lexer
from parse.parserMain import parse

code = open("./source/code.txt", "r").read()
print("\nLexer")
tokenList = lexer(code)
print("\nParser")
parse(tokenList)

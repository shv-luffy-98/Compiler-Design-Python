from lexer.lexerMain import lexer
from parse.parserMain import parse

code = open("./source/code.txt", "r").read()
print("Lexer\n")
tokenList = lexer(code)
print("\nParser\n")
parse(tokenList)

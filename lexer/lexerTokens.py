class Token:
    def __init__(self, value, name, needLexeme):
        self.value = value
        self.name = name
        self.needLexeme = needLexeme


tokens = [
    Token("^//.*\Z", "comments", False),
    Token("^/\*(.|\n)*\*/\Z", "comments", False),
    Token("^[\s\t\n]\Z", "spaces", False),

    Token("^[\(\)\[\]\{\}]\Z", "bracket", True),
    Token("^(\+\+|\-\-)\Z", "unary operator", False),
    Token("^(\+|\-|\*|/|=)\Z", "operator", True),
    Token("^(<|>|<=|>=|==|!=)\Z", "relop", False),

    Token("^(begin|end|while|for)\Z", "keyword", True),
    Token("^(int|float|char)\Z", "type", False),

    Token("^;\Z", "semicolon", True),

    Token("^(\d)+(.(\d)+)?\Z", "number", False),
    Token("^[a-zA-Z][a-zA-Z0-9]*\Z", "id", False),
]

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
    Token("^(<|>|<=|>=|==|!=)\Z", "relational operator", False),

    Token("^(begin|end|while)\Z", "keyword", True),
    Token("^(int|float|char)\Z", "type", False),

    Token("^;\Z", "semicolon", False),

    Token("^(\d)+(.(\d)+)?\Z", "number", False),
    Token("^[a-zA-Z][a-zA-Z0-9]*\Z", "id", False),
]

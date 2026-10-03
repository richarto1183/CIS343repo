from token_type import TokenType
from token import Token


class Scanner:
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.keywords = {
            "let": TokenType.LET,
            "when": TokenType.WHEN,
            "otherwise": TokenType.OTHERWISE,
            "loop": TokenType.LOOP,
            "func": TokenType.FUNC,
            "return": TokenType.RETURN,
            "print": TokenType.PRINT,
            "true": TokenType.TRUE,
            "false": TokenType.FALSE,
            "null": TokenType.NULL,
        }


    def scan_tokens(self):
        # scans the source string and returns a list of tokens
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

# --- start of AI code ---
    def scan_token(self):
        # scans a single token from the source string
        character = self.advance()

        if character == "!":
            if self.match("="):
                self.add_token(TokenType.BANG_EQUAL)
            else:
                self.add_token(TokenType.BANG)

        elif character == "=":
            if self.match("="):
                self.add_token(TokenType.EQUAL_EQUAL)
            else:
                self.add_token(TokenType.EQUAL)

        elif character == "<":
            if self.match("="):
                self.add_token(TokenType.LESS_EQUAL)
            else:
                self.add_token(TokenType.LESS)

        elif character == ">":
            if self.match("="):
                self.add_token(TokenType.GREATER_EQUAL)
            else:
                self.add_token(TokenType.GREATER)

        elif character == "(":
            self.add_token(TokenType.LEFT_PAREN)
        elif character == ")":
            self.add_token(TokenType.RIGHT_PAREN)
        elif character == "{":
            self.add_token(TokenType.LEFT_BRACE)
        elif character == "}":
            self.add_token(TokenType.RIGHT_BRACE)
        elif character == ",":
            self.add_token(TokenType.COMMA)
        elif character == ".":
            self.add_token(TokenType.DOT)
        elif character == ";":
            self.add_token(TokenType.SEMICOLON)
        elif character == "+":
            self.add_token(TokenType.PLUS)
        elif character == "-":
            self.add_token(TokenType.MINUS)
        elif character == "*":
            self.add_token(TokenType.STAR)
        elif character == "/":
            if self.match("/"):
                while self.peek() != "\n" and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)

        elif character == " " or character == "\r" or character == "\t":
            # ignore whitespace
            pass
        elif character == "\n":
            # increment line number on new line
            self.line += 1

        elif character == '"':
            self.string()

        elif character.isdigit():
            self.number()

        elif character.isalpha() or character == "_":
            self.identifier()

        else:
            print(f"[line {self.line}] Error: Unexpected character '{character}'.")
# --- end of AI code ---


    def advance(self):
        # returns the current character and advances the current position
        character =  self.source[self.current]
        self.current += 1
        return character

    def match(self, expected):
        # returns True if the current character matches the expected character and advances the current position
        if self.is_at_end():
            return False

        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self):
        # returns the current character without advancing the current position
        if self.is_at_end():
            return "\0"
        
        return self.source[self.current]

    def peek_next(self):
        # returns the next character without advancing the current position
        if self.current + 1 >= len(self.source):
            return "\0"

        return self.source[self.current + 1]


    def string(self):
        # scans a string literal from the source string
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == "\n":
                self.line += 1

            self.advance()

        if self.is_at_end():
            print(f"[line {self.line}] Error: Unterminated string.")
            return

        # consume the closing "
        self.advance()

        # remove the surrounding quotes for the literal value
        value = self.source[self.start + 1:self.current - 1]

        self.add_token(TokenType.STRING, value)

    def number(self):
        while self.peek().isdigit():
            self.advance()

        if self.peek() == "." and self.peek_next().isdigit():
            self.advance()

            while self.peek().isdigit():
                self.advance()

        value = float(self.source[self.start:self.current])
        self.add_token(TokenType.NUMBER, value)

    def identifier(self):
        while self.peek().isalnum() or self.peek() == "_":
            self.advance()

        text = self.source[self.start:self.current]

        token_type = self.keywords.get(text, TokenType.IDENTIFIER)

        self.add_token(token_type)


    def add_token(self, token_type, literal=None):
        # adds a token to the list of tokens
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))

    def is_at_end(self):
        # returns True if the current position is at the end of the source string
        return self.current >= len(self.source)
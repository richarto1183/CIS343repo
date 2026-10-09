# --- begin AI code ---

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from expr import Binary, Grouping, Unary, Literal
from ast_printer import AstPrinter
from token import Token
from token_type import TokenType

# --- end AI code ---

printer = AstPrinter()

assert printer.print(Literal(42)) == "42"
assert printer.print(Literal(True)) == "true"
assert printer.print(Literal(False)) == "false"
assert printer.print(Literal(None)) == "null"

print("Basic literal tests passed.")

unary_expression = Unary(
    Token(TokenType.MINUS, "-", None, 1),
    Literal(5)
)

binary_expression = Binary(
    Literal(5),
    Token(TokenType.PLUS, "+", None, 1),
    Literal(3)
)

nested_expression = Binary(
    Grouping(
        Binary(
            Literal(5),
            Token(TokenType.PLUS, "+", None, 1),
            Literal(3)
        )
    ),
    Token(TokenType.STAR, "*", None, 1),
    Literal(2)
)

assert printer.print(unary_expression) == "(- 5)"
assert printer.print(binary_expression) == "(+ 5 3)"
assert printer.print(nested_expression) == "(* (group (+ 5 3)) 2)"

print("Expression tests passed.")

print("\ntesting all binary operators:")

operators = [
    (TokenType.PLUS, "+"),
    (TokenType.MINUS, "-"),
    (TokenType.STAR, "*"),
    (TokenType.SLASH, "/"),
    (TokenType.EQUAL_EQUAL, "=="),
    (TokenType.BANG_EQUAL, "!="),
    (TokenType.GREATER, ">"),
    (TokenType.GREATER_EQUAL, ">="),
    (TokenType.LESS, "<"),
    (TokenType.LESS_EQUAL, "<=")
]

for token_type, symbol in operators:
    expression = Binary(
        Literal(10),
        Token(token_type, symbol, None, 1),
        Literal(5)
    )

    actual = printer.print(expression)
    expected = f"({symbol} 10 5)"

    assert actual == expected, f"Expected: {expected}, but got: {actual}"

    print(f"PASS: {actual}")

print("\ntesting all literal types:")

literals = [
    (Literal(42), "42"),
    (Literal(3.14), "3.14"),
    (Literal("Hello, World!"), "Hello, World!"),
    (Literal(True), "true"),
    (Literal(False), "false"),
    (Literal(None), "null")
]

for expression, expected in literals:
    actual = printer.print(expression)

    assert actual == expected, f"Expected {expected}, got {actual}"

    print(f"PASS: {actual}")

print("\ntesting unary operators:")

unary_tests = [
    (Unary(Token(TokenType.MINUS, "-", None, 1), Literal(10)), "(- 10)"),
    (Unary(Token(TokenType.BANG, "!", None, 1), Literal(True)), "(! true)")
]

for expression, expected in unary_tests:
    actual = printer.print(expression)

    assert actual == expected, f"Expected {expected}, got {actual}"

    print(f"PASS: {actual}")

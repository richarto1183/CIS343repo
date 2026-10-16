# --- start AI code ---

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from scanner import Scanner
from parser import Parser, ParserError
from ast_printer import AstPrinter


def parse_expression(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    if scanner.had_error:
        return "Lexical Error"

    try:
        parser = Parser(tokens)
        expression = parser.parse()
        return AstPrinter().print(expression)

    except ParserError as error:
        return str(error)

tests = [
    # Arithmetic operators
    ("Addition", "5 + 3", "(+ 5.0 3.0)"),
    ("Subtraction", "10 - 5", "(- 10.0 5.0)"),
    ("Multiplication", "4 * 3", "(* 4.0 3.0)"),
    ("Division", "20 / 4", "(/ 20.0 4.0)"),

    # Precedence and associativity
    ("Precedence", "5 + 3 * 2", "(+ 5.0 (* 3.0 2.0))"),
    ("Associativity", "10 - 5 - 2", "(- (- 10.0 5.0) 2.0)"),
    ("Grouping", "(5 + 3) * 2", "(* (group (+ 5.0 3.0)) 2.0)"),
    ("Nested Grouping", "((2 + 3) * (4 - 1))",
     "(group (* (group (+ 2.0 3.0)) (group (- 4.0 1.0))))"),

    # Comparison operators
    ("Greater Than", "10 > 5", "(> 10.0 5.0)"),
    ("Greater Equal", "10 >= 5", "(>= 10.0 5.0)"),
    ("Less Than", "5 < 10", "(< 5.0 10.0)"),
    ("Less Equal", "5 <= 10", "(<= 5.0 10.0)"),

    # Equality operators
    ("Equal", "5 == 5", "(== 5.0 5.0)"),
    ("Not Equal", "5 != 3", "(!= 5.0 3.0)"),

    # Unary operators
    ("Unary Minus", "-5", "(- 5.0)"),
    ("Logical Not", "!true", "(! true)"),
    ("Multiple Unary", "!-5", "(! (- 5.0))"),

    # Literal types
    ("Integer", "42", "42.0"),
    ("Decimal", "3.14", "3.14"),
    ("String", '"Hello Nova"', "Hello Nova"),
    ("True", "true", "true"),
    ("False", "false", "false"),
    ("Null", "null", "null"),

    # Syntax errors
    ("Missing Parenthesis", "(5 + 3",
     "[line 1] Error at end: Expected ')' after expression."),
    ("Missing Operand", "5 +",
     "[line 1] Error at end: Expected expression."),
    ("Unexpected Operator", "5 + * 3",
     "[line 1] Error at '*': Expected expression."),
    ("Trailing Token", "5 3",
     "[line 1] Error at '3': Unexpected token after expression."),

    # Lexical errors
    ("Invalid Character", "5 + @", "Lexical Error"),
    ("Unterminated String", '"Hello', "Lexical Error"),
]

passed = 0

for name, source, expected in tests:
    actual = parse_expression(source)

    if actual == expected:
        print(f"PASS: {name}")
        passed += 1
    else:
        print(f"FAIL: {name}")
        print(f"  Input:    {source}")
        print(f"  Expected: {expected}")
        print(f"  Actual:   {actual}")

print(f"\nResults: {passed}/{len(tests)} tests passed")

# --- end AI code ---
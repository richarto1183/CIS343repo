import sys

from scanner import Scanner
from parser import Parser, ParserError
from ast_printer import AstPrinter
from expr import EvaluationError


def stringify(value):
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"

    if type(value) is float:
        text = str(value)
        if text.endswith(".0"):
            return text[:-2]
        return text

    return str(value)

def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    if scanner.had_error:
        return

    try:
        parser = Parser(tokens)
        statements = parser.parse()

        for statement in statements:
            statement.execute()
        
    except (ParserError, EvaluationError) as error:
        print(error)

def run_file(path):
    with open(path, "r") as file:
        source = file.read()

    run(source)

def run_prompt():
    print("Nova Interactive Mode")
    print("Type 'exit' to quit.")

    while True:
        try:
            line = input("> ")

            if line == "exit":
                break

            run(line)

        except EOFError:
            break

def main():
    if len(sys.argv) > 2:
        print("Usage: python src/main.py [script]")
        return

    if len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()

if __name__ == "__main__":
    main()
import sys

def run_file(path):
    print("Scanner Not Implemented")


def run_prompt():
    while True:
        try:
            line = input("> ")
            print("Scanner Not Implemented")
        except (EOFError, KeyboardInterrupt):
            print()
            break


def main():
    if len(sys.argv) > 2:
        print("Usage: python src/lox.py [script]")
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()


if __name__ == "__main__":
    main()
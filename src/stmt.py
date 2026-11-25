from environment import Environment


class Expression:
    def __init__(self, expression):
        self.expression = expression
    
    def execute(self, environment):
        self.expression.interpret(environment)


class Print:
    def __init__(self, expression):
        self.expression = expression
    
    def execute(self, environment):
        value = self.expression.interpret(environment)

        if value is None:
            print("null")
        elif value is True:
            print("true")
        elif value is False:
            print("false")
        # --- start AI code ---
        elif type(value) is float and str(value).endswith(".0"):
            print(int(value))
        # --- end AI code ---
        else:
            print(value)

class Var:
    def __init__(self, name, initializer):
        self.name = name
        self.initializer = initializer

    def execute(self, environment):
        value = None

        if self.initializer is not None:
            value = self.initializer.interpret(environment)

        environment.define(self.name.lexeme, value)

class Block:
    def __init__(self, statements):
        self.statements = statements

    def execute(self, environment):
        local_environment = Environment(environment)

        for statement in self.statements:
            statement.execute(local_environment)

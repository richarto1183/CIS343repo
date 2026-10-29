from token_type import TokenType


class EvaluationError(Exception):
    def __init__(self, token, message):
        super().__init__(
            f"[line {token.line}] Runtime error at "
            f"'{token.lexeme}': {message}"
        )

def is_truthy(value):
    return value is not None and value is not False


class Literal:
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value


class Grouping:
    def __init__(self, expression):
        self.expression = expression

    def interpret(self):
        return self.expression.interpret()


class Unary:
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def interpret(self):
        right = self.right.interpret()

        if self.operator.token_type == TokenType.MINUS:
            if type(right) is not float:
                raise EvaluationError(self.operator, "Operand must be a number.")
            return -right

        if self.operator.token_type == TokenType.BANG:
            return not is_truthy(right)

        raise EvaluationError(self.operator, "Unknown unary operator.")


class Binary:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def interpret(self):
        left = self.left.interpret()
        right = self.right.interpret()
        operator = self.operator.token_type

        if operator == TokenType.EQUAL_EQUAL:
            return type(left) is type(right) and left == right

        if operator == TokenType.BANG_EQUAL:
            return not (type(left) is type(right) and left == right)

        if operator == TokenType.PLUS:
            if type(left) is float and type(right) is float:
                return left + right

            if type(left) is str and type(right) is str:
                return left + right

            raise EvaluationError(self.operator, "Operands must be two numbers or two strings.")

        if type(left) is not float or type(right) is not float:
            raise EvaluationError(self.operator, "Operands must be numbers.")

        if operator == TokenType.MINUS:
            return left - right

        if operator == TokenType.STAR:
            return left * right

        if operator == TokenType.SLASH:
            if right == 0:
                raise EvaluationError(self.operator, "Cannot divide by zero.")
            return left / right

        if operator == TokenType.GREATER:
            return left > right

        if operator == TokenType.GREATER_EQUAL:
            return left >= right

        if operator == TokenType.LESS:
            return left < right

        if operator == TokenType.LESS_EQUAL:
            return left <= right

        raise EvaluationError(self.operator, "Unknown binary operator.")
    
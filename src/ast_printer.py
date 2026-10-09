from expr import Binary, Grouping, Unary, Literal


class AstPrinter:
    def print(self, expression):
        return self.visit(expression)

    def visit(self, expression):
        if isinstance(expression, Binary):
            return self.visit_binary(expression)
        elif isinstance(expression, Grouping):
            return self.visit_grouping(expression)
        elif isinstance(expression, Unary):
            return self.visit_unary(expression)
        elif isinstance(expression, Literal):
            return self.visit_literal(expression)
        else:
            raise ValueError(f"Unknown expression type: {type(expression)}")

    def visit_literal(self, expression):
        if expression.value is None:
            return "null"

        if expression.value is True:
            return "true"

        if expression.value is False:
            return "false"

        return str(expression.value)

    def visit_unary(self, expression):
        operator = expression.operator.lexeme
        right = self.visit(expression.right)

        return f"({operator} {right})"

    def visit_binary(self, expression):
        left = self.visit(expression.left)
        operator = expression.operator.lexeme
        right = self.visit(expression.right)

        return f"({operator} {left} {right})"

    def visit_grouping(self, expression):
        inside = self.visit(expression.expression)

        return f"(group {inside})"

    
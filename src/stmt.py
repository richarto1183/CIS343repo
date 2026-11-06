class Expression:
    def __init__(self, expression):
        self.expression = expression
    
    def execute(self):
        self.expression.interpret()


class Print:
    def __init__(self, expression):
        self.expression = expression
    
    def execute(self):
        value = self.expression.interpret()

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

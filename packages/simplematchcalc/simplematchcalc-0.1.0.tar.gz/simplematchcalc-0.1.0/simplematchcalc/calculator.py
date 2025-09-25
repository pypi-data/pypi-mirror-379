class SimpleMatchCalc:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def mod(self, a, b):
        if b == 0:
            raise ValueError("Modulo by zero is not allowed")
        return a % b

class DemoClass:

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number.")
        else:
            self.value = value

    def add(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        else:
            return self.value + amount
    
    def subtract(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        else:
            return self.value - amount

    def multiply(self, factor):
        if not isinstance(factor, (int, float)):
            raise ValueError("Factor must be a number.")
        else:
            return self.value * factor
    
    def divide(self, divisor):
        if not isinstance(divisor, (int, float)):
            raise ValueError("Divisor must be a number.")
        else:
            if divisor == 0:
                raise ValueError("Cannot divide by zero.")
            return self.value / divisor
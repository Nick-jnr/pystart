import operator

class Calculator:
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': self.safe_divide,
            '**': operator.pow,
        }

    def safe_divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def calculate(self, a, op, b):
        if op not in self.operations:
            raise ValueError(f"Unsupported operation: {op}")
        return self.operations[op](a, b)

def main():
    calc = Calculator()
    print("Simple Calculator")
    print("Supported operations: +, -, *, /, **")
    while True:
        try:
            expr = input("Enter expression (e.g., 2 + 3) or 'quit': ")
            if expr.lower() == 'quit':
                break
            parts = expr.split()
            if len(parts) != 3:
                print("Invalid input format. Use: number operator number")
                continue
            a, op, b = parts
            a = float(a)
            b = float(b)
            result = calc.calculate(a, op, b)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
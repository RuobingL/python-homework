class Calculator:
    """
    @param a, b: Two integers.
    @param operator: A character, +, -, *, /.
    """

    """
    # solution 1
    def calculate(self, a, operator, b):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        else:
            return a / b
    """

    # solution 2
    def calculate(self, a, operator, b):
        res =  {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }[operator](a, b)
        return res


if __name__ == '__main__':
    calc = Calculator()
    print calc.calculate(1, '/', 2)



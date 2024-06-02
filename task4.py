class Calculator:
    def __init__(self, a, b, znak):
        self.a = a
        self.b = b
        self.operation = znak

    def sum(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def zarb(self):
        return self.a * self.b

    def taqsim(self):
        if self.b == 0:
            return self.a / self.b


while True:

    a = int(input())
    znak = input()
    b = int(input())

    calc = Calculator(a, b, znak)
    match znak:
        case '+':
            print(f"{a} + {b} = {calc.sum()}")
        case '-':
            print(f"{a} - {b} = {calc.minus()}")
        case '*':
            print(f"{a} * {b} = {calc.zarb()}")
        case '/':
            print(f"{a} / {b} = {calc.taqsim()}")    



        
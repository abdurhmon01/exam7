class Calculator:
    def factorial(self,n):
        fac=1
        for i in range(1,n+1):
            fac*=i
        return fac
    def power(self,a,b):
        return a**b
    def sqrt(self,n):
        return n**0.5
calculator=Calculator()
print(calculator.factorial(5))
print(calculator.power(2,3))
print(calculator.sqrt(25))

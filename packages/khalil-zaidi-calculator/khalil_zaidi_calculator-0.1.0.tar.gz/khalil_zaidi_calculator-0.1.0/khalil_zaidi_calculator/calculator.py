import math

class Calculator:
    """آلة حاسبة متقدمة تدعم العمليات الأساسية وبعض العمليات الإضافية"""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("لا يمكن القسمة على صفر")
        return a / b

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("لا يمكن أخذ الجذر التربيعي لعدد سالب")
        return math.sqrt(a)

    def modulo(self, a, b):
        return a % b

    def average(self, numbers):
        if not numbers:
            raise ValueError("القائمة فارغة")
        return sum(numbers) / len(numbers)

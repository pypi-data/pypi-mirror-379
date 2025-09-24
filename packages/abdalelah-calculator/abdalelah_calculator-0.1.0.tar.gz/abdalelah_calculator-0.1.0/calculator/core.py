class Calculator:
    """آلة حاسبة بسيطة تدعم العمليات الأساسية"""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("لا يمكن القسمة على صفر")
        return a / b

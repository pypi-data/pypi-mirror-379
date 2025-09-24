import math

class AdvancedCalculator:
    """آلة حاسبة متقدمة للعمليات العلمية"""

    def power(self, base, exp):
        return math.pow(base, exp)

    def sqrt(self, x):
        if x < 0:
            raise ValueError("لا يمكن حساب الجذر التربيعي لعدد سالب")
        return math.sqrt(x)

    def factorial(self, n):
        if n < 0:
            raise ValueError("العامل غير معرف للأعداد السالبة")
        return math.factorial(n)

    def sin(self, x):
        return math.sin(math.radians(x))

    def cos(self, x):
        return math.cos(math.radians(x))

    def tan(self, x):
        return math.tan(math.radians(x))

# Calculator

مكتبة بايثون لآلة حاسبة احترافية:
- العمليات الأساسية: جمع، طرح، ضرب، قسمة.
- العمليات المتقدمة: قوة، جذر تربيعي، مضروب، جيب، جيب تمام، ظل.

## مثال استخدام
```python
from calculator import Calculator, AdvancedCalculator

c = Calculator()
print(c.add(5, 3))   # 8

adv = AdvancedCalculator()
print(adv.sqrt(16))  # 4.0

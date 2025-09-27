# khalil-zaidi-calculator

آلة حاسبة متقدمة بلغة بايثون تدعم العمليات الأساسية والإضافية.

## التثبيت
```bash
pip install khalil-zaidi-calculator
```

## الاستخدام
```python
from khalil_zaidi_calculator import Calculator

calc = Calculator()

print(calc.add(5, 3))       # 8
print(calc.divide(10, 2))   # 5
print(calc.power(2, 4))     # 16
print(calc.sqrt(25))        # 5
print(calc.average([1,2,3])) # 2
```

## المزايا
- جمع، طرح، ضرب، قسمة
- رفع للأس (Power)
- جذر تربيعي
- باقي القسمة (Modulo)
- المتوسط الحسابي
- معالجة أخطاء ذكية

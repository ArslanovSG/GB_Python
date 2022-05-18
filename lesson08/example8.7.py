# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, arg1, arg2):
        self.real = arg1
        self.img = arg2

    def __add__(self, other):
        print(f'Сумма чисел:')
        return f'{self.real + other.real} + {self.img + other.img} * i'

    def __mul__(self, other):
        print(f'Произведение чисел:')
        return f'{self.real * other.real - (self.img * other.img)} + {self.img + other.real} * i'

number1 = ComplexNumber(8, 9)
number2 = ComplexNumber(4, 8)
print(number1 + number2)
print(number1 * number2)
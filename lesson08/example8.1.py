# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен
# проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def to_int(cls, data):
        d, m, y = data.split('-')
        return cls(int(d), int(m), int(y))

    @staticmethod
    def validdate(obj):
        if obj.day < 1 or obj.day > 31:
            return "Введите верно день"
        elif obj.month > 12 or obj.month < 1:
            return "Введите верно месяц"
        elif obj.year < 1 or obj.year > 9999:
            return "Введите верно год"
        else:
            return f"{obj.day}-{obj.month}-{obj.year}"

my_date = Data.to_int("18-05-2022")
print(Data.validdate(my_date))
#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def salary():
    a = float(input('Введите количество отработанных часов: '))
    b = float(input('Введите ставку за 1 час: '))
    c = float(input('Укажите размер премии: '))
    return (a * b) + c

print(f'Размер заработной платы составит: {salary() }')
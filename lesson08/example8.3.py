# 3. Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyNumberException(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []

while True:
    inp_list = input("Введите значение или Q для выхода: ")
    if inp_list == 'Q':
        print(f"Список чисел: {my_list}")
        break
    try:
        if not inp_list.isdigit():
            raise MyNumberException("Необходимо ввести число!")
    except MyNumberException as wrong:
        print(wrong)
    else:
        my_list.append(inp_list)
        print(f"Список чисел: {my_list}")
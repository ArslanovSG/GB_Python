#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

new_list = [13, "sun", [1, 3], True, 1.3, {"city": "Moscow", "country": "Russia"}]

for i in new_list:
    print(f'{i} is {type(i)}')

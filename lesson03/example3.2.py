# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(firstname, lastname, birthyear, city, email, phone):
    print(firstname, lastname, birthyear, city, email, phone)


my_func(firstname='Сергей', lastname='Арсланов', birthyear=1980, city='Moscow', email='email', phone='1234567')

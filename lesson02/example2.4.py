#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_str = input('Введите предложение: ').split()

for key, value in enumerate(my_str, 1):
    print(key, value[0:10])

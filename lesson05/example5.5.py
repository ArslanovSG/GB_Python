#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randrange

with open("text5.txt", "w") as user_file:
    for i in range(5):
        user_file.write(str(randrange(1, 10)) + " ")

with open('text5.txt', 'r') as user_file:
    my_line = user_file.readline().split()
    total = sum([int(el) for el in my_line])
    print(f"Сумма чисел: {total}")
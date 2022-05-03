#4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

import codecs

my_list = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

def my_func(string):

    for key, value in enumerate(string):
        if value in my_list:
            string[key] = my_list[value]
    return string

with codecs.open("text4.txt", "r") as list_numb:
    for line in list_numb:
        string = line.split()
        with codecs.open("text4_new.txt", "a+") as list_numb_new:
            new_string = " ".join(my_func(string))
            list_numb_new.write(f"{new_string}\n")
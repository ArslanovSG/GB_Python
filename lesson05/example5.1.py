#1. Создать программно файл в текстовом формате, записать в него построчно данные,вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_list = []
while True:
    my_write = input("Введите данные для записи (для выхода введите пустую строку): ")
    if my_write == "":
        print(my_list)
        exit()
    else:
        new_list = my_write + "\n"
        my_list.append(new_list)

    with open("text.txt", "w", encoding='utf-8') as file_object:
        file_object.writelines(my_list)
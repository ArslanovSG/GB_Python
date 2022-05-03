# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_list = ["Я люблю людей!\n", "Вы тоже\n", "любите!\n"]

with open("text2.txt", "w+") as file_object:
    file_object.writelines(my_list)
with open("text2.txt") as file_object:
    lines = 0
    letters = 0
    for line in file_object:
        letters = len(line.split())
        print(f"Количество слов в {lines + 1} строке: {letters}")
        lines += 1

print(f"Количество строк: {lines}")


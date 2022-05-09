#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict = {}

with open("text6.txt", "r", encoding="utf-8") as user_file:
    for i in user_file:
        name, hours = i.split(:")
        hours_sum = sum(map(int, "".join([i for i in hours if i == ' ' or  (i >= "0" and i <= "9")]).split()))
        my_dict[name] = hours_sum

print(my_dict)
#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
#Пример файла:
# Иванов 23543.12
# Петров 13749.32

employees = {
    'Иванов': 23543.12,
    'Петров': 13749.32,
    'Сидоров': 19000.00,
    'Арсланов': 25000.78,
    'Арсланова': 22456.90,
    'Иванова': 12433.00,
    'Петрова': 11098.98,
    'Сидорова': 22222.43,
    'Грозный': 30000.00,
    'Ленин': 15000.00
}

try:
    file_object = open("text3.txt", "w")
    for last_name, salary in employees.items():
        file_object.write(last_name + " " + str(salary) + "\n")
except IOError:
    print("Произошла ошибка!")
finally:
    file_object.close()

summa = 0
count = 0
employee = []
with open("text3.txt", "r", encoding="utf-8") as file_object:
    for line in file_object:
        print(line, end="")
        counter = line.split(" ")
        if float(counter[1]) <= 20000:
            employee.append(counter[0])
        summa += float(counter[1])
        count += 1
result = summa / count

print(f"Сотрудники с окладом менее 20 тыс.: {employee}")
print(f"Средняя величина доходов сотрудников: {result}")
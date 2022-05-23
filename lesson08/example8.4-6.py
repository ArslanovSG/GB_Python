# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также
# класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для
# приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на
# склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Equipment:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return '\n' + self.__class__.__name__ \
               + ': ' + str(self.__dict__)

class Printer(Equipment):
    laser_printer: bool

    def __init__(self, name, price, laser_printer = True):
        super().__init__(name, price)
        self.laser_printer = laser_printer


class Scaner(Equipment):
    manual_scanner: bool

    def __init__(self, name, price, manual_scanner = True):
        super().__init__(name, price)
        self.manual_scanner = manual_scanner


class Xerox(Equipment):
    color_copier: bool

    def __init__(self, name, price, color_copier = True):
        super().__init__(name, price)
        self.color_copier = color_copier


class Storage:
    storage = {}
    departments = {}

    def __init__(self, department: tuple):
        self.storage = {}
        for el in department:
            if type(el) != str:
                self.departments = {}
                print('Передан не список названий подразделений')
                return
            self.departments[el] = {}

    def __repr__(self):
        return str(self.storage) + '\n' + str(self.departments)

    def add_position(self, equipment):
        self.storage[equipment] = 0

    def add_to_storage(self, item, count):
        if type(count) != int or count <= 0:
            print('Количество должно быть положительным')
            return
        if not isinstance(item, (Printer, Scaner, Xerox)):
            print('Это не оргтехника')
            return
        self.storage[item] += count

    def move_to_department(self, item, count, department):
        if type(count) != int or count <= 0:
            print('Количество должно быть положительным')
            return
        if not isinstance(item, (Printer, Scaner, Xerox)):
            print(f'Перемещение в '
                  f'"{department}" не оргтехники')
            return
        if self.storage[item] - count < 0:
            print(f'Запрошенное количество '
                  f'"{item.name}" '
                  f'на складе отсутствует')
            return
        self.storage[item] -= count
        if item in self.departments[department].keys():
            self.departments[department][item] += count
        else:
            self.departments[department][item] = count


def moving():
    storage = Storage(('Бухглатерия', 'Отдел кадров'))

    xerox = Xerox('HP', 5000)
    storage.add_position(xerox)

    scaner = Scaner('Canon', 3000, manual_scanner = False)
    storage.add_position(scaner)

    printer = Printer('Epson', 6500)
    storage.add_position(printer)
    print(f'Остатки на складе и в отделах: {storage}')

    print('\nДобавляем на склад:')
    storage.add_to_storage(xerox, 11)
    storage.add_to_storage(scaner, 13)
    storage.add_to_storage(printer, 20)
    print(storage)

    print('\nПеремещяем в отдел: ')
    storage.move_to_department(xerox, 1, 'Бухглатерия')
    print(storage)
    storage.move_to_department(xerox, 3, 'Отдел кадров')
    print(storage)

    print('\nПеремещение больше имеющегося на складе:')
    storage.move_to_department(scaner, 20, 'Отдел кадров')


if __name__ == '__main__':
    moving()
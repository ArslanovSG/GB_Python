# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)


    def go(self):
        return f'{self.name} поехал'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} {self.speed} км/ч')

        if self.speed > 65:
            return f'Скорость {self.name} выше, чем допустимо для городского автомобиля'
        else:
            return f'Скорость {self.name} нормальная для городского автомобиля'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} {self.speed} км/ч')

        if self.speed > 40:
            return f'{self.speed} км/ч. Скорость {self.name} выше, чем допускают для рабочего автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'

mclaren = SportCar(100, 'Красный', 'Макларен', '')
hyundai = TownCar(55, 'Желтый', 'Хёндэ', '')
kamaz = WorkCar(70, 'Оранжевый', 'Камаз', '')
ford = PoliceCar(110, 'Голубой', 'Форд', '')

print(kamaz.turn_left())
print(f'Когда {hyundai.turn_right()}, тогда {mclaren.stop()}')
print(f'{kamaz.go()} со скоростью {kamaz.show_speed()}')
print(f'{kamaz.name} {kamaz.color}')
print(f'{mclaren.name} полицейский автомобиль? {mclaren.is_police}')
print(f'{ford.name} полицейский автомобиль? {ford.is_police}')
print(mclaren.show_speed())
print(hyundai.show_speed())
print(ford.police())
print(ford.show_speed())
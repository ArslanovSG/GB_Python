# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
# название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
# быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом
# уроке знания: реализовать абстрактные классы для основных классов проекта, проверить
# на практике работу декоратора @property.

class Clothes():

    def __init__(self, attrs: int):
        self.attrs = attrs

class Coat(Clothes):

    @property
    def material(self):
        return self.attrs / 6.5 + 0.5

class Сostume(Clothes):

    @property
    def material(self):
        return 2 * self.attrs + 0.3

class Total(Clothes):

    def __init__(self, attrs: int, attrs1: int):
        super().__init__(attrs)
        self.attrs = attrs
        self.attrs1 = attrs1

    @property
    def material(self):
        return self.attrs / 6.5 + 0.5 + 2 * self.attrs1 + 0.3

size = 50
heigth = 10

object_coat = Coat(size)
object_costume = Сostume(heigth)
object_total = Total(size, heigth)

print(f"Расход ткани на пальто: {object_coat.material:.2f}")
print(f"Расход ткани на костюм: {object_costume.material:.2f}")
print(f"Общий расход: {object_total.material:.2f}")

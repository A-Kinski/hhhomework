class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, carsList):
        self.carsList = carsList

    def add(self, car):
        self.carsList.append(car)

    def delete(self, index):
        del self.carsList[index]


# if __name__ == '__main__':
#     car1 = Car('mark1', 'model1')
#     car2 = Car('mark2', 'model2')
#     cars = [car1, car2]
#     garage = Garage(cars)
#     car3 = Car('mark3', 'model3')
#     garage.add(car3)
#     print(garage.carsList)
#     garage.delete(1)
#     print(garage.carsList)

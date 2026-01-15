#Завдання 3
class Vehicle:
    def __init__(self, name,speed):
        self.name = name
        self.speed = speed

    def moving(self):
        print(f"{self.name} Рухається зі швидкістю {self.speed} км/год")


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


class Train(Vehicle):
    pass


car = Car("Автомобіль",90)
bike = Bike("Велосипед",25)
train = Train("Потяг",120)

car.moving()
bike.moving()
train.moving()

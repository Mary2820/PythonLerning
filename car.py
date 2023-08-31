# Создайте класс Car. Добавьте обязательные атрибуты класса: модель, год выпуска, объем двигателя, цена, пробег, количество колес = 4.
# Создайте 1 экземпляр класса
# Добавить метод возвращающий информацию по созданному объекту.
# Создать класс наследник - Грузовик. Который наследует все атрибуты класса, но количество колес = 8.
# Создать 1 экземпляр класса Наследника

class Car():

    def __init__(self, model, manufacturing_year, engine_capacity, price, mileage):
        self.model = model
        self.manufacturing_year = manufacturing_year
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.wheel_number = 4

    def car_information(self):
        information = 'модель: ' + self.model + ', год выпуска: ' + str(self.manufacturing_year) + ', объем двигателя: ' + str(self.engine_capacity) + ', цена: ' + str(self.price) + ', пробег: ' + str(self.mileage) + ', количество колес: ' + str(self.wheel_number)
        return information


car1 = Car('BMW', 2010, 1596, 90000, 563)
print('Основная информация об автомобиле: ' + car1.car_information())

class Truck(Car):

    def __init__(self, model, manufacturing_year, engine_capacity, price, mileageself):
        super(). __init__(model, manufacturing_year, engine_capacity, price, mileageself)
        self.wheel_number = 8

car2 = Truck('Маз', 2008, 2561, 30000, 1000)
print('Основная информация о грузовике: ' + car2.car_information())

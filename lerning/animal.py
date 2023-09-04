class Animal():

    def __init__(self, family, name, age, color):
        self.family = family
        self.name = name
        self.age = age
        self.color = color
        print('Животное создано')

    def sleep(self):
        print(self.name + ' спит')

    def play(self):
        print(self.name + ' играет')

    def colour(self):
        print(self.family + ' ' + self.name + ' имеет ' + self.color + ' окрас')

animal1 = Animal('Лев', 'Симба', '5', 'рыжий')
animal2 = Animal('Кот', 'Фог', '2', 'серый')
animal3 = Animal('Зебра', 'Мартин', '6', 'черно-белый')

animal1.colour()
animal2.colour()
animal3.colour()
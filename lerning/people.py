class Person():

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        description = self.name + ', ему ' + str(self.age) + ', рост ' + str(self.height) + ' см, вес ' + str(self.weight) + ' кг.'
        print('Созданного человека зовут ' + description)

    def update_weight(self, kg):
        self.weight = kg
        # print('Теперь ' + self.name + ' весит ' + str(self.weight) + ' кг.')
        return self.weight

# man = Person('Харри', 45, 175)
# man.description_person()
#
woman = Person('Алиша', 28, 172)
woman.description_person()
woman.update_weight(49)


class Girl(Person):

    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.color = 'рыжий'

    def hair(self, hair_color):
        self.color = hair_color
        # print('У нее ' + self.color + ' цвет волос.')
        return self.color

    def description_person(self):
        description = self.name + ', ей ' + str(self.age) + ', у нее ' + self.color + ' цвет волос.'
        print('Девушку зовут ' + description)


woman1 = Girl('Даяна', 19, 165)
woman1.description_person()

class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increment_population()

    @classmethod
    def increment_population(cls):
        cls.population += 1


    
person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  #
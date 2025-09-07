from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human (Animal):
    def move(self):
        print('i can walk and run')

class Snake(Animal):
    def move(self):
        print(' i can crawl')

class Dog(Animal):
    def move(self):
        print('i can bark')

class Lion(Animal):
    def move(self):
        print('i can roar')

R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()
K = Lion()
K.move()





class India():
    def capital (self):
        print('New Dehli is the capital of India')
    def language(self):
        print('Hindi is the most widely spoken language of India')
    def type(self):
        print('India is a developing country')


class USA():
    def capital (self):
        print('Washington, D.C. is the capital of USA')
    def language(self):
        print('English is the most widely spoken language of USA')
    def type(self):
        print('USA is a developed country')

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
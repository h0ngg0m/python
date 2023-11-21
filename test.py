class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print('move')

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('bark')

class Cat(Animal):
    def speak(self):
        print('meow')

dog = Dog('doggy')
dog.speak() # bark

cat = Cat('kitty')
cat.speak() # meow
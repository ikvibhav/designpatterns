from abc import ABC, abstractmethod

# Define an interface using ABC (Abstract Base Class)
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Dog(Animal):
    def eat(self):
        print("Dog is eating")

    def sleep(self):
        print("Dog is sleeping")

class Cat(Animal):
    def eat(self):
        print("Cat is eating")

    def sleep(self):
        print("Cat is sleeping")

# Usage
dog = Dog()
cat = Cat()

dog.eat()
dog.sleep()

cat.eat()
cat.sleep()
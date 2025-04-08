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
    
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def eat(self):
        print("Cat is eating")

    def sleep(self):
        print("Cat is sleeping")
    
    def meow(self):
        print("Cat is meowing")


# Usage
dog = Dog()
cat = Cat()

dog.eat()
dog.sleep()
dog.bark()

cat.eat()
cat.sleep()
cat.meow()
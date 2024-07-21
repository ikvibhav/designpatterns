# Define a parent class
class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

# Define a child class that inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Define another child class that inherits from Animal
class Cat(Animal):
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
# Designpatterns

## Creational Design Patterns
- Handles creating and cloning new objects

### Singleton
- Intent -
    - Only one object of a class.
    - Single object globally accessible within the program
- Implementation -
    - A private constructor with a public method that instantiates the class if it is not already instantiated

### Factory Method

#### Factory Object
- Intent - 
    - To create "product" objects of particular type that multiple clients can use
    - Codes to an interface, not an implementation
- Implementation
    - An abstract base class/interface that provides an abstract method.
    - Concrete implementations are made of this abstract method
    - A static method then returns a concrete implementation of the abstract method, based on the provided type


## Misc
- lazy creation - object is not created until its truly needed
- concrete instantiation - The act of instantiating a class to create an object of a specific type (In Java with new operator)
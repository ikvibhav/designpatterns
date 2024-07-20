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

## Creational Design Patterns

### Facade Pattern
- Intent
    - To give a point of entry to the subsystem
    - A facade pattern acts as a wrapper class that encapsulates a subsystem in oorder to hide the subsystem's complexity

- Implementation
    - Facade class Encapsulates subsystem classes into facade class (Encapsulation).
    - Facade class hides implementation of subsystem classes from the client class (Information Hiding)
    - Each subsystem class performs a seperate functionality (seperation of concerns)
    - Steps -
        - Step1 - Design the interface
        - Step2 - Implement the interface with one or more classes
        - Step3 - Create the facade class and wrap the classes that implement the interface
        - Step4 - Use facade class to access the subsystem


### Adapter Pattern
- Intent
    - To solve the problem of "Output of one system does not conform to the input of another system" (Eg, a client code with a third party library)

- Implementation
    - Step1 - Design the Target Interface
    - Step2 - Implement the Target Interface with the adapter class
    - Step3 - Implement the Target Interface with the adapter class

### Composite Pattern
- Intent
    - To compose nested structures of objects
    - To deal with classes for these objects uniformly

- Implementation
    - Step1 - Design the interface that defines the overall type
    - Step2 - Implement the composite class
    - Step3 - Implement the leaf class

### Proxy Pattern 
- Intent
    - To implement a simplified or lightweight version of the original object
    - A proxy class can protect the overload of real subject classes
    - A proxy class can act as a local interface for a remote system

- Implementation
    - Step1 - Design the subject interface
    - Step2 - Implement the real subject class
    - Step3 - Implement the proxy class

### Decorator Pattern
- Intent
    - To allow additional behaviour to be dynamically attached to the object

- Implementation
    - Step1 - Design the component interface
    - Step2 - Implement the interface of the base concrete class
    - Step3 - Implement the interface of the abstract decorator class
    - Step4 - Inherit from abstract decorator and implement the component interface with concrete decorator classes

## Misc
- lazy creation - object is not created until its truly needed
- concrete instantiation - The act of instantiating a class to create an object of a specific type (In Java with new operator)
- recursive composition - Allows objects to be composed of other objects that are of a common type
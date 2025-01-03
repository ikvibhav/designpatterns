# Software Design Patterns
This repository -
1. Presents commonly used design patterns in a tabular format
2. Explains each pattern using PUML Architecture diagrams
3. Explains each pattern using Python and Java Code

## Creational Design Patterns

| S.No | Pattern            | Intent                                                                 | Implementation                                                                                       |
|------|--------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| 1    | **Singleton**      | Only one object of a class. Single object globally accessible.         | Private constructor, public method to instantiate if not already instantiated.                       |
| 2    | **Factory Method** | Create "product" objects of a particular type for multiple clients.    | Abstract base class/interface with an abstract method. Concrete implementations and a static method. |
| 3    | **Abstract Factory Method** | Create multiple types of factories for multiple "product" objects    | Create an Abstract Factory Method that can be used by multiple factories. Declare interfaces for each distinct product. |
| 4    | **Facade Pattern** | Entry point to a subsystem, hides complexity.                          | Design interface, implement with classes, create facade class, wrap classes, use facade class.       |
| 5    | **Adapter Pattern**| Solve "Output of one system does not conform to input of another".     | Design Target Interface, implement with adapter class.                                               |
| 6    | **Composite Pattern** | Compose nested structures of objects, deal with classes uniformly.  | Design interface, implement composite class, implement leaf class.                                   |
| 7    | **Proxy Pattern**  | Simplified/lightweight version of the original object.                 | Design subject interface, implement real subject class, implement proxy class.                       |
| 8    | **Decorator Pattern** | Dynamically attach additional behavior to objects.                 | Design component interface, implement base concrete class, implement abstract decorator class, inherit and implement with concrete decorator classes. |

## Behavioural Design Patterns

| S.No | Pattern                   | Intent                                                                 | Implementation                                                                                       |
|------|---------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| 1    | **Template Method**       | Create the implementation steps in function methods                    | Superclass - A Public Template Method and multiple abstract methods. Individual Subclasses implement the abstract methods. |
| 2    | **Chain of Responsibility** | To process a single request using a chain of multiple handlers         | Define an interface for handling requests. Concrete handlers implement the handler interface.        |
| 3    | **State**                 | To allow an object to change its behaviour dynamically based on its internal state | Define an interface and context class. Interface handles requests and transitions. Context Class maintains current state, delegates requests and coordinates state changes. |
| 4    | **Command**               | To allow parameterization of different requests through object encapsulation | Define command interface and implement command interface with references to receiver objects. Implement an Invoker class that stores and executes commands. |
| 5    | **Mediator**              | To provide communication mechanism between different components (colleagues) instead of components communicating directly with each other | Define a mediator interface and a concrete mediator for communication between colleague components (objects). |
| 6    | **Observer**              | To enable an object (the subject) to maintain and notify a list of dependents (the observers) | Define a subject class (add, remove and notify) and observers to define how they react to changes from the subject. |

## Misc

| S.No | Concept                | Description                                                                 |
|------|------------------------|-----------------------------------------------------------------------------|
| 1    | **Lazy Creation**      | Object is not created until it's truly needed.                              |
| 2    | **Concrete Instantiation** | Instantiating a class to create an object of a specific type (e.g., `new` in Java). |
| 3    | **Recursive Composition** | Allows objects to be composed of other objects of a common type.         |
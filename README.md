## Creational Design Patterns

| S.No | Pattern            | Intent                                                                 | Implementation                                                                                       |
|------|--------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| 1    | **Singleton**      | Only one object of a class. Single object globally accessible.         | Private constructor, public method to instantiate if not already instantiated.                       |
| 2    | **Factory Method** | Create "product" objects of a particular type for multiple clients.    | Abstract base class/interface with an abstract method. Concrete implementations and a static method. |
| 3    | **Factory Method** | Create multiple types of factories for multiple "product" objects    | Create an Abstract Factory Method that can be used by multiple factories. Declare interfaces for each distinct product. |
| 4    | **Facade Pattern** | Entry point to a subsystem, hides complexity.                          | Design interface, implement with classes, create facade class, wrap classes, use facade class.       |
| 5    | **Adapter Pattern**| Solve "Output of one system does not conform to input of another".     | Design Target Interface, implement with adapter class.                                               |
| 6    | **Composite Pattern** | Compose nested structures of objects, deal with classes uniformly.  | Design interface, implement composite class, implement leaf class.                                   |
| 7    | **Proxy Pattern**  | Simplified/lightweight version of the original object.                 | Design subject interface, implement real subject class, implement proxy class.                       |
| 8    | **Decorator Pattern** | Dynamically attach additional behavior to objects.                 | Design component interface, implement base concrete class, implement abstract decorator class, inherit and implement with concrete decorator classes. |

## Misc

| S.No | Concept                | Description                                                                 |
|------|------------------------|-----------------------------------------------------------------------------|
| 1    | **Lazy Creation**      | Object is not created until it's truly needed.                              |
| 2    | **Concrete Instantiation** | Instantiating a class to create an object of a specific type (e.g., `new` in Java). |
| 3    | **Recursive Composition** | Allows objects to be composed of other objects of a common type.         |
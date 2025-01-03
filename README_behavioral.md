# Designpatterns

## Behavioural Design Patterns

### Template Method Pattern
- Intent
    - Create the implementation steps in function methods
- Implementation
    - Superclass - A Public Template Method and multiple abstract methods. Individual Subclasses implement the abstract methods

### Chain of Responsibility Pattern
- Intent
    - To Process a single request using a chain of multiple handlers
- Implementation
    - Define an interface for handling requests. Concrete handlers implement the handler interface

### State Pattern
- Intent
    - To allow an object to change its behaviour dynamically based on its internal state
- Implementation
    - Define an interface and context class. Interface handles requests and transitions.Context Class maintains current state, delegates requests and coordinates state changes

### Command Pattern
- Intent
    - To allow parameterization of different requests through object encapsulation.
- Implementation
    - Define command interface and implement command interface with references to receiver objects. Implement an Invoker class that stores and executes commands

### Mediator Pattern
- Intent
    - To provide communication mechanism between different components (colleagues) instead of components communication directly with each other
- Implementation
    - Define a mediator interface and a concrete mediator for communication b/w colleague components (objects).

### Observer Pattern
- Intent
    - To enable an object (the subject) to maintain and notify a list of dependents (the observers)
- Implementation
    - Define a subject class (add, remove and notify) and observers to define how it reacts from the subject
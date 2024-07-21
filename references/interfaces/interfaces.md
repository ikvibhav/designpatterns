# What?
- An interface is a set of methods that a class must implement
- It does not contain implementation of methods, only the signatures

# Why?
- Provide a way to achieve abstraction
- Defines a common protocol that different classes can follow
- For polymorphism

# How?
- A class that implements an interface must provide all the concrete implementations

# Misc Questions

## Is interfaces preferred or inheritence?
- Choice b/w interface and inheritence depends on the specific requirements of design.
- Interfaces is preferred in the need to -
    - Define a contract that multiple classes should follow
    - Achieve Polymorphism and decoupling
    - Implement multiple behaviours unrelated to one another
- Inheritence is preferred in the need to -
    - Define clear parent-child relationships
    - Reuse code from parent class
    - Extend functionality of an existing class
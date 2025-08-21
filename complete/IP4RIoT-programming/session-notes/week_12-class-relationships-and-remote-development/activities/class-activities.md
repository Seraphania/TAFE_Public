# Overview

Examine the relationships presented in today's presentation, and implement an association, aggregation, and composition relationship that closely mirrors those models.

- Use PEP8 regardless of the naming conventions in the UML diagrams
- Place each class in its own file and use imports as appropriate
- Use a main.py file to instantiate your objects and test your code
- You may also want to practice the example generalization and realization relationships

## Your notes
Before you begin write down what each of the relationships mean and try and recall how they are represented in UML:

- Association:
  - > Describes how instances are created between objects, for example if one object creates an instance of another.
- Generalization:
  - > Also called inheritance, one object derives some or all of its attributes and behaviours from another.
- Realization:
  - > Similar to inheritance relationships, however the parent object is an interface (an abstract class with abstract methods that cannot be instantiated). These are most commonly used to describe behaviours.
- Aggregation:
  - > Models objects that contain other objects, where the contained objects are able to exist independantly from the 'parent' object, and can be moved between different instances of the same type as the parent.
- Composition:
  - > Similar to aggregation, however the contained objects can not exist independantly from the container, or be moved between containers.

What is cardinality and how is it represented in UML? Try and think of a few examples.
  - > Cardinality descrbes the multiplicity in relationships, whether an object relates to one or many instances of another object it is related to.
## Tips

- Some of the diagrams have been reproduced in mermaid syntax, see:
  - [Association](./association/association.md)
  - [Aggregation](./aggregation/aggregation.md)
  - [Composition](./composition/composition.md)

- There are solutions to the examples in a separate branch: `2024/s2/raf-solutions` but try not to rely on those!

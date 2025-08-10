# Composition

A composition relationship is a type of aggregation where the contained object cannot exist independently of the containing object. In other words, the contained object is dependent on the containing object and will be destroyed when the containing object is destroyed.

In UML, a composition relationship is represented by a filled diamond shape pointing to the containing object.

## UML Example

```mermaid
classDiagram
    class House {
        +String address
        +addRoom(Room)
    }
    class Room {
        +String name
        +double area
    }
    House *-- "1..*" Room : consists of

```

## Python Implementation

```python
# room.py
class Room():
    def __init__(self, name: str, area: float):
        self.name = name
        self.area = area

# house.py
from room import Room

class House():
    def __init__(self, address: str):
        self.address = address
        self.rooms = []

    def add_room(self, name, area):
        room = Room(name, area)
        self.rooms.append(room)

# main.py
from house import House

house = House("17, Street St, Applecross, WA 6000")
room1 = house.add_room("bedroom", 30.0)
room2 = house.add_room("bathroom", 25.0)

print(house.address)
```

from room import Room

class House():
    def __init__(self, address: str):
        self.address = address
        self.rooms = []

    def add_room(self, name, area):
        room = Room(name, area)
        self.rooms.append(room)
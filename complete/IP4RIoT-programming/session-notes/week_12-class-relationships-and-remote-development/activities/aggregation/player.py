class Player:
    def __init__(self, name, position): # could have used type hinting
        self.name = name
        self.position = position

    def play(self):
        print(f"{self.name} plays {self.position} position")
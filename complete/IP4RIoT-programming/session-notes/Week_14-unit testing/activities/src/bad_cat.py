class Cat:
    def __init__(self, name, coat):
        self.name = name
        # Bug: forgot to assign coat

    def speak(self):
        return f"{self.name} says meow in a {self.coat} coat"
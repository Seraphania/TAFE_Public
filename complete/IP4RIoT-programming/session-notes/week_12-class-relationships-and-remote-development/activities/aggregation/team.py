from player import Player # Required if doing type hinting

class Team():
    def __init__(self, name: str): # Not necessary, but nice (type hinting)
        self.name = name
        self.players = []

    def add_player(self, player: Player): # Type hint for my own class!
        self.players.append(player) # a check if the player was in players[] would be nice
        return self.players # Not necessary unless the list is needed

    def remove_player(self, player: Player): # could `player: "Player"`` if not importing but it's jank.
        self.players.remove(player)
        return self.players
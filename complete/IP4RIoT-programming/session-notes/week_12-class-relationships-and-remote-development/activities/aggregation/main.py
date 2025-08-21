from player import Player
from team import Team

player1 = Player("Zorp \'Meatspin\' Vangelis", "Hyperflanker")
player2 = Player("Midge Chromefinger", "Backfield Distractor")

team = Team("Quantum Ferrets")
team.add_player(player1)
team.add_player(player2)

for player in team.players:
    player.play()
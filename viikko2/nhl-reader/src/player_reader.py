import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

        self.get_players = self.player_parse()

    def player_parse(self):
        response = requests.get(self.url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players
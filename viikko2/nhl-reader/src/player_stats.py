class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):

        def player_order(player):
            return player.points

        players = []

        for player in self.reader.get_players:
            if player.nationality == nationality:
                players.append(player)
        
        sorted_players = sorted(players, key=player_order, reverse=True)

        return sorted_players
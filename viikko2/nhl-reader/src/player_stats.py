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

    def top_scorers_by_team(self, team):
        players = [
            player for player in self.reader.get_players
            if player.team == team
        ]

        return sorted(players, key=lambda player: player.points, reverse=True)

    def fix_pylint_method_count(self):
        return

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa."""

        players = sorted(
            self.reader.get_players,
            key=lambda player: player.goals,
            reverse=True
        )

        return players[:how_many]

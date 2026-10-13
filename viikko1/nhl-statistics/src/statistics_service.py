from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, reader):
        self._reader = reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, function = None):

        if not function:
            # metodin käyttämä apufufunktio voidaan määritellä näin
            def sort_by_points(player):
                return player.points

            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_points
            )

            result = []
            i = 0
            while i <= how_many - 1:
                result.append(sorted_players[i])
                i += 1

            return result

        else:
            def sort_by_enum(player):
                if function.name == "POINTS":
                    return player.points
                elif function.name == "GOALS":
                    return player.goals
                else:
                    return player.assists
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_enum
            )

            result = []
            i = 0
            while i <= how_many - 1:
                result.append(sorted_players[i])
                i += 1

            return result


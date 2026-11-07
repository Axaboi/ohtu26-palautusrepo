import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def __init__(self, players):
        self.get_players = players


class PlayerStatsTest(unittest.TestCase):
    def setUp(self):
        players = [
            Player({
                "name": "Finn One",
                "nationality": "FIN",
                "assists": 70,
                "goals": 30,
                "team": "AAA",
            }),
            Player({
                "name": "Finn Two",
                "nationality": "FIN",
                "assists": 40,
                "goals": 20,
                "team": "BBB",
            }),
            Player({
                "name": "Canadian One",
                "nationality": "CAN",
                "assists": 80,
                "goals": 50,
                "team": "AAA",
            }),
        ]
        self.stats = PlayerStats(PlayerReaderStub(players))

    def test_top_scorers_by_nationality_returns_matching_players_in_points_order(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual([player.name for player in players], ["Finn One", "Finn Two"])
        self.assertTrue(all(player.nationality == "FIN" for player in players))

    def test_top_scorers_by_nationality_returns_empty_list_when_no_players_match(self):
        self.assertEqual(self.stats.top_scorers_by_nationality("SWE"), [])

    def test_top_scorers_by_team_returns_matching_players_in_points_order(self):
        players = self.stats.top_scorers_by_team("AAA")

        self.assertEqual([player.name for player in players], ["Canadian One", "Finn One"])
        self.assertTrue(all(player.team == "AAA" for player in players))

    def test_top_goal_scorers_returns_requested_number_in_goal_order(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual([player.name for player in players], ["Canadian One", "Finn One"])
        self.assertEqual([player.goals for player in players], [50, 30])


if __name__ == "__main__":
    unittest.main()

import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReadersStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReadersStub())

    def test_konstruktori_asettaa_viisi_pelaajaa_oikein(self):
        player_count = len(self.stats._players)

        self.assertEqual(player_count, 5)

    def test_pelaaja_loytyy(self):
        player_comparison = self.stats._players[0]

        player_search = self.stats.search("Semenko")

        self.assertEqual(player_comparison, player_search)

    def test_pelaaja_ei_loydy(self):
        player_search = self.stats.search("Pelaaja")

        self.assertEqual(player_search, None)

    def test_joukkueen_pelaajat(self):
        comparison_team = ["Semenko", "Kurri", "Gretzky"]
        
        team = self.stats.team("EDM")

        team_players = [i.name for i in team]

        self.assertEqual(comparison_team, team_players)

    def test_pistejarjestys_pelaajat_kaikki(self):
        comparison_players = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]

        player_count = len(comparison_players)

        players = self.stats.top(player_count)

        player_names = [i.name for i in players]

        self.assertEqual(comparison_players, player_names)

    def test_pistejarjestys_pelaajat_osa(self):
        comparison_players = ["Gretzky", "Lemieux", "Yzerman"]

        player_count = len(comparison_players)

        players = self.stats.top(player_count)

        player_names = [i.name for i in players]

        self.assertEqual(comparison_players, player_names)

    def test_enum_jarjestys_kokonaispisteet(self):
        comparison_players = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]

        player_count = len(comparison_players)

        players = self.stats.top(player_count, SortBy.POINTS)

        player_names = [i.name for i in players]

        self.assertEqual(comparison_players, player_names)

    def test_enum_jarjestys_maalit(self):
        comparison_players = ["Lemieux", "Yzerman", "Kurri", "Gretzky", "Semenko"]

        player_count = len(comparison_players)

        players = self.stats.top(player_count, SortBy.GOALS)

        player_names = [i.name for i in players]

        self.assertEqual(comparison_players, player_names)

    def test_enum_jarjestys_syotot(self):
        comparison_players = ["Gretzky", "Yzerman", "Lemieux", "Kurri", "Semenko"]

        player_count = len(comparison_players)

        players = self.stats.top(player_count, SortBy.ASSISTS)

        player_names = [i.name for i in players]

        self.assertEqual(comparison_players, player_names)
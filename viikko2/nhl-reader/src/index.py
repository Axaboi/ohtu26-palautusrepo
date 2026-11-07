import rich.prompt
from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def create_stats():
    season = rich.prompt.Prompt.ask(
        "Season", choices=["2018-19", "2019-20", "2020-21", "2021,22", "2022-23",
                           "2023-24", "2024-25", "2025-26"], default="2024-25"
    )
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    return season, reader, PlayerStats(reader)


def select_players(reader, stats):
    filter_type = rich.prompt.Prompt.ask(
        "Filter by", choices=["Nationality", "Team"])

    if filter_type == "Nationality":
        nationality = rich.prompt.Prompt.ask(
            "Nationality", choices=["USA", "FIN", "CAN", "SWE", "CZE",
                                    "RUS", "SLO", "FRA", "GBR", "SVK",
                                    "DEN", "NED", "AUT", "BLR", "GER",
                                    "SUI", "NOR", "UZB", "LAT", "AUS"])
        players = stats.top_scorers_by_nationality(nationality)
        title = f"Season players from {nationality}"
    else:
        teams = sorted({player.team for player in reader.get_players})
        team = rich.prompt.Prompt.ask("Team", choices=teams)
        players = stats.top_scorers_by_team(team)
        title = f"Season players from {team}"

    return players, title


def print_players(players, title, season):
    console = Console()
    table = Table("Released", "teams", "goals", "assists", "points",
                  title=f"Season {season} {title}")

    for player in players:
        table.add_row(f"{player.name}", f"{player.team}", f"{player.goals}",
                      f"{player.assists}", f"{player.points}")

    console.print(table)


def main():
    season, reader, stats = create_stats()

    while True:
        players, title = select_players(reader, stats)
        print_players(players, title, season)


if __name__ == "__main__":
    main()

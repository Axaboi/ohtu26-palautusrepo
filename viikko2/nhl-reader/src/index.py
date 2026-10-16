import rich.prompt
from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    season = rich.prompt.Prompt.ask(
        "Season", choices=["2018-19", "2019-20", "2020-21", "2021,22", "2022-23",
                           "2023-24", "2024-25", "2025-26"], default="2024-25"
    )
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = rich.prompt.Prompt.ask(
            "Nationality",  choices=["USA", "FIN", "CAN", "SWE", "CZE",
                                    "RUS", "SLO", "FRA", "GBR", "SVK",
                                    "DEN", "NED", "AUT", "BLR", "GER",
                                    "SUI", "NOR", "UZB", "LAT", "AUS"])

        players = stats.top_scorers_by_nationality(nationality)

        console = Console()

        table = Table(title=f"Season {season} players from {nationality}")

        table.add_column("Released", justify="right", style="cyan", no_wrap=True)
        table.add_column("teams", style="magenta")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")

        for player in players:
            table.add_row(f"{player.name}", f"{player.team}", f"{player.goals}", f"{player.assists}", f"{player.points}")

        console.print(table)


if __name__ == "__main__":
    main()


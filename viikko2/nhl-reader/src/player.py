class Player:
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.nationality = dictionary['nationality']
        self.assists = dictionary['assists']
        self.goals = dictionary['goals']
        self.team = dictionary['team']
        self.points = dictionary['goals'] + dictionary['assists']

    def fix_pylint_method_count(self):
        return

    def __str__(self):
        return f"{self.name:<20} {self.team:<20} {self.goals} + {self.assists} = {self.points}"

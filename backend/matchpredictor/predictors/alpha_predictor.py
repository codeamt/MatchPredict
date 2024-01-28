from matchpredictor.predictors.predictor import Prediction, Predictor
from matchpredictor.matchresults.result import Fixture, Outcome, Result, Team


#A function that sorts two teams by name alphabetically
def sort_teams(team1: Team, team2: Team) -> Tuple[Team, Team]:
    if team1.name < team2.name:
        return (team1, team2)
    else:
        return (team2, team1)

# AlphaPredictor is a predictor that arranges teams by name alphabetically, and predictas the first team to win.
class AlphaPredictor(Predictor):
    def predict(self, fixture: Fixture) -> Prediction:
        team1, team2 = sort_teams(fixture.home_team, fixture.away_team)
        return Prediction(team1, 1.0, team2, 0.0)
        
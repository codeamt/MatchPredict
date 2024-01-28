from matchpredictor.predictors.predictor import Prediction, Predictor
from matchpredictor.matchresults.result import Fixture, Outcome, Team


#A function that sorts two teams by name alphabetically
def sort_teams(team1: Team, team2: Team) -> Outcome:
    if team1.name < team2.name:
        return Outcome.AWAY
    else:
        return Outcome.HOME

# AlphaPredictor is a predictor that arranges teams by name alphabetically, and predictas the first team to win.
class AlphaPredictor(Predictor):
    def predict(self, fixture: Fixture) -> Prediction:
        outcome = sort_teams(fixture.home_team, fixture.away_team)
        return Prediction(outcome, 1.0)
        
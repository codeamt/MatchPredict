from typing import List
import random

from matchpredictor.matchresults.result import Fixture, Outcome, Team
from matchpredictor.predictors.predictor import Predictor, Prediction

from matchpredictor.teams.teams_provider import TeamsProvider

# A Predictor subclass, CustomPredictor.
class CustomPredictor(Predictor):
    def predict(self, fixture: Fixture) -> Prediction:
        # Get the home and away teams from the fixture
        home_team = fixture.home_team
        away_team = fixture.away_team

        # If the home team's name is longer than the away team's name, return "home"
        if len(home_team.name) > len(away_team.name):
            return Prediction(Outcome.HOME)
        # If the away team's name is longer, return "away"
        elif len(home_team.name) < len(away_team.name):
            return Prediction(Outcome.AWAY)
        # Otherwise, predict a draw
        else:
            return Prediction(Outcome.DRAW)
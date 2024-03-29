#a measurement test for my alphabet model in the backend/test/predictors directory
# Path: backend/test/predictors/measure_alpha_predictor.py
from unittest import TestCase

from matchpredictor.evaluation.evaluator import Evaluator
from matchpredictor.matchresults.results_provider import training_results, validation_results  
from matchpredictor.predictors.alpha_predictor import AlphaPredictor
from test.predictors import csv_location

class TestAlphaPredictor(TestCase):
    def test_accuracy(self) -> None:
        #training_data = training_results(csv_location, 2019)
        validation_data = validation_results(csv_location, 2019)
        predictor = AlphaPredictor()

        accuracy, _ = Evaluator(predictor).measure_accuracy(validation_data)

        self.assertGreaterEqual(accuracy, .33)
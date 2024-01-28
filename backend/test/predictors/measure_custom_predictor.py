#a measurement test for CustomPredictor in the backend/test/predictors directory
# Path: backend/test/predictors/measure_custom_predictor.py
from unittest import TestCase

from matchpredictor.evaluation.evaluator import Evaluator
from matchpredictor.matchresults.results_provider import training_results, validation_results  
from matchpredictor.predictors.custom_predictor import CustomPredictor
from test.predictors import csv_location

class TestCustomPredictor(TestCase):
    def test_accuracy(self) -> None:
        #training_data = training_results(csv_location, 2019)
        validation_data = validation_results(csv_location, 2019)
        predictor = CustomPredictor()

        accuracy, _ = Evaluator(predictor).measure_accuracy(validation_data)

        self.assertGreaterEqual(accuracy, .33)
        self.assertGreaterEqual(accuracy, .35)

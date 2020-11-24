"""Run validation test for your ML program."""
import os
from pathlib import Path
from time import time
import unittest

# from model_core.datasets import TextDataset ImageDataset
# from model_core.predict import ImageClassifier, TextClassifier

os.environ["CUDA_VISIBLE_DEVICES"] = ""

SUPPORT_DIRNAME = Path(__file__).parents[0].resolve() / "support" / "example_data"


class TestEvaluateSomething(unittest.TestCase):
    def test_evaluate(self):
        """Write your own evaluation tests"""

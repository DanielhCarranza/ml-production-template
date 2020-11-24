"""Tests for CharacterPredictor class."""
import os
from pathlib import Path
import unittest

from model_core.predictor import Predictor

SUPPORT_DIRNAME = Path(__file__).parents[0].resolve() / "support" / "support_data"

os.environ["CUDA_VISIBLE_DEVICES"] = ""


class TestPredictor(unittest.TestCase):
    """Tests for the Predictor class."""

    def test_filename(self):
        """Test that Predictor correctly predicts something."""
        predictor = Predictor()

